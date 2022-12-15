#!/bin/bash
. .env
echo $S3_BUCKETNAME
mkdir -p _aws/$S3_BUCKETNAME/cartel/
cp -r backend/dummy/image/ _aws/$S3_BUCKETNAME/cartel/