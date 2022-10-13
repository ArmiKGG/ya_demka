from flask import Flask, render_template, request
from utils import requesting_ya_products
#import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/data")
def data():
    txt = request.args.get("query")
    max_page = request.args.get("page")
    all_items_with_category, all_skus, all_specs, \
    all_direct_suggestions, all_suggest_products = [], [], [], [], []
    for i in range(1, int(max_page) + 1):
        if i != 1:
            items_with_category, skus, specs, \
            direct_suggestions, suggest_products = requesting_ya_products(i, txt, False)
            all_items_with_category += items_with_category
            all_skus += skus
            all_specs += specs
            all_direct_suggestions += direct_suggestions
            all_suggest_products += suggest_products
        else:
            items_with_category, skus, specs, \
            direct_suggestions, suggest_products = requesting_ya_products(i, txt)
            all_items_with_category += items_with_category
            all_skus += skus
            all_specs += specs
            all_direct_suggestions += direct_suggestions
            all_suggest_products += suggest_products
        if all_direct_suggestions:
            for sub in all_direct_suggestions:
                items_with_category, skus, specs, \
                direct_suggestions, suggest_products = requesting_ya_products(i, sub)
                all_items_with_category += items_with_category
                all_skus += skus
                all_specs += specs
                all_suggest_products += suggest_products

        all_skus = [dict(t) for t in {tuple(d.items()) for d in all_skus}]
        all_items_with_category = [dict(t) for t in {tuple(d.items()) for d in all_items_with_category}]
        all_specs = [dict(t) for t in {tuple(d.items()) for d in all_specs}]
        all_suggest_products = [dict(t) for t in {tuple(d.items()) for d in all_suggest_products}]

    return render_template("test.html",
                           skus=all_skus,
                           offers=all_items_with_category,
                           specification=all_specs,
                           suggestions=all_direct_suggestions,
                           suggest_items=all_suggest_products
                           )


app.run(host="0.0.0.0", port=8080)
