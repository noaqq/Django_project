import json

import requests


def get_data():

    cookies = {
        "HINTS_FIO_COOKIE_NAME": "2",
        "MVID_AB_SERVICES_DESCRIPTION": "var4",
        "MVID_ADDRESS_COMMENT_AB_TEST": "2",
        "MVID_BLACK_FRIDAY_ENABLED": "true",
        "MVID_CALC_BONUS_RUBLES_PROFIT": "false",
        "MVID_CART_AVAILABILITY": "true",
        "MVID_CART_MULTI_DELETE": "false",
        "MVID_CATALOG_STATE": "1",
        "MVID_CITY_ID": "CityCZ_975",
        "MVID_CREDIT_AVAILABILITY": "true",
        "MVID_FILTER_CODES": "true",
        "MVID_FILTER_TOOLTIP": "1",
        "MVID_FLOCKTORY_ON": "true",
        "MVID_GET_LOCATION_BY_DADATA": "DaData",
        "MVID_GIFT_KIT": "true",
        "MVID_GUEST_ID": "21483091190",
        "MVID_HANDOVER_SUMMARY": "true",
        "MVID_IS_NEW_BR_WIDGET": "true",
        "MVID_KLADR_ID": "7700000000000",
        "MVID_LAYOUT_TYPE": "1",
        "MVID_LP_SOLD_VARIANTS": "3",
        "MVID_MCLICK": "true",
        "MVID_MINI_PDP": "true",
        "MVID_MOBILE_FILTERS": "true",
        "MVID_NEW_ACCESSORY": "true",
        "MVID_NEW_DESKTOP_FILTERS": "true",
        "MVID_NEW_LK_CHECK_CAPTCHA": "true",
        "MVID_NEW_LK_OTP_TIMER": "true",
        "MVID_NEW_MBONUS_BLOCK": "true",
        "MVID_PROMO_CATALOG_ON": "true",
        "MVID_REGION_ID": "1",
        "MVID_REGION_SHOP": "S002",
        "MVID_SERVICES": "111",
        "MVID_SERVICES_MINI_BLOCK": "var2",
        "MVID_TAXI_DELIVERY_INTERVALS_VIEW": "new",
        "MVID_TIMEZONE_OFFSET": "3",
        "MVID_WEBP_ENABLED": "true",
        "NEED_REQUIRE_APPLY_DISCOUNT": "true",
        "PICKUP_SEAMLESS_AB_TEST": "2",
        "PRESELECT_COURIER_DELIVERY_FOR_KBT": "true",
        "PROMOLISTING_WITHOUT_STOCK_AB_TEST": "2",
        "SENTRY_ERRORS_RATE": "0.1",
        "SENTRY_TRANSACTIONS_RATE": "0.5",
        "searchType2": "3",
        "wurfl_device_id": "generic_web_browser",
        "MVID_NEW_OLD": "eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9",
        "MVID_OLD_NEW": "eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==",
        "deviceType": "desktop",
        "_ym_uid": "1663583556254664400",
        "_ym_d": "1663583556",
        "afUserId": "13111e44-ca19-455a-9367-f8cd3e809735-p",
        "flocktory-uuid": "0968b95b-72c3-4fc3-95bb-bf6f496d95ad-7",
        "uxs_uid": "612be7e0-3806-11ed-82a6-5755a00505ae",
        "MVID_CRITICAL_GTM_INIT_DELAY": "3000",
        "MVID_MINDBOX_DYNAMICALLY": "true",
        "__SourceTracker": "google__organic",
        "admitad_deduplication_cookie": "google__organic",
        "MVID_AB_PDP_CHAR": "2",
        "MVID_GLP": "true",
        "MVID_MULTIOFFER": "true",
        "MVID_GEOLOCATION_NEEDED": "false",
        "__ttl__widget__ui": "1666631611106-a22682d0bff9",
        "__lhash_": "3d9cc0efe976beb0639d145cc3cd77ef",
        "JSESSIONID": "1tWjjCLSMq2bGSvMtgJkR7Ph646gN3mvJGSCQs74fLvpww2vwpTL!-955907452",
        "COMPARISON_INDICATOR": "false",
        "flacktory": "no",
        "BIGipServeratg-ps-prod_tcp80": "2969885706.20480.0000",
        "bIPs": "-971835924",
        "MVID_GTM_BROWSER_THEME": "1",
        "SMSError": "",
        "authError": "",
        "_gid": "GA1.2.997635636.1669483317",
        "_sp_ses.d61c": "*",
        "_ym_isad": "1",
        "advcake_track_id": "96b4f8fc-e1e9-06ee-fc3b-3cbeca4ede20",
        "advcake_session_id": "179dc93f-d768-9eb0-9bf4-9f804a1d049a",
        "AF_SYNC": "1669483317581",
        "BIGipServeratg-ps-prod_tcp80_clone": "2969885706.20480.0000",
        "MVID_AB_TOP_SERVICES": "2",
        "MVID_GLC": "true",
        "MVID_GTM_ENABLED": "011",
        "MVID_IMG_RESIZE": "true",
        "MVID_LP_HANDOVER": "0",
        "tmr_lvid": "9e31cad33a605f7702d119a87d5b6f39",
        "tmr_lvidTS": "1663583555766",
        "fgsscgib-w-mvideo": "TIYA73835571ce58b90bf81a8f22bb3783bf40f5",
        "CACHE_INDICATOR": "false",
        "mindboxDeviceUUID": "c8154a62-e117-4749-9e89-67769601e465",
        "directCrm-session": "%7B%22deviceGuid%22%3A%22c8154a62-e117-4749-9e89-67769601e465%22%7D",
        "_ga": "GA1.2.1771151270.1663583556",
        "tmr_detect": "1%7C1669483601209",
        "MVID_ENVCLOUD": "prod1",
        "_ga_CFMZTSS5FM": "GS1.1.1669483316.8.1.1669483815.0.0.0",
        "_ga_BNX5WPP3YK": "GS1.1.1669483316.8.1.1669483815.60.0.0",
    }

    headers = {
        "authority": "www.mvideo.ru",
        "accept": "application/json",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "baggage": "sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-t\
            race_id=4238ef8d96df49e8957a1628fb11b1c3,sentry-sample_rate=0%2C5",
        # Requests sorts cookies= alphabetically
        # 'cookie': 'HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21483091190; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=3; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; _ym_uid=1663583556254664400; _ym_d=1663583556; afUserId=13111e44-ca19-455a-9367-f8cd3e809735-p; flocktory-uuid=0968b95b-72c3-4fc3-95bb-bf6f496d95ad-7; uxs_uid=612be7e0-3806-11ed-82a6-5755a00505ae; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_MINDBOX_DYNAMICALLY=true; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; MVID_AB_PDP_CHAR=2; MVID_GLP=true; MVID_MULTIOFFER=true; MVID_GEOLOCATION_NEEDED=false; __ttl__widget__ui=1666631611106-a22682d0bff9; __lhash_=3d9cc0efe976beb0639d145cc3cd77ef; JSESSIONID=1tWjjCLSMq2bGSvMtgJkR7Ph646gN3mvJGSCQs74fLvpww2vwpTL!-955907452; COMPARISON_INDICATOR=false; flacktory=no; BIGipServeratg-ps-prod_tcp80=2969885706.20480.0000; bIPs=-971835924; MVID_GTM_BROWSER_THEME=1; SMSError=; authError=; _gid=GA1.2.997635636.1669483317; _sp_ses.d61c=*; _ym_isad=1; advcake_track_id=96b4f8fc-e1e9-06ee-fc3b-3cbeca4ede20; advcake_session_id=179dc93f-d768-9eb0-9bf4-9f804a1d049a; AF_SYNC=1669483317581; BIGipServeratg-ps-prod_tcp80_clone=2969885706.20480.0000; MVID_AB_TOP_SERVICES=2; MVID_GLC=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_LP_HANDOVER=0; tmr_lvid=9e31cad33a605f7702d119a87d5b6f39; tmr_lvidTS=1663583555766; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqfxRXIVp1QmAeTzM8PFccN1ppQi1iXXlzdy9yCyAkFXM2ZmhuRCwdRxs5Yx5ODSkMCRkXGjhuImRQWSZHWk9qJh8XCG8rUgoMX0VEdGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTI/bSBkT1kiQ11Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=aL0LnQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqfxRXIVp1QmAeTzM8PFccN1ppQi1iXXlzdy9yCyAkFXM2ZmhuRCwdRxs5Yx5ODSkMCRkXGjhuImRQWSZHWk9qJh8XCG8rUgoMX0VEdGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTI/bSBkT1kiQ11Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=aL0LnQ==; cfidsgib-w-mvideo=MkUJminCZ+IqZ9QCK635g5khkOKBJIg0SBT+n8mePvRUDIxgV2AMSyrb254TOTehk2PRri5QoDkNwXpCOVccOZ5ZiX9f5sTtPXmqHZ0sFMToWGNsAPck3rj0kZPP3nhgAQl8qq3jAhKppS6fCt/8HHBf0c6sJOp7thYxaQ==; cfidsgib-w-mvideo=MkUJminCZ+IqZ9QCK635g5khkOKBJIg0SBT+n8mePvRUDIxgV2AMSyrb254TOTehk2PRri5QoDkNwXpCOVccOZ5ZiX9f5sTtPXmqHZ0sFMToWGNsAPck3rj0kZPP3nhgAQl8qq3jAhKppS6fCt/8HHBf0c6sJOp7thYxaQ==; gsscgib-w-mvideo=AYDw+6QUk2zQhQzhAT9gskgWwXyQ/YszVfmRL9FHZ6bJ5R+UL/xaDgGdbHFapUR22U1eGSo18l61ISOWVIyFSQjpC33vS/GY9R6Lpw+SNFCfOwJ66WKFoYO649Watz/Ye0c3edt6oFpivefFTFpwZIcM8Hu0/BIH9fo0qDpEHer7f4NBkNwwjEdEwh32S42cKIC1h9gFzDI+Tzlg76giTLtb7o+TtVyAGjHXBCLJI8oaXZQJBrFWGR86XSMxtw==; gsscgib-w-mvideo=AYDw+6QUk2zQhQzhAT9gskgWwXyQ/YszVfmRL9FHZ6bJ5R+UL/xaDgGdbHFapUR22U1eGSo18l61ISOWVIyFSQjpC33vS/GY9R6Lpw+SNFCfOwJ66WKFoYO649Watz/Ye0c3edt6oFpivefFTFpwZIcM8Hu0/BIH9fo0qDpEHer7f4NBkNwwjEdEwh32S42cKIC1h9gFzDI+Tzlg76giTLtb7o+TtVyAGjHXBCLJI8oaXZQJBrFWGR86XSMxtw==; fgsscgib-w-mvideo=TIYA73835571ce58b90bf81a8f22bb3783bf40f5; fgsscgib-w-mvideo=TIYA73835571ce58b90bf81a8f22bb3783bf40f5; cfidsgib-w-mvideo=HjFvtkqFKZk2ciJXeYruKhZigxl3MCenylGWtGKTf52NJ+g0FGAkc3C5hIgg0uSV6ZncQgzEvxC+TBdtl832esrex4v02wc2GjUVLm+CTOox1vEFarCFg5ReLcQ+I8Vtn7UMBBaZxbPJwQ5dU17D6ebTdod96cygKGXplw==; CACHE_INDICATOR=false; mindboxDeviceUUID=c8154a62-e117-4749-9e89-67769601e465; directCrm-session=%7B%22deviceGuid%22%3A%22c8154a62-e117-4749-9e89-67769601e465%22%7D; _ga=GA1.2.1771151270.1663583556; tmr_detect=1%7C1669483601209; _sp_id.d61c=2a4ff3c9-c2f0-4c3b-9439-0fac8502fabf.1663583556.8.1669483613.1666631611.a91e59ce-de47-45c3-88f4-8489eb63260b.9f551086-ba14-4cd3-a8f6-4243faf7fbbe.f0a07ad2-389c-46e6-be25-fcd66207215d.1669483316650.66; MVID_ENVCLOUD=prod1; _ga_CFMZTSS5FM=GS1.1.1669483316.8.1.1669483815.0.0.0; _ga_BNX5WPP3YK=GS1.1.1669483316.8.1.1669483815.60.0.0',
        "referer": "https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914/tolko-v-nalichii=da",
        "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "4238ef8d96df49e8957a1628fb11b1c3-922756f90b5296e8-0",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, lik\
            e Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
        "x-set-application-id": "4b9719d1-3826-41f6-b47a-6e944084265c",
    }

    params = {
        "categoryId": "205",
        "offset": "0",
        "limit": "24",
        "filterParams": [
            "WyJjYXRlZ29yeSIsIiIsImlwaG9uZS05MTQiXQ==",
            "WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==",
        ],
        "doTranslit": "true",
    }

    response = requests.get(
        "https://www.mvideo.ru/bff/products/listing",
        params=params,
        cookies=cookies,
        headers=headers,
    ).json()
    # print(response)

    products_ids = response.get("body").get("products")
    with open("1_products_mvideo.json", "w", encoding="utf-8") as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        "productIds": products_ids,
        "mediaTypes": [
            "images",
        ],
        "category": True,
        "status": True,
        "brand": True,
        "propertyTypes": [
            "KEY",
        ],
        "propertiesConfig": {
            "propertiesPortionSize": 5,
        },
        "multioffer": True,
    }

    response = requests.post(
        "https://www.mvideo.ru/bff/product-details/list",
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()

    with open("2_item.json", "w", encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ",".join(products_ids)

    params = {
        "productIds": products_ids_str,
        "addBonusRubles": "true",
        "isPromoApplied": "true",
    }

    response = requests.get(
        "https://www.mvideo.ru/bff/products/prices",
        params=params,
        cookies=cookies,
        headers=headers,
    ).json()

    with open("3_prices.json", "w", encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get("body").get("materialPrices")

    for item in material_prices:
        item_id = item.get("price").get("productId")
        item_base_prise = item.get("price").get("basePrice")
        item_sale_price = item.get("price").get("salePrice")
        item_bonus = item.get("bonusRubles").get("total")

        items_prices[item_id] = {
            "item_base_prise": item_base_prise,
            "item_sale_price": item_sale_price,
            "item_bonus": item_bonus,
        }

    with open("4_item_prices.json", "w", encoding="utf-8") as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open("2_item.json", "r", encoding="utf-8") as file:
        products_data = json.load(file)

    with open("4_item_prices.json", "r", encoding="utf-8") as file:
        products_prices = json.load(file)
    products_data = products_data.get("body").get("products")

    for item in products_data:
        product_id = item.get("productId")

        if product_id in products_prices:
            prices = products_prices[product_id]

        item["item_basePrice"] = prices.get("item_basePrice")
        item["item_basePrice"] = prices.get("item_basePrice")
        item["item_bonus"] = prices.get("item_bonus")

    with open("5_result.json", "w", encoding="utf-8") as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == "__main__":
    main()
