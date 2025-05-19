import random
import json
from datetime import datetime, timedelta

products:str = ["Red", "Green", "Blue"]
locations:str = ["Northwest", "Southwest", "Central", "Northeast", "Southeast"]
TOTAL_PRODUCTS:int = 100
FILE_NAME:str = "bicycle_data.json"

today = datetime.today()
start_date = today - timedelta(days=365)

data_list: list = []
row: dict = {}
for count in range(TOTAL_PRODUCTS):
    rand_days = random.randint(0, 364)
    date = (start_date + timedelta(days=rand_days)).strftime("%Y-%m-%d")
    product = random.choice(products)
    price = round(random.uniform(200.00, 1000.00), 2)
    location = random.choice(locations)
    row = {
        "id": count,
        "date": date,
        "product": product,
        "price": price,
        "location": location
    }
    data_list.append(row)

file = open(FILE_NAME, "w")
json.dump(data_list,file)
file.close()
# Create a flask application with a route to serve up data from a local file named product_data.json