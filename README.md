# Talent Engine II training

## How to run tests

Run `pytest` from repo folder.

## Framework structure

talent-engine-II
├───config_sources
│       ├───config.json
|
├───src
│   ├───config
|   |   ├───config.py
|   |
│   ├───data
│   ├───models
|   |   ├───usermodel.py
|   |
│   ├───providers
|       ├───baseprovider.py
|       ├───jsonconfigprovider.py
|       ├───osconfigprovider.py
|       ├───providerconstants.py
|
├───TESTS
|       ├───test_basictypes.py
|
.gitignore
conftest.py
README.md
requirements.txt
