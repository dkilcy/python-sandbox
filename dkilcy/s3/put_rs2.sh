#
# PUT Object ACL into RS2
#
bucket=$1
file=$2

resource="/${bucket}/${file}"
contentType="application/text"
dateValue=`date -uR`
stringToSign="PUT\n\n${contentType}\n${dateValue}\n${resource}"
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${RS2_SECRET_KEY} -binary | base64`

curl -k -vv -X PUT -T "${file}" \
  -H "Host: ${bucket}.${RS2_HOST}" \
  -H "Date: ${dateValue}" \
  -H "Content-Type: ${contentType}" \
  -H "Authorization: AWS ${RS2_ACCESS_KEY}:${signature}" \
  http://${bucket}.{$RS2_HOST}/${file}

