from utils import *

txt = "Телефон смартфон с 3 камерами и ios на борту"
rpp = requests.get(url.format(txt), headers=headers, cookies=cookie).json()

print(rpp)

suggestions = requests.get(f"https://yandex.ru/suggest-market/suggest-market-new?srv=goods&platform=desktop"
                                   f"&format=v2&svg=0&part={txt}&pos=0", headers=headers, cookies=cookie).json()

