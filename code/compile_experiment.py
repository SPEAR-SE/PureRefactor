import os
import re
import subprocess

import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
# OpenAI API key
OPENAI_API_KEY = config['OPENAI_API_KEY']
project_prefix_path = config['project_prefix_path']

def run_command(command):
    """run command"""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    success = result.returncode == 0
    if success:
        print(f"Command succeeded: {command}")
    else:
        print(f"Command failed: {command}\n{result.stderr}")
    return success, result

def checkout_commit(commit_hash):
    """checkout commit"""
    return run_command(f"git checkout {commit_hash}")


def replace_java_code(file_path, new_code):
    """replace java code"""
    try:
        with open(file_path, "w") as file:
            file.write(new_code)
        print(f"Replaced code in {file_path}")
        return True
    except Exception as e:
        print(f"Failed to replace code in {file_path}: {e}")
        return False

def compile_project(is_maven = True):
    # success, result = run_command("mvn clean package")
    if is_maven:
        success, result_first = run_command("mvn clean package -Drat.skip=true -Dmaven.javadoc.skip=true")
    else:
        success, result_first = run_command("./gradlew clean build ")
        if not success:
            success, result = run_command("./gradlew clean build  -x checkstyleMain")
        if not success:
            success, result = run_command("./gradlew clean build  -x spotlessJavaCheck")
        if not success:
            success, result = run_command("./gradlew clean build  -x enforceRules")
        if not success:
            success, result = run_command("./gradlew clean build  -x spotlessJava")
    
    str_result = ""
    if not success:
        # build failed log
        if is_maven:
            str_result = "\nBuild failed. Details:\n" + result_first.stdout + result_first.stderr
            ansi_escape = re.compile(r'\x1B\[[0-9;]*[a-zA-Z]')
            str_result = ansi_escape.sub('', str_result)
            str_result = re.findall(r'\[ERROR\].*', str_result)
        else:
            str_result = "\nBuild failed. Details:\n" + result_first.stderr
        print("\nBuild failed. Details:\n")
        print(result_first.stdout)  # print the output
        print("---------------------------------------------------------------line")
        print(result_first.stderr)  # print the error

    return success, str_result

def force_checkout_commit(commit_id):
    """force checkout commit"""
    # Step 1: git reset --hard HEAD
    if not run_command("git reset --hard HEAD"):
        print("Failed to discard changes. Exiting.")
        return False

    # Step 2: checkout the specified commit
    if not run_command(f"git checkout -f {commit_id}"):
        print(f"Failed to checkout commit {commit_id}. Exiting.")
        return False

    print(f"Successfully checked out commit {commit_id}.")
    return True



def compile_current_commit(project_dir, commit_id, compile_jdk):

    compile_result = False
    try:
        os.chdir(project_dir)
        print(f"Switched to project directory: {project_dir}")
    except Exception as e:
        print(f"Failed to switch to directory {project_dir}: {e}")
        return compile_result, "Failed to switch to directory."
    force_checkout_commit(commit_id)
    prev_commit = get_previous_commit(commit_id)
    if not prev_commit:
        print("Failed to retrieve previous commit. Exiting.")
        return compile_result, "Failed to retrieve previous commit."

    if not force_checkout_commit(prev_commit):
        print("Failed to checkout previous commit. Exiting.")
        return compile_result, "Failed to checkout previous commit."

    print("Running Maven build for the previous commit...")
    # modify_build_file(project_dir)
    switch_java_version(compile_jdk)
    is_maven = check_project_type()
    compile_re, log = compile_project(is_maven)
    switch_java_version(17)
    if not compile_re:
        print("Build failed for the previous commit.")
    else:
        print("Build succeeded for the previous commit.")
        compile_result = True
    return compile_result, log

def check_project_type():
    """check project type"""
    print("Checking project type...")
    files = os.listdir(".")
    if "pom.xml" in files:
        return True
    return False

def main(project_dir, commit_id, file_path, new_code):
    compile_result = [False, False, False]
    try:
        os.chdir(project_dir)
        print(f"Switched to project directory: {project_dir}")
    except Exception as e:
        print(f"Failed to switch to directory {project_dir}: {e}")
        return compile_result, "Failed to switch to directory."
    force_checkout_commit(commit_id)

    prev_commit = get_previous_commit(commit_id)
    if not prev_commit:
        print("Failed to retrieve previous commit. Exiting.")
        return compile_result, "Failed to retrieve previous commit."

    if not force_checkout_commit(prev_commit):
        print("Failed to checkout previous commit. Exiting.")
        return compile_result, "Failed to checkout previous commit."
    print("Running Maven build for the previous commit...")
    compile_re, log = compile_project()
    if not compile_re:
        print("Build failed for the previous commit.")
        compile_result[0] = True
        compile_result[1] = True
        compile_result[2] = True
        return compile_result, "Build failed for the previous commit."
    else:
        print("Build succeeded for the previous commit.")
    compile_result[0] = True
    print(f"Replacing code in {file_path}...")
    if not replace_java_code(file_path, new_code):
        print("Failed to replace code. Exiting.")
        return compile_result, "Failed to replace code."

    compile_result[1] = True
    print("Running Maven build after code replacement...")
    is_maven = check_project_type()
    print("is_maven", is_maven)
    compile_result_after_replacement, log = compile_project(is_maven)
    if compile_result_after_replacement:
        print("Build succeeded after code replacement.")
        compile_result[2] = True
        return compile_result, "Build succeeded after code replacement."
    else:
        print("Build failed after code replacement.")
        return compile_result, log




def switch_java_version(version):
    """
    switch java version
    """
    try:
        # build command

        command = ["jenv", "local", str(version)]

        # execute command
        subprocess.run(command, check=True)

        # check if the version is switched
        result = subprocess.run(["jenv", "version"], capture_output=True, text=True, check=True)
        if str(version) in result.stdout:
            print(f"switch Java {version}。")
        else:
            print(f"switch Java {version} failure。version: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"switch Java failure: {e}")
    except FileNotFoundError:
        print("jenv command not found, make sure jenv is properly installed and in your path.")



def get_compile_result_in_commit(project_dir, commit_id, file_path, refactored_code, java_version = 11):
    switch_java_version(java_version)
    compile_result, log = main(project_dir, commit_id, file_path, refactored_code)
    switch_java_version(17)
    try:
        os.chdir(project_prefix_path)
        print(f"Switched to project directory: {project_dir}")
    except Exception as e:
        print(f"Failed to switch to directory {project_dir}: {e}")
    if compile_result[0] and compile_result[1] and compile_result[2]:
        return True, "This commit can be compile and test successfully."
    if compile_result[0] and compile_result[1]:
        return False, log
    if not compile_result[0]:
        raise Exception("Failed to compile the previous commit.")


def get_previous_commit(commit_id):
    """get previous commit"""
    result = subprocess.run(f"git rev-parse {commit_id}~1", shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print(f"Failed to get the previous commit for {commit_id}: {result.stderr}")
        return None

