from grocery import *
import requests

def get_status():
    resp = requests.get(STATUS_ENDPOINT)
    print(resp.text)
    print(resp.content)
    print(resp.json())
    print(resp.status_code)

#get_status()

def get_products():
    resp = requests.get(PRODUCTS_ENDPOINT)
    print(resp.text)
    print(resp.content)
    print(resp.json())
    print(resp.status_code)

#get_products()



def get_product_by_category():
    payload = {'results': 2, 'category': 'coffee', "available": "true"}
    resp = requests.get(PRODUCTS_ENDPOINT, params=payload)
    print(resp.text)
    print(resp.content)
    print(resp.json())
    print(resp.status_code)

#get_product_by_category()

def get_product_by_productId():
    resp = requests.get(PRODUCTS_ENDPOINT_PATH_PARAM_PRODUCT_ID.format("8554"))
    print(resp)
    print(resp.text)
    print(resp.content)
    print(resp.json())
    print(resp.status_code)
#get_product_by_productId()

