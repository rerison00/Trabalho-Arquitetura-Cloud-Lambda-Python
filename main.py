import http.client
import json


def lambda_handler(event, context):
    conn = http.client.HTTPSConnection("fnbr.co")

    headers = {
        "x-api-key": "1c8636d8-0a6c-40e3-a711-802b90074b3c"
    }
    conn.request("GET", "/api/shop", headers=headers)

    response = conn.getresponse()

    data = response.read().decode()

    conn.close()

    json_data = json.loads(data)

    # if response.status == 200:
    #     loja = json_data['data']['featured']
    #     for item in loja:
    #         print(item['name'])

    #     quantidade_itens = len(loja)
    #     print("Quantidade de itens na loja: ",quantidade_itens)

    return json_data