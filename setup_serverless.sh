export PYTHONPATH=./src:./test
export AWS_DEFAULT_REGION=ap-southeast-2
serverless config credentials -p aws -k ${AWS_ACCESS_KEY_ID} -s ${AWS_SECRET_ACCESS_KEY}