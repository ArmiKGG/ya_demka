# -*- coding: utf-8 -*-
"""
Yandex Products API
"""
import gc
import pprint

from utils import *
from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
gc.enable()

app = Flask(__name__)
api = Api(app)


def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


class Health(Resource):
    """Health checking"""

    def get(self):
        return make_response(corsify_actual_response(jsonify({"status": "OK"})), 200)

    def post(self):
        return make_response(corsify_actual_response(jsonify({"status": "OK"})), 200)


class Items(Resource):
    """Api Items parser endpoint"""

    def options(self):
        return build_cors_preflight_response()

    def post(self):
        params = request.get_json()
        txt = params.get("query")
        if not txt:
            return make_response(
                corsify_actual_response(jsonify({"status": False, "message": "No query"})), 400)

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
        pprint.pprint(ya_product_values)
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
        pprint.pprint(ya_product_values)
        return make_response(corsify_actual_response(jsonify(ya_product_values)), 200)


api.add_resource(Health, "/api/", "/api/health")
api.add_resource(Items, "/api/items")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
