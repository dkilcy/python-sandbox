#
# PUT Object ACL from RS2
#
bucket=$1
file=$2

resource="/${bucket}/${file}?acl"
dateValue=`date -uR`
stringToSign="PUT\n\n\n${dateValue}\n${resource}"
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${RS2_SECRET_KEY} -binary | base64`

curl -k -vv -T ./test.acl \
  -H "Host: ${bucket}.${RS2_HOST}" \
  -H "Date: ${dateValue}" \
  -H "Content-Type: ${contentType}" \
  -H "Authorization: AWS ${RS2_ACCESS_KEY}:${signature}" \
  http://${bucket}.${RS2_HOST}/${file}?acl

