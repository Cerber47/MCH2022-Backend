import json
from bson import objectid


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(self, o):
            return str(o)
        return json.JSONEncoder.default(self, o)