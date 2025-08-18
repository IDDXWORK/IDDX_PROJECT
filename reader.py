import pickle
import json

with open('iddx_annotations.json','rb') as f:
    data=json.load(f)
print(type(data))