#!make
include .env
export $(shell sed 's/=.*//' .env)

init:
		pip3 install -r requirements.txt --user
		python3 -m pip install mypy pylint black --user

test:
		sh scripts/run_unittests.sh

lint:
		python3 -m pylint glue-python-scripts

format:
		python3 -m black glue-python-scripts

types:
		python3 -m mypy

full-test:
		make format
		make lint
		make types
		make test

run-events:
		python3 glue-python-scripts/jobEventClickstream.py --bucketName="datalake.acc.staging.guidion.io" --redshiftSecretName="redshift-credentials-accept"

run:
		python3 glue-python-scripts/jobEventClickstream.py --bucketName="datalake.acc.staging.guidion.io" --redshiftSecretName="redshift-credentials-accept"
		python3 glue-python-scripts/jobS3ToRedshift.py --bucketName="datalake.acc.staging.guidion.io" --redshiftSecretName="redshift-credentials-accept" --configBucketName="glue-etl.acc.guidion.io" --configFilePath="configuration-files/salesforceConfig.json" --redshiftRole="arn:aws:iam::813402095705:role/glue-service-role"
		python3 glue-python-scripts/jobSalesforceToS3.py --bucketName="datalake.acc.staging.guidion.io" --sfApiSecretName="sf-accept-api-user-creds" --sfEnvName="acc"

deploy-dev:
		sh scripts/deploy.sh
