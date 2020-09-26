
# AWS Lambda Python3.8 with OpenCV4 & NumPy

## Overview

Follow the instructions to have a Python AWS Lambda function with OpenCV and NumPy.

1. Setup your PC with the prerequisites
2. Deploy the Lambda function using Serverless Framework
3. Invoke the Lambda function and check that it is working
4. Clean-up

## Prerequisites

- [Docker Desktop](https://docs.docker.com/get-docker/)
    - Used for building OpenCV and the required Shared Object lib (.so) files
- [Serverless Framework CLI](https://www.serverless.com/framework/docs/getting-started/)
- AWS account with credentials configured locally (use AWS CLI, `aws configure`)

## Deploy

```sh
# Don't forget to start Docker Desktop
npm i
sls deploy
```

## Invoke

```sh
sls invoke --function hello --log
```

### Invoke output

```sh
mac:aws-lambda-sls-py-cv2-numpy user$ sls invoke --function hello --log
null
--------------------------------------------------------------------
START RequestId: 8f9265ed-49fe-4006-bdfc-721b94d0c5af Version: $LATEST
Start of function
OpenCV version: 4.4.0
NumPy version: 1.19.2
End of function
END RequestId: 8f9265ed-49fe-4006-bdfc-721b94d0c5af
REPORT RequestId: 8f9265ed-49fe-4006-bdfc-721b94d0c5af  Duration: 1.14 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 127 MB Init Duration: 1066.09 ms
```

## Clean-up

```sh
sls remove
```

## Credit

https://stackoverflow.com/a/61924452/10942272
