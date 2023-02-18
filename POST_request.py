from grocery import *
import requests
import json


def post_card():
    resp = requests.post(CART_ENDPOINT)
    print(resp.text)
    print(resp.content)
    print(resp.json())
    print(resp.status_code)
    return resp.json()


card_json = post_card()
card = card_json["cartId"]
print(card)


def post_add_item_to_cart():
    payload = {"productId": "4643"}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post(CART_ITEMS_ENDPOINT.format(card), data=json.dumps(payload), headers=headers)
    print(resp.text)
    print(resp.content)
    print(resp.json())
    print(resp.status_code)
    return resp.json()


post_add_item_to_cart()
