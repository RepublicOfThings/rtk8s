import json


class Ingress:
    def __init__(self, name, namespace="default", paths=None):
        paths = paths or []
        self._name = name
        self._data = {
            "apiVersion": "extensions/v1beta1",
            "kind": "Ingress",
            "metadata": {
                "name": f"{name}-ingress",
                "namespace": namespace
            },
            "spec": {
                "tls": [
                    {
                        "secretName": "smeiling-tls"
                    }
                ],
                "rules": [
                    *self._build_rules(paths)
                ]
            }
        }

    @staticmethod
    def _build_rules(paths):
        return [
            {"path": "/"+path,
            "backend": {
                "serviceName": path,
                "servicePort": path+"-tcp"
            }} for path in paths
        ]

    def to_json(self, **kwargs):
        return json.dumps(self._data, **kwargs)