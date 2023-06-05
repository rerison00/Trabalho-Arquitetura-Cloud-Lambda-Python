# Trabalho-Arquitetura-Cloud-Lambda-Python

# Documentação da Função Lambda

Esta é uma documentação para a função Lambda que realiza uma requisição HTTP para obter dados de uma API.

## Função da Lambda

A função da Lambda é fazer uma requisição GET para a API "fnbr.co/api/shop" e retornar os dados recebidos da resposta como um objeto JSON.

## Entrada

Esta função não requer nenhum parâmetro de entrada. No entanto, é necessário fornecer a chave de API correta para autenticação. A chave de API deve ser fornecida no cabeçalho da requisição.

## Saída

A função retorna um objeto JSON contendo os dados recebidos da resposta da API. O formato dos dados depende da estrutura da resposta da API "fnbr.co/api/shop".

## Dependências Externas

Esta função depende dos seguintes módulos Python:

- `http.client`: Utilizado para fazer a requisição HTTP.
- `json`: Utilizado para manipular dados JSON.

## Instruções de Execução

Para executar esta função Lambda, siga as instruções abaixo:

1. Abra um ambiente de desenvolvimento que suporte a execução de funções Lambda em Python.

2. Crie uma nova função Lambda e copie o código fornecido para a função.

3. Certifique-se de que as dependências externas (`http.client` e `json`) estejam disponíveis no ambiente.

4. Fornecer a chave de API correta para a variável `x-api-key` no cabeçalho da requisição.

5. Configure o ambiente para invocar a função Lambda em resposta a um evento específico, se necessário.

6. Salve e publique a função Lambda.

## Teste da Função

Você pode testar a função Lambda seguindo as etapas abaixo:

1. Execute a função Lambda no ambiente de desenvolvimento.

2. Verifique se a função é executada corretamente e se os dados da resposta da API são retornados como um objeto JSON.

## Depuração

Para depurar a função Lambda, você pode utilizar as seguintes técnicas:

1. Adicione declarações de impressão (por exemplo, `print`) ao código para exibir informações e verificar se a função está passando pelos pontos esperados.

2. Verifique os logs da função Lambda para obter detalhes sobre erros ou problemas que possam ocorrer durante a execução.

3. Se possível, execute a função Lambda em um ambiente de desenvolvimento local para facilitar a depuração e o monitoramento.

## O Que esperar do retorno do json

1. O Json retorna a loja do jogo Fortnite, trazendo todos os itens que estao a venda no dia, um exemplo a baixo do retorno dele

"status": 200,
  "data": {
    "date": "2023-06-05T00:00:00.000Z",
    "featured": [
      {
        "id": "5c2aad8560e93a37d9635605",
        "name": "DJ Bop",
        "price": "2,000",
        "priceIcon": "vbucks",
        "priceIconLink": "https://image.fnbr.co/price/icon_vbucks.png",
        "images": {
          "icon": "https://image.fnbr.co/outfit/5c2aad8560e93a37d9635605/icon.png",
          "png": false,
          "gallery": "https://image.fnbr.co/outfit/5c2aad8560e93a37d9635605/gallery.png",
          "featured": "https://image.fnbr.co/outfit/5c2aad8560e93a37d9635605/featured.png",
          "resizeAvailable": true
        },
        "rarity": "legendary",
        "type": "outfit",
        "slug": "dj-bop",
        "readableType": "Outfit",
        "description": "Lose yourself in the beat.",
        "bundleSet": false,
        "bannerText": false,
        "history": {
          "occurrences": 60,
          "firstSeen": "2019-01-01T00:00:00.000Z",
          "lastSeen": "2023-06-05T00:00:00.000Z",
          "dates": [
            "2023-06-05T00:00:00.000Z",
            "2023-06-04T00:00:00.000Z",
            "2023-01-30T00:00:00.000Z",
            "2022-12-27T00:00:00.000Z",
            "2022-12-26T00:00:00.000Z",
            "2022-11-23T00:00:00.000Z",
            "2022-10-12T00:00:00.000Z",
            "2022-10-11T00:00:00.000Z",
            "2021-06-06T00:00:00.000Z",
            "2021-03-26T00:00:00.000Z",
            "2020-09-25T00:00:00.000Z",
            "2021-08-07T00:00:00.000Z",
            "2022-01-22T00:00:00.000Z",
            "2022-06-08T00:00:00.000Z",
            "2021-06-24T00:00:00.000Z",
            "2023-01-29T00:00:00.000Z",
            "2023-01-27T00:00:00.000Z",
            "2022-06-09T00:00:00.000Z",
            "2020-01-02T00:00:00.000Z",
            "2022-01-21T00:00:00.000Z",
            "2022-09-10T00:00:00.000Z",
            "2020-09-26T00:00:00.000Z",
            "2019-02-01T00:00:00.000Z",
            "2021-08-06T00:00:00.000Z",
            "2022-04-02T00:00:00.000Z",
            "2021-08-09T00:00:00.000Z",
            "2020-05-09T00:00:00.000Z",
            "2022-01-01T00:00:00.000Z",
            "2020-05-08T00:00:00.000Z",
            "2021-01-01T00:00:00.000Z",
            "2020-08-01T00:00:00.000Z",
            "2021-06-25T00:00:00.000Z",
            "2019-01-01T00:00:00.000Z",
            "2022-10-08T00:00:00.000Z",
            "2020-05-10T00:00:00.000Z",
            "2023-01-31T00:00:00.000Z",
            "2022-11-21T00:00:00.000Z",
            "2022-06-06T00:00:00.000Z",
            "2020-07-31T00:00:00.000Z",
            "2019-01-02T00:00:00.000Z",
            "2021-12-31T00:00:00.000Z",
            "2021-08-08T00:00:00.000Z",
            "2022-01-20T00:00:00.000Z",
            "2022-04-03T00:00:00.000Z",
            "2022-10-07T00:00:00.000Z",
            "2020-01-03T00:00:00.000Z",
            "2022-04-04T00:00:00.000Z",
            "2022-11-22T00:00:00.000Z",
            "2022-06-10T00:00:00.000Z",
            "2022-06-04T00:00:00.000Z",
            "2022-06-05T00:00:00.000Z",
            "2022-10-06T00:00:00.000Z",
            "2023-01-28T00:00:00.000Z",
            "2022-06-07T00:00:00.000Z",
            "2022-06-11T00:00:00.000Z",
            "2022-09-09T00:00:00.000Z",
            "2022-06-12T00:00:00.000Z",
            "2021-06-23T00:00:00.000Z",
            "2022-10-09T00:00:00.000Z",
            "2022-10-10T00:00:00.000Z"
          ]
        }
      },
      
      Ele traz o ID do item a venda, o preco dele, o nome, a raridade do item (Skin), e uma breve descricao do mesmo, traz as imagens do itens como tambem o simbolo da moeda do jogo, e traz tambem todas as datas que o item apareceu na loja do jogo.


## CODIGO ABAIXO

    import http.client
    import json

    def lambda_handler(event, context):
        conn = http.client.HTTPSConnection("fnbr.co")

    headers = {
        "x-api-key": "CODIGO E SECRETO!!!!!!!"
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
