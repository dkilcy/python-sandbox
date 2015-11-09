#
# PUT Object Canned ACL into RS2
#
bucket=$1
file=$2
acl="x-amz-acl:public-read"

resource="/${bucket}/${file}"
dateValue=`date -uR`
stringToSign="PUT\n\n\n${dateValue}\n${acl}\n${resource}"
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${RS2_SECRET_KEY} -binary | base64`

curl -k -vv -X PUT \
  -H "Host: ${bucket}.${RS2_HOST}" \
  -H "x-amz-acl: public-read" \
  -H "Date: ${dateValue}" \
  -H "Authorization: AWS ${RS2_ACCESS_KEY}:${signature}" \
  http://${bucket}.{$RS2_HOST}/${file}

