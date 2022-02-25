from jsonschema import validate
import json

# ------------------------------
# first schema
# ------------------------------

# schema = {
#     "type" : "object",
#     "properties" : {
#         "price" : {"type" : "number"},
#         "name"  : {"type" : "string"},
#     }
# }

# ok with schema
# validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

# not ok with schema
# validate(instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema)


# ------------------------------
# second schema
# ------------------------------

# schema = {
#     "type" : "object",
#     "required": ["name"]
# }

# ok with schema
# validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

# not ok with schema
# validate(instance={"price" : 34.99}, schema=schema)

# ------------------------------
# third schema
# ------------------------------

schema = {
    "type": "object",
    "properties": {
        "customer": {
            "type": "object",
            "required": ["lastName", "firstName", "age"]}},
    "required": ["service", "customer"]
}

json_document = '''{
    "service" : "Some Service Name",
    "customer" : {
        "lastName" : "Kim",
        "firstName" : "Bingbong",
        "age" : "99"
    }
}'''

# Read in the JSON document
data = json.loads(json_document)

# validate the result
validate(data, schema)

# more on jsonschema
# https://github.com/Julian/jsonschema
# https://json-schema.org/