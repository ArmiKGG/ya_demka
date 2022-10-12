import requests
from configs import *

url = "https://yandex.ru/products/api/rr/search?order=dpop&page=1&text={}&with_rich_media_gallery=0"


def get_specs_price_min_max(object_resp):
    filters = object_resp["search"]["filters"]
    specs_f = []
    if filters.get("glprice"):
        del filters["glprice"]
    for j in filters.values():
        if not j.get("max"):
            vals = j.get("values", [])
            spec = {j.get("title", ""): ", ".join([ii.get("value", "") for ii in vals])}
        else:
            spec = {j.get("title", ""): ", ".join([str(j.get('max')) + " " + j.get('unit', '')])}

        specs_f.append(spec)

    return specs_f


def get_category(object_resp):
    if object_resp.get("entities") \
            and object_resp["entities"].get("categories") \
            and object_resp.get("entities").get("categories"):
        cat = list(object_resp["entities"]["categories"].values())[0]
        return cat.get("name")
    return ""


def get_offers(object_resp):
    if object_resp.get("entities") and object_resp["entities"].get("offers"):
        offers = object_resp["entities"].get("offers")
        oftop = []
        for ofer in offers.values():
            current_price = int(ofer["price"].get("current", 0)) if ofer.get("price") and ofer["price"].get(
                "current") else 0
            old_price = int(ofer["price"].get("old", 0)) if ofer.get("price") and ofer["price"].get("old") else 0
            oftop.append({"title": ofer.get("title", ""),
                          "url": ofer["urls"].get("direct", "") if ofer.get("urls") else "",
                          "picture": "https:" + ofer["pictures"][0] if ofer.get("pictures") else "",
                          "current_price": current_price,
                          "old_price": old_price
                          })
        return oftop
    return []


def get_items_skus(object_resp):
    if object_resp.get("entities") and object_resp["entities"].get("skus"):
        skus = object_resp["entities"]["skus"]
        oftop = []
        for ofer in skus.values():
            oftop.append({"title": ofer.get("title", ""),
                          "picture": "https:" + ofer["pictures"][0] if ofer.get("pictures") else "",
                          "min_price": int(ofer["price"].get("min", 0)) if ofer.get("price") else 0,
                          "max_price": int(ofer["price"].get("max", 0)) if ofer.get("price") else 0
                          })
        return oftop
    return []


def fix_category(category, objects_all):
    if category:
        for d in objects_all:
            d["category"] = category
    return objects_all


def suggestion(suggest):
    direct_suggestions = []
    suggest_products = []
    for sug in suggest:
        if len(sug) > 2:
            if sug[0] == "fulltext":
                direct_suggestions.append(sug[1])
            if sug[0] == "nav" and "product" in sug[3] and type(sug[-1]) == dict:
                prod = {"title": sug[1],
                        "url": "https://yandex.ru/products" + sug[3],
                        "price": sug[-1]["price"],
                        "picture": "https:" + sug[-1]["img"].get("url") if sug[-1].get("img") else ""}
                suggest_products.append(prod)
    return direct_suggestions, suggest_products


def requesting_ya_products(txt: str, calc_suggestions=True):
    rpp = requests.get(url.format(txt), headers=headers, cookies=cookie).json()
    specs = get_specs_price_min_max(rpp)
    items_with_category = fix_category(get_category(rpp), get_offers(rpp))
    skus = get_items_skus(rpp)

    payload = {"specification": specs,
               "offers": items_with_category,
               "skus": skus}

    if calc_suggestions:
        suggestions = requests.get(f"https://yandex.ru/suggest-market/suggest-market-new?srv=goods&platform=desktop"
                                   f"&format=v2&svg=0&part={txt}&pos=0", headers=headers, cookies=cookie).json()
        direct_suggestions, suggest_products = suggestion(suggestions)
        payload["suggestions"] = direct_suggestions
        payload["suggest_items"] = suggest_products
    return payload
