import json

import requests
from flask import Flask, render_template, request
from utils import requesting_ya_products
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/data")
def data():
    txt = request.args.get("query")

    ya_product_values = requesting_ya_products(txt)
    specs = ya_product_values["specification"]
    suggestions = ya_product_values["suggestions"]
    suggested_items = ya_product_values["suggest_items"]
    if not ya_product_values["offers"] and ya_product_values["suggestions"]:
        for sug_query in ya_product_values["suggestions"]:
            ya_product_values = requesting_ya_products(sug_query, False)
            specs += ya_product_values["specification"]
            if ya_product_values["offers"]:
                break
    if not ya_product_values["offers"] and ya_product_values["skus"]:
        for sku in ya_product_values["skus"]:
            new_query = sku.get("title")
            if new_query:
                ya_product_values = requesting_ya_products(new_query)
                specs += ya_product_values["specification"]
                suggestions += ya_product_values["suggestions"]
                suggested_items += ya_product_values["suggest_items"]
            if ya_product_values["offers"]:
                break
    ya_product_values["specification"] = specs
    ya_product_values["suggestions"] = suggestions
    ya_product_values["suggest_items"] = suggested_items
    ya = ya_product_values
    return render_template("test.html",
                           skus=ya["skus"],
                           offers=ya["offers"],
                           specification=ya["specification"],
                           suggestions=ya.get("suggestions", []),
                           suggest_items=ya.get("suggest_items", []))


app.run(host="0.0.0.0", port=8080)