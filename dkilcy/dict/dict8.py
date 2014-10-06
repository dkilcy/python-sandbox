import json

template = {
        "Parameters": {
            "Foo": {
                "Type": "CommaDelimitedList"
            }
        }
}

t = json.loads( json.dumps(template) )

print t
print type(t)
print t['Parameters'] 