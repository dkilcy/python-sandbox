#!/usr/bin/env bash
# Usage: s3-put <FILE> <S3_BUCKET> [<CONTENT_TYPE>]
#
# Uploads a file to the Amazon S3 service.
#
# Depends on AWS credentials being set via env:
# - RS2_ACCESS_KEY
# - RS2_SECRET_ACCESS
#
# Outputs the URL of the newly uploaded file.
set -e

authorization() {
  local signature="$(string_to_sign | hmac_sha1 | base64)"
  echo "AWS ${RS2_ACCESS_KEY?}:${signature}"
}

hmac_sha1() {
  openssl dgst -binary -sha1 -hmac "${RS2_SECRET_KEY?}"
}

base64() {
  openssl enc -base64
}

bin_md5() {
  openssl dgst -binary -md5
}

string_to_sign() {
  echo "$http_method"
  echo "$content_md5"
  echo "$content_type"
  echo "$date"
  echo "x-amz-acl:$acl"
  printf "/$bucket/$remote_path"
}

bucket="$1"
file="$2"
content_type="$3"

http_method=PUT
acl="public-read"
remote_path="${file##*/}"
content_md5="$(bin_md5 < "$file" | base64)"
date=`date -uR`

url="https://$bucket.${RS2_HOST}/$remote_path"

curl -k -v -T "$file" \
  -H "Authorization: $(authorization)" \
  -H "x-amz-acl: $acl" \
  -H "Date: $date" \
  -H "Content-MD5: $content_md5" \
  -H "Content-Type: $content_type" \
  "$url"

echo "$url"
