import json
import base64


class Secret:
    def __init__(self, name, crt, key, namespace="default"):
        self._name = name
        self._data = {
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {"name": f"{name}-tls", "namespace": namespace},
            "data": {
                "tls.crt": self._encode_key(crt),
                "tls.key": self._encode_key(key),
            },
            "type": "kubernetes.io/tls",
        }

    @staticmethod
    def _encode_key(path):
        with open(path, "r") as file:
            data = file.read()

        s = data.encode("utf-8")
        s = base64.encodebytes(s).decode("utf-8").replace("\n", "")

        return s

    def to_json(self, **kwargs):
        return json.dumps(self._data, **kwargs)
