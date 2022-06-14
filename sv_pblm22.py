import json

jsonFile = open('test_payload.json')
data = json.load(jsonFile)

def del_ele(json_ele, key):
    if key in json_ele:
        del json_ele[key]
    else:
        for k, v in json_ele.items():
            if isinstance(v, dict) and key in v.keys():
                del json_ele[k][key]
                return json_ele
        return "key doesnt exists in given json object"
    return json_ele

print(del_ele(data, 'appdate'))