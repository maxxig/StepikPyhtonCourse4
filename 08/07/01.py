import json
class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
