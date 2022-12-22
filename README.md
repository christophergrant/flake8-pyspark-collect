Beware: these are liars right now, they are TODOs:
[![Build Status](https://dev.azure.com/chrisgrant0527/flake8/_apis/build/status/christophergrant.flake8-pyspark-collect?repoName=christophergrant%2Fflake8-pyspark-collect&branchName=main)](https://dev.azure.com/chrisgrant0527/flake8/_build/latest?definitionId=1&repoName=christophergrant%2Fflake8-pyspark-collect&branchName=main)[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/69/main.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=69&branchName=main)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/flake8-match/main.svg)](https://results.pre-commit.ci/latest/github/asottile/flake8-match/main)

## disclaimer

this code, although tested, is not battle hardened just yet

flake8-pyspark-collect
============

flake8 plugin which forbids [DataFrame.collect()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.collect.html)

## installation

```bash
pip install flake8-pyspark-collect
```

## flake8 codes

| Code   | Description          |
|--------|----------------------|
| PS001 | do not use collect()  |

## rationale

The usage of [DataFrame.collect()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.collect.html) is a common anti-pattern in Apache Spark. [Apache Spark](https://spark.apache.org/) is a **parallel** processing engine that helps distribute computations over an army of resources. When you use `collect()`, you put all of the data onto a single node, which is the opposite of parallel. Also, bad usage of `collect()` can lead to cluster instability and bad user experience. There are some legitimate purposes of using `collect()` but a large amount of its usage is not warranted and does not help the user. For these reasons, this plugin was built to issue alerts when `DataFrame.collect()` is being used.

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 3.8.4
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-pyspark-collect==1.0.0]
```

## an inside look

Admittedly, I did not write a majority of this code. I credit the creation of this plugin to the work of @asottile, specifically [this repo](https://github.com/asottile/flake8-match), and also to OpenAI's ChatGPT to write [this portion](https://github.com/christophergrant/flake8-pyspark-collect/blob/main/flake8_collect.py#L16) of the plugin. 

For the ChatGPT portion, I used this series of prompts: `write a python program that parses the AST of a pyspark program, intercepting any collect() method calls`. The code was not correct, so I directed ChatGPT to issue a correction: `collect is a method, not a function. correct this code to intercept collect() method calls`. I then put these parts together and added some basic tests to make sure that things worked. 

That being said, I'm sure the code can be improved futher.
