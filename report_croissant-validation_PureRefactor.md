# CROISSANT VALIDATION REPORT
================================================================================
## VALIDATION RESULTS
--------------------------------------------------------------------------------
Starting validation for file: croissant
### JSON Format Validation
✓
The URL returned valid JSON.
### Croissant Schema Validation
✓
The dataset passes Croissant validation.
### Records Generation Test (Optional)
✓
Record set 'default_splits' passed validation.
Record set 'default' passed validation.
## JSON-LD REFERENCE
================================================================================
```json
{
  "@context": {
    "@language": "en",
    "@vocab": "https://schema.org/",
    "arrayShape": "cr:arrayShape",
    "citeAs": "cr:citeAs",
    "column": "cr:column",
    "conformsTo": "dct:conformsTo",
    "cr": "http://mlcommons.org/croissant/",
    "data": {
      "@id": "cr:data",
      "@type": "@json"
    },
    "dataBiases": "cr:dataBiases",
    "dataCollection": "cr:dataCollection",
    "dataType": {
      "@id": "cr:dataType",
      "@type": "@vocab"
    },
    "dct": "http://purl.org/dc/terms/",
    "extract": "cr:extract",
    "field": "cr:field",
    "fileProperty": "cr:fileProperty",
    "fileObject": "cr:fileObject",
    "fileSet": "cr:fileSet",
    "format": "cr:format",
    "includes": "cr:includes",
    "isArray": "cr:isArray",
    "isLiveDataset": "cr:isLiveDataset",
    "jsonPath": "cr:jsonPath",
    "key": "cr:key",
    "md5": "cr:md5",
    "parentField": "cr:parentField",
    "path": "cr:path",
    "personalSensitiveInformation": "cr:personalSensitiveInformation",
    "recordSet": "cr:recordSet",
    "references": "cr:references",
    "regex": "cr:regex",
    "repeated": "cr:repeated",
    "replace": "cr:replace",
    "sc": "https://schema.org/",
    "separator": "cr:separator",
    "source": "cr:source",
    "subField": "cr:subField",
    "transform": "cr:transform",
    "@base": "cr_base_iri/"
  },
  "@type": "sc:Dataset",
  "distribution": [
    {
      "@type": "cr:FileObject",
      "@id": "repo",
      "name": "repo",
      "description": "The Hugging Face git repository.",
      "contentUrl": "https://huggingface.co/datasets/easenxu/PureRefactor/tree/refs%2Fconvert%2Fparquet",
      "encodingFormat": "git+https",
      "sha256": "https://github.com/mlcommons/croissant/issues/80"
    },
    {
      "@type": "cr:FileSet",
      "@id": "parquet-files-for-config-default",
      "containedIn": {
        "@id": "repo"
      },
      "encodingFormat": "application/x-parquet",
      "includes": "default/*/*.parquet"
    }
  ],
  "recordSet": [
    {
      "@type": "cr:RecordSet",
      "dataType": "cr:Split",
      "key": {
        "@id": "default_splits/split_name"
      },
      "@id": "default_splits",
      "name": "default_splits",
      "description": "Splits for the default config.",
      "field": [
        {
          "@type": "cr:Field",
          "@id": "default_splits/split_name",
          "dataType": "sc:Text"
        }
      ],
      "data": [
        {
          "default_splits/split_name": "train"
        }
      ]
    },
    {
      "@type": "cr:RecordSet",
      "@id": "default",
      "description": "easenxu/PureRefactor - 'default' subset",
      "field": [
        {
          "@type": "cr:Field",
          "@id": "default/split",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "fileProperty": "fullpath"
            },
            "transform": {
              "regex": "default/(?:partial-)?(train)/.+parquet$"
            }
          },
          "references": {
            "field": {
              "@id": "default_splits/split_name"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/type",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "type"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/description",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "description"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/diffLocations",
          "subField": [
            {
              "@type": "cr:Field",
              "@id": "default/diffLocations/endColumn",
              "dataType": "cr:Int64",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "diffLocations"
                },
                "transform": {
                  "jsonPath": "endColumn"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/diffLocations/endLine",
              "dataType": "cr:Int64",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "diffLocations"
                },
                "transform": {
                  "jsonPath": "endLine"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/diffLocations/filePath",
              "dataType": "sc:Text",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "diffLocations"
                },
                "transform": {
                  "jsonPath": "filePath"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/diffLocations/startColumn",
              "dataType": "cr:Int64",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "diffLocations"
                },
                "transform": {
                  "jsonPath": "startColumn"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/diffLocations/startLine",
              "dataType": "cr:Int64",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "diffLocations"
                },
                "transform": {
                  "jsonPath": "startLine"
                }
              }
            }
          ],
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/sourceCodeBeforeRefactoring",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "sourceCodeBeforeRefactoring"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/filePathBefore",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "filePathBefore"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/isPureRefactoring",
          "dataType": "sc:Boolean",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "isPureRefactoring"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/commitId",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "commitId"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/packageNameBefore",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "packageNameBefore"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/classNameBefore",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "classNameBefore"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/methodNameBefore",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "methodNameBefore"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/classSignatureBefore",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "classSignatureBefore"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/methodNameBeforeSet",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "methodNameBeforeSet"
            }
          },
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/classNameBeforeSet",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "classNameBeforeSet"
            }
          },
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/classSignatureBeforeSet",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "classSignatureBeforeSet"
            }
          },
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/purityCheckResultList",
          "subField": [
            {
              "@type": "cr:Field",
              "@id": "default/purityCheckResultList/description",
              "dataType": "sc:Text",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "purityCheckResultList"
                },
                "transform": {
                  "jsonPath": "description"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/purityCheckResultList/isPure",
              "dataType": "sc:Boolean",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "purityCheckResultList"
                },
                "transform": {
                  "jsonPath": "isPure"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/purityCheckResultList/mappingState",
              "dataType": "cr:Int64",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "purityCheckResultList"
                },
                "transform": {
                  "jsonPath": "mappingState"
                }
              }
            },
            {
              "@type": "cr:Field",
              "@id": "default/purityCheckResultList/purityComment",
              "dataType": "sc:Text",
              "source": {
                "fileSet": {
                  "@id": "parquet-files-for-config-default"
                },
                "extract": {
                  "column": "purityCheckResultList"
                },
                "transform": {
                  "jsonPath": "purityComment"
                }
              }
            }
          ],
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/sourceCodeBeforeForWhole",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "sourceCodeBeforeForWhole"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/filePathAfter",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "filePathAfter"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/sourceCodeAfterForWhole",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "sourceCodeAfterForWhole"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/diffSourceCodeSet",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "diffSourceCodeSet"
            }
          },
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/invokedMethodSet",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "invokedMethodSet"
            }
          },
          "isArray": true,
          "arrayShape": "-1"
        },
        {
          "@type": "cr:Field",
          "@id": "default/sourceCodeAfterRefactoring",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "sourceCodeAfterRefactoring"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/diffSourceCode",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "diffSourceCode"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/uniqueId",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "uniqueId"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/moveFileExist",
          "dataType": "sc:Boolean",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "moveFileExist"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/compileResultBefore",
          "dataType": "sc:Boolean",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "compileResultBefore"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/compileResultCurrent",
          "dataType": "sc:Boolean",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "compileResultCurrent"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/compileJDK",
          "dataType": "cr:Float64",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "compileJDK"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/hasTestC",
          "dataType": "sc:Boolean",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "hasTestC"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/coverageInfo",
          "subField": [
            {
              "@type": "cr:Field",
              "@id": "default/coverageInfo/BRANCH",
              "subField": [
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/BRANCH/covered",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "BRANCH"
                      },
                      {
                        "jsonPath": "covered"
                      }
                    ]
                  }
                },
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/BRANCH/missed",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "BRANCH"
                      },
                      {
                        "jsonPath": "missed"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "@type": "cr:Field",
              "@id": "default/coverageInfo/COMPLEXITY",
              "subField": [
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/COMPLEXITY/covered",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "COMPLEXITY"
                      },
                      {
                        "jsonPath": "covered"
                      }
                    ]
                  }
                },
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/COMPLEXITY/missed",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "COMPLEXITY"
                      },
                      {
                        "jsonPath": "missed"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "@type": "cr:Field",
              "@id": "default/coverageInfo/INSTRUCTION",
              "subField": [
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/INSTRUCTION/covered",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "INSTRUCTION"
                      },
                      {
                        "jsonPath": "covered"
                      }
                    ]
                  }
                },
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/INSTRUCTION/missed",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "INSTRUCTION"
                      },
                      {
                        "jsonPath": "missed"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "@type": "cr:Field",
              "@id": "default/coverageInfo/LINE",
              "subField": [
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/LINE/covered",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "LINE"
                      },
                      {
                        "jsonPath": "covered"
                      }
                    ]
                  }
                },
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/LINE/missed",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "LINE"
                      },
                      {
                        "jsonPath": "missed"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "@type": "cr:Field",
              "@id": "default/coverageInfo/METHOD",
              "subField": [
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/METHOD/covered",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "METHOD"
                      },
                      {
                        "jsonPath": "covered"
                      }
                    ]
                  }
                },
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/METHOD/missed",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "METHOD"
                      },
                      {
                        "jsonPath": "missed"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "@type": "cr:Field",
              "@id": "default/coverageInfo/testMethod",
              "subField": [
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/testMethod/covered",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "testMethod"
                      },
                      {
                        "jsonPath": "covered"
                      }
                    ]
                  }
                },
                {
                  "@type": "cr:Field",
                  "@id": "default/coverageInfo/testMethod/missed",
                  "dataType": "cr:Int64",
                  "source": {
                    "fileSet": {
                      "@id": "parquet-files-for-config-default"
                    },
                    "extract": {
                      "column": "coverageInfo"
                    },
                    "transform": [
                      {
                        "jsonPath": "testMethod"
                      },
                      {
                        "jsonPath": "missed"
                      }
                    ]
                  }
                }
              ]
            }
          ]
        },
        {
          "@type": "cr:Field",
          "@id": "default/projectName",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "projectName"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/compileCommand",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "compileCommand"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/callInfo",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "callInfo"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "default/testResult",
          "dataType": "sc:Boolean",
          "source": {
            "fileSet": {
              "@id": "parquet-files-for-config-default"
            },
            "extract": {
              "column": "testResult"
            }
          }
        }
      ]
    }
  ],
  "conformsTo": "http://mlcommons.org/croissant/1.1",
  "name": "PureRefactor",
  "description": "easenxu/PureRefactor dataset hosted on Hugging Face and contributed by the HF Datasets community",
  "alternateName": [
    "easenxu/PureRefactor"
  ],
  "creator": {
    "@type": "Person",
    "name": "Yisen Xu",
    "url": "https://huggingface.co/easenxu"
  },
  "keywords": [
    "cc-by-4.0",
    "< 1K",
    "json",
    "Text",
    "Datasets",
    "pandas",
    "Croissant",
    "Polars",
    "\ud83c\uddfa\ud83c\uddf8 Region: US"
  ],
  "license": "https://choosealicense.com/licenses/cc-by-4.0/",
  "url": "https://huggingface.co/datasets/easenxu/PureRefactor"
}
```