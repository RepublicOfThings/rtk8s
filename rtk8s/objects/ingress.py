import json


class Ingress:
    def __init__(self, name, namespace="default", paths=None, host="localhost"):
        paths = paths or []
        self._name = name
        self._data = {
            "apiVersion": "extensions/v1beta1",
            "kind": "Ingress",
            "metadata": {
                "name": f"{name}-ingress",
                "namespace": namespace,
                "annotations": {
                    "nginx.ingress.kubernetes.io/use-regex": "true",
                    "nginx.ingress.kubernetes.io/ssl-redirect": "true",
                },
            },
            "spec": {
                "tls": [{"secretName": "smeiling-tls", "hosts": [host]}],
                "rules": [
                    {"host": host, "http": {"paths": [*self._build_rules(paths)]}}
                ],
            },
        }

    @staticmethod
    def _build_rules(paths):
        return [
            {
                "path": "/" + path + "/*",
                "backend": {"serviceName": path, "servicePort": path.replace("-", "")},
            }
            for path in paths
        ]

    def to_json(self, **kwargs):
        return json.dumps(self._data, **kwargs)
