#
# Create RS2 User
#
user=$1
host=$2

resource="/users/${user}?dname=${user}"
dateValue=`date -uR`
stringToSign="PUT\n\n\n${dateValue}\n${resource}"
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${RS2_ADMIN_SECRET_KEY} -binary | base64`

curl -k -vv -X PUT -T "${file}" \
  -H "Date: ${dateValue}" \
  -H "Authorization: AWS ${RS2_ADMIN_ACCESS_KEY}:${signature}" \
  http://{$host}${resource}

