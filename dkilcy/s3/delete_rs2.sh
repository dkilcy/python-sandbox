#
# DELETE Object from RS2
#
bucket=$1
file=$2
host=$3

resource="/${bucket}/${file}"
dateValue=`date -uR`
stringToSign="DELETE\n\n\n${dateValue}\n${resource}"
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${RS2_SECRET_KEY} -binary | base64`

curl -k -vv -X DELETE \
  -H "Host: ${bucket}.${host}" \
  -H "Date: ${dateValue}" \
  -H "Authorization: AWS ${RS2_ACCESS_KEY}:${signature}" \
  http://${bucket}.${host}/${file}

