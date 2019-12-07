import json
import base64


class Secret:
    def __init__(self, name, crt, key, namespace="default"):
        self._name = name
        self._data = {
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {
                "name": f"{name}-ingress",
                "namespace": namespace
            },
            "data": {
                "tls.crt": self._encode_key(crt),
                "tls.key": self._encode_key(key)
            },
            "type": "kubernetes.io/tls"
        }

    @staticmethod
    def _encode_key(path):
        with open(path, "rb") as file:
            data = file.read()

        return base64.encodebytes(data).decode("utf-8")

    def to_json(self, **kwargs):
        return json.dumps(self._data, **kwargs)