# -*- coding: utf-8 -*-
"""
Yandex Products API
"""
import gc
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
        page = params.get("page")
        if not txt:
            return make_response(
                corsify_actual_response(jsonify({"status": False, "message": "No query"})), 400)

        all_items_with_category, all_skus, all_specs, \
        all_direct_suggestions, all_suggest_products = [], [], [], [], []
        for i in range(1, int(page) + 1):
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
        return make_response(corsify_actual_response(jsonify({"offers": all_items_with_category,
                                                              "skus": all_skus,
                                                              "specification": all_specs,
                                                              "suggestions": all_direct_suggestions,
                                                              "suggest_items": all_suggest_products})), 200)


api.add_resource(Health, "/api/", "/api/health")
api.add_resource(Items, "/api/items")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
