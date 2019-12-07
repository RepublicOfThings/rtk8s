from rtk8s.objects import Secret, Ingress

secret = Secret("smeiling", "keys/cert.pem", "keys/key.pem")
ingress = Ingress("smeiling")

print(ingress.to_json(indent=4))
print(secret.to_json(indent=4))
