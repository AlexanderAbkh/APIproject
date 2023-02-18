import os




BASE_API = "https://simple-grocery-store-api.glitch.me"
# *************** GET ****************
STATUS_ENDPOINT = os.path.join(str(BASE_API) + "/status")
PRODUCTS_ENDPOINT = os.path.join(str(BASE_API) + "/products")
# **** with query param
PRODUCTS_ENDPOINT_PATH_PARAM_PRODUCT_ID = os.path.join(str(PRODUCTS_ENDPOINT) + "/{}")
# ************ POST *******************
CART_ENDPOINT = os.path.join(str(BASE_API) + "/carts")
# with path param
CART_ITEMS_ENDPOINT = os.path.join(str(BASE_API) + "/carts/{}/items")