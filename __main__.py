import requests as req
from datetime import datetime
from decouple import config


# PROPERTIES
PIXELA_USERNAME = config("PIXELA_USERNAME")
PIXELA_TOKEN = config("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_HEADERS = {"X-USER-TOKEN": PIXELA_TOKEN}

# PIXELA_GRAPH_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today}"
# PIXELA_GRAPH_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today}"
# pixela_params = {"username": PIXELA_USERNAME, "token": PIXELA_TOKEN, "agreeTermsOfService": "yes", "notMinor": "yes"}
# pixela_graph_config = {"id": PIXELA_GRAPH_ID, "name": "Cycling Graph", "unit": "Km", "type": "float", "color": "ajisai"}


# DATA
def post_graph_data(graph_id, date, quantity):
    pixela_graph_post_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}"
    pixela_pixel_data = {"date": date, "quantity": quantity}
    res = req.post(url=pixela_graph_post_endpoint, json=pixela_pixel_data, headers=PIXELA_HEADERS)
    print(res.text)


# MAIN
today = datetime.now().strftime("%Y%m%d")
post_graph_data("graph-1", today, "7")
