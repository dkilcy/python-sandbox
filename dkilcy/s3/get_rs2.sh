#
# GET Object from RS2
#
bucket=$1
file=$2
host=$3

resource="/${bucket}/${file}"
contentType="application/text"
dateValue=`date -uR`
stringToSign="GET\n\n${contentType}\n${dateValue}\n${resource}"
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${RS2_SECRET_KEY} -binary | base64`

curl -k -vv -X GET \
  -H "Host: ${bucket}.${host}" \
  -H "Date: ${dateValue}" \
  -H "Content-Type: ${contentType}" \
  -H "Authorization: AWS ${RS2_ACCESS_KEY}:${signature}" \
  http://${bucket}.${host}/${file}

