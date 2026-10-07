import requests

# 1. Pega aquí el token que copiaste del cuadro azul de Postman (línea access_token)
TOKEN_BEARER = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJhMmU4ZGNkYy1jMWNkLTRkZTItYmE0Zi1lMjVkNjJkYjY3NmYiLCJqdGkiOiJlZjAwNThjMWJmNmRmMGIwOGU5NmYwZDhkOGYwYjNmNGY0NzVjMDI0Yjc1YTlmMTRhZDYyZDMzMmU1OGFjZjUxMGRlN2Y5YmQ3YThjNzJlYyIsImlhdCI6MTc5MTMwNzEwMS45MDA0OTUsIm5iZiI6MTc5MTMwNzEwMS45MDA0OTgsImV4cCI6MTc5MTMxMDcwMS44NzIwNjQsInN1YiI6IjQ3Iiwic2NvcGVzIjpbXX0.VolwnqGNsqO1dhDkg-hIzH3N4UQgY3pXQcs7d0_9Iik5ZvQRTA20pI01Zf84XNo5dMXDN9dVOjNErJ3zBcCu_oOdlu1yF7vhES8tNHtPwwtL55l4ChQkVBu-eUI4wXOPugKJm9bu8LzqavBEjJBpkKbTSQez4_I17PufhK-5JP2n__skXR-tky21MApwuUxxCEbBZv2uR2XiqdjB5mjwHrFGPAd05hiyXlbGa_lqvE5gwzSOajy0Nbn8mHM3_wV6Dj6HnlUabYl6hqIdcfohluCnK53_Pl4kqSfAcS2Xgaf3BOu3-W0UeliKKvnhr3k-uKB_fDhqsDP7FuE244kGBSLaqyCmXFnxJVMKS8mM1trC1jUwTjjxI3m9tnmbckQsWtpXeHte58GgJVRxAX2yrmKHbydXRUbM0nG-7ZhJ09okvmuat7D5nbB6xXVQr7FwLvO-463Z7twmvjOtxy1yfYIrErjJLarkzABPNSLoViTmwtCmrNFW736KWBh-78tuFcqpV-k9po6DbPRkvHPydbSwd9Yl6Q1dLhEzYcfwjzoWYflK0igo6UnsFhnNNQMxzicG8jIzPNt9r2mtJYsa4jcpai1BrETfmLNUAk8rC4a-y-0iB-QrQ7pO8gg4JIzVnn0tiTnYK5-DnsuCdKZU5TgavBAjtozH0E2rKxstJUs"

# Configuración de URL del Sandbox y Encabezados
URL_FACTUS = "https://api-sandbox.factus.com.co/v2/bills/validate"

headers = {
    "Authorization": f"Bearer {TOKEN_BEARER}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# 2. Estructura de la Factura (JSON validado)
factura_payload = {
    "numbering_range_id": 389,
    "reference_code": "FAC-003",
    "observation": "Factura emitida desde módulo Python",
    "customer": {
        "identification": "123456789",
        "dv": "3",
        "company": "",
        "trade_name": "",
        "names": "Mateo",
        "surnames": "Hernández",
        "email": "dilanzabala041@gmail.com",
        "phone": "3001234567",
        "legal_organization_id": "2",
        "tribute_id": "21",
        "identification_document_code": "13",
        "municipality_id": "980",
    },
    "payment_details": [
        {
            "payment_method_code": "10",
            "payment_form": "1",
            "amount": 59500,
        }
    ],
    "items": [
        {
            "code_reference": "ITEM-01",
            "name": "Servicio de Consultoría",
            "quantity": 1,
            "discount_rate": 0,
            "price": 50000,
            "unit_measure_code": "94",
            "standard_code": "1",
            "is_excluded": 0,
            "taxes": [{"code": "01", "rate": "19.00"}],
        }
    ],
}


# 3. Envío de la Petición
def enviar_factura():
  print("Enviando factura electrónica a Factus...")
  response = requests.post(URL_FACTUS, json=factura_payload, headers=headers)

  print(f"\nEstado HTTP: {response.status_code}")
  print("Respuesta API:")
  print(response.json())


if __name__ == "__main__":
  enviar_factura()