# Serverless Framework Upload Dependency to Lambda

Template for uploading single dependency as a Lambda Layer

## Prerequisites

Using the Serverless Framework CLI, create a local directory for this template

The serverless-python-requirements plugin is required to bundle third-party dependencies
```bash
serverless plugin install -n serverless-python-requirements
```

## Instructions

Edit the requirements.txt file to include a single dependency

```bash
pandas
```

Edit the ```serverless.yml``` accordingly

## Deployment 
```bash
sls deploy
```
