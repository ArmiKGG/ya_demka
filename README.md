#Example request:

~~~
curl --location --request POST 'http://127.0.0.1:80/api/items' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "iphone xs max",
    "page": 3
}'
~~~

#Example response:
```json

{
    "offers": [
        {
            "category": "Мобильные телефоны",
            "current_price": 49990,
            "old_price": 0,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/6259061/pic5bf4f5d9efd380f411c459adeaa80ebc/orig",
            "title": "Смартфон CleverCel APPLE iPhone XS MAX 256Gb (подержанный c гарантией), золотистый",
            "url": "https://www.citilink.ru/product/smartfon-clevercel-iphone-xs-max-256gb-zolotistyi-3g-4g-6-5-ios-12-wif-1361023/?utm_medium=koldunshik_tovary&utm_source=yandex_organic"
        },
        {
            "category": "Мобильные телефоны",
            "current_price": 48990,
            "old_price": 54590,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/6513844/pic035ec1a2700188fd876411bb7177b444/orig",
            "title": "Смартфон CleverCel APPLE iPhone XS MAX 256Gb (подержанный c гарантией), серебристый",
            "url": "https://www.citilink.ru/product/smartfon-clevercel-apple-iphone-xs-max-256gb-poderzhannyi-c-garantiei-1389184/?utm_medium=koldunshik_tovary&utm_source=yandex_organic"
        },
        {
            "category": "Мобильные телефоны",
            "current_price": 52990,
            "old_price": 0,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/6799855/pica50bf8f170a3731be550d89e0df35f10/orig",
            "title": "Apple iPhone XS Max 256Gb Silver (Серебристый) Рос-Тест (RU)",
            "url": "https://i4you.ru/iphone_xs_max_256gb_silver_rst"
        },
        {
            "category": "Мобильные телефоны",
            "current_price": 42136,
            "old_price": 60863,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/6479949/pic4043a3a7437e3e88070e7c43840aad09/orig",
            "title": "Смартфон Apple iPhone XS Max 256 ГБ",
            "url": "https://www.ozon.ru/product/smartfon-apple-iphone-xs-max-256-gb-620484524/"
        },
        {
            "category": "Мобильные телефоны",
            "current_price": 52990,
            "old_price": 0,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/6340477/pic75f64681db9cd710098325ab7d98bcc3/orig",
            "title": "Apple iPhone XS Max 256Gb Space Gray (Серый космос) Рос-Тест (RU)",
            "url": "https://i4you.ru/iphone_xs_max_256gb_space_gray_rst"
        },
        {
            "category": "Мобильные телефоны",
            "current_price": 42136,
            "old_price": 60863,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/7081951/pic45a317fb6a2e7a9863ae55b1225959ca/orig",
            "title": "Смартфон Apple iPhone XS Max 256 ГБ",
            "url": "https://www.ozon.ru/context/detail/id/620496689/"
        },
        {
            "category": "Мобильные телефоны",
            "current_price": 52990,
            "old_price": 0,
            "picture": "https://avatars.mds.yandex.net/get-goods_pic/6201417/picf795eeca0d997c526e57e1f87e9706ed/orig",
            "title": "Apple iPhone XS Max 256Gb Gold (Золотой) Рос-Тест (RU)",
            "url": "https://i4you.ru/iphone_xs_max_256gb_gold_rst"
        }
    ],
    "skus": [
        {
            "max_price": 57990,
            "min_price": 48590,
            "picture": "https://avatars.mds.yandex.net/get-mpic/3631580/img_id6587612376638266781.jpeg/orig",
            "title": "Смартфон Apple iPhone Xs Max восстановленный 256 ГБ RU, серебристый"
        },
        {
            "max_price": 57990,
            "min_price": 49750,
            "picture": "https://avatars.mds.yandex.net/get-mpic/5234463/img_id4791071290158236663.png/orig",
            "title": "Смартфон Apple iPhone Xs Max восстановленный 256 ГБ RU, серый космос"
        },
        {
            "max_price": 63900,
            "min_price": 32390,
            "picture": "https://avatars.mds.yandex.net/get-mpic/5289692/img_id3407777377907527180.png/orig",
            "title": "Смартфон Apple iPhone Xs Max 256 ГБ, серый космос"
        },
        {
            "max_price": 87222,
            "min_price": 32390,
            "picture": "https://avatars.mds.yandex.net/get-mpic/5210379/img_id360328695888202565.jpeg/orig",
            "title": "Смартфон Apple iPhone Xs Max 256 ГБ, серебристый"
        },
        {
            "max_price": 81655,
            "min_price": 28290,
            "picture": "https://avatars.mds.yandex.net/get-mpic/5220903/img_id9216011076837104703.png/orig",
            "title": "Смартфон Apple iPhone Xs Max 256 ГБ, золотой"
        }
    ],
    "specification": [
        {
            "Слот для карты памяти": [
                "1",
                "0"
            ]
        },
        {
            "Разрешение фронтальной камеры": [
                "7 Мпикс"
            ]
        },
        {
            "Количество SIM-карт": [
                "1",
                "2"
            ]
        },
        {
            "Бренд": [
                "Apple"
            ]
        },
        {
            "Тип SIM-карты": [
                "eSIM",
                "nano SIM+eSIM"
            ]
        },
        {
            "Линейка": [
                "iPhone 13 Pro",
                "iPhone 14 Pro Max",
                "iPhone Xs"
            ]
        },
        {
            "Цвет": [
                "золотистый",
                "серебристый",
                "серый"
            ]
        },
        {
            "Диагональ экрана (точно)": [
                "6.7 \""
            ]
        },
        {
            "Разрешение экрана": [
                "2436×1125",
                "2532x1170",
                "2688x1242",
                "2778x1284",
                "2796x1290",
                "3840×2160 (4K)"
            ]
        },
        {
            "Степень защиты": [
                "IP68"
            ]
        },
        {
            "Емкость аккумулятора": [
                "2500-2999 мА⋅ч",
                "3000-3499 мА⋅ч"
            ]
        },
        {
            "Встроенная память ": [
                "64 ГБ",
                "256 ГБ",
                "512 ГБ"
            ]
        },
        {
            "Разрешение основной камеры": [
                "10-13 МП"
            ]
        },
        {
            "Количество основных камер": [
                "1",
                "2",
                "3",
                "4"
            ]
        },
        {
            "Диагональ экрана": [
                "5.5\"-5.9\"",
                "6.5\" и больше"
            ]
        },
        {
            "Частота обновления экрана": [
                "60 Гц",
                "120 Гц"
            ]
        },
        {
            "Оперативная память": [
                "4 ГБ"
            ]
        },
        {
            "Беспроводные интерфейсы": [
                "Bluetooth",
                "NFC",
                "Wi-Fi"
            ]
        },
        {
            "Стандарт связи": [
                "3G",
                "4G LTE"
            ]
        },
        {
            "Формат разрешения экрана": [
                "Full HD"
            ]
        },
        {
            "Операционная система": [
                "iOS"
            ]
        },
        {
            "Процессор": [
                "Apple A12 Bionic",
                "Apple A15 Bionic",
                "Apple A16 Bionic"
            ]
        }
    ],
    "suggest_items": [
        {
            "img": "https://avatars.mds.yandex.net/get-mpic/3631580/img_id6587612376638266781.jpeg/orig",
            "price": "От 47 290 ₽",
            "title": "Смартфон Apple iPhone Xs Max восстановленный",
            "url": "https://yandex.ru/products/product/651767003?sku=100865012729&suggest=1&suggest_text=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+Apple+iPhone+Xs+Max+%D0%B2%D0%BE%D1%81%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9&suggest_type=model"
        },
        {
            "img": "https://avatars.mds.yandex.net/get-mpic/5210379/img_id360328695888202565.jpeg/orig",
            "price": "От 57 890 ₽",
            "title": "Смартфон Apple iPhone Xs Max",
            "url": "https://yandex.ru/products/product/175939244?sku=101491834734&suggest=1&suggest_text=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+Apple+iPhone+Xs+Max&suggest_type=model"
        },
        {
            "img": "https://avatars.mds.yandex.net/get-mpic/1865974/img_id9196790216848506343.jpeg/orig",
            "price": "От 39 897 ₽",
            "title": "Смартфон Apple iPhone Xs восстановленный",
            "url": "https://yandex.ru/products/product/651752076?sku=100864951791&suggest=1&suggest_text=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+Apple+iPhone+Xs+%D0%B2%D0%BE%D1%81%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9&suggest_type=model"
        },
        {
            "img": "https://avatars.mds.yandex.net/get-mpic/5234357/img_id3872107053272005053.jpeg/orig",
            "price": "От 39 890 ₽",
            "title": "Смартфон Apple iPhone Xs",
            "url": "https://yandex.ru/products/product/175944272?sku=101534032743&suggest=1&suggest_text=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+Apple+iPhone+Xs&suggest_type=model"
        },
        {
            "img": "https://avatars.mds.yandex.net/get-mpic/5235448/img_id4222516894328537616.jpeg/orig",
            "price": "От 81 590 ₽",
            "title": "Смартфон Apple iPhone 13 Pro Max",
            "url": "https://yandex.ru/products/product/1414858424?sku=101648804085&suggest=1&suggest_text=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+Apple+iPhone+13+Pro+Max&suggest_type=model"
        }
    ],
    "suggestions": [
        "iphone xs max",
        "iphone xs max 256",
        "iphone xs max 64",
        "iphone xs max 512",
        "iphone xs max 256gb"
    ]
}

```