[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.flake8-match?branchName=main)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=69&branchName=main)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/69/main.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=69&branchName=main)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/flake8-match/main.svg)](https://results.pre-commit.ci/latest/github/asottile/flake8-match/main)

flake8-pyspark-collect
============

flake8 plugin which forbids DataFrame.collect()

## installation

```bash
pip install flake8-pyspark-collect
```

## flake8 codes

| Code   | Description          |
|--------|----------------------|
| PS0001 | do not use collect() |

## rationale

lol

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
