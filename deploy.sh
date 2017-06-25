#!/bin/bash

npm run production

# S3を使う場合
# pip install awscli
# aws configure set region ap-northeast-1
# aws s3 sync dist/ s3://www.yours3bucket.com/ --delete

# Github Pages の場合

cp -r dist /tmp
git checkout gh-pages
rm -rf *
cp -r /tmp/dist/* .
git add .
git commit 'release'
git push origin gh-pages
git checkout master
