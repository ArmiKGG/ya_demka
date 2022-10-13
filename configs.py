cookie = {'yandexuid': '2801698381655450086', ' yuidss': '2801698381655450086', ' gdpr': '0',
          ' amcuid': '666553071655450189', ' mda': '0', ' my': 'YwA=', ' is_gdpr': '0', ' is_gdpr_b': 'CNucGhCbeSgC',
          ' font_loaded': 'YSv1', ' yandex_gid': '2', ' _ym_uid': '1657185863478971770',
          ' sae': '0:4D2455FD-1913-4B9F-B131-A43EC3BC2699:p:22.5.0.1916:m:d:RU:20220617',
          ' spravka': 'dD0xNjU3Mzc5NjcwO2k9NDUuMTM2LjI0Ni41MztEPUE4ODM2OUI3Q0E5RjA4RDM2RjczQUNGNjlGMUIzRjQ4NUVFMzE0MEI3MTM2QTVEMUQ5QTc1MTEwMjA2MTFGMTdGRjExNDE3Mjt1PTE2NTczNzk2NzA5OTg3NTI4ODM7aD02NWRjZGEyMGEyYjc5NzdjZGNmODNlMzY0ZjY1M2Y1ZA==',
          ' L': 'cT97VEcIfmhcfF1aXVV8XEZEQVxff2JXGg8jHz4uMVUMA1sLdiES.1657392782.15033.327311.13788ee41dfa807d820b9e0f3198179a',
          ' yandex_login': 'kirill@devjs.ru', ' cycada': 'IA4W0PKUxGmSNC89dKv4eEDX6cdvr3CTbRT54WP1FXM=',
          ' ymex': '1970810088.yrts.1655450088#1972825888.yrtsi.1657465888', ' _ym_isad': '2', ' _ym_d': '1657466332',
          ' yabs-frequency': '/5/100B01VDoMAsHybY/-E5KvAxPdq9qHo5LztfWcqX-KdH78IBjJmGCfCPkT4SZIkQnfDqwfKPeHou0/',
          ' _yasc': '7cPgSiJQSkc1XdamNvFZnvd+Ftykm7E7BJ0vwlm8rjtNHkAmmb03qo7KBMKLpXUQ7EzF9ve8dLZ4RA==',
          ' ys': 'svt.1#def_bro.1#udn.cDpraXJpbGxAZGV2anMucnU%3D#wprid.1657466382310092-11583376320511124606-sas6-5246-13c-sas-l7-balancer-8080-BAL-5934#ybzcc.ru#newsca.native_cache',
          ' yp': '1686986088.cld.1955450#1972752782.udn.cDpraXJpbGxAZGV2anMucnU%3D#1687344637.ygu.1#1673234334.szm.2:1440x900:1440x800#1660144743.csc.1#1971080131.multib.1#1971080256.2fa.1#1657616503.clh.1955452#1657473060.gpauto.59_93895%3A30_315636%3A100000%3A3%3A1657465860#1657952529.mcv.0#1657952529.mcl.1ygm49n#1657468131.rnwcst.3'}


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru,en;q=0.9"
}


string_cookie = 'is_gdpr=0; is_gdpr_b=CJ2cGhC5jwE=; gdpr=0; _ym_uid=1664162086643216049; _ym_d=1665699386; _ym_isad=1; yandexuid=8932436291665699385; yuidss=8932436291665699385; ymex=1981059385.yrts.1665699385#1981059385.yrtsi.1665699385; spravka=dD0xNjY1Njk5NTgwO2k9OTEuMTg5LjI0Mi4yMzc7RD05NzYzREJDQjdFNTEyOUEzMEM4M0VEMDcwMzc5OUUwODhBRkM2Rjk5ODZCRDREQkMxNzQwNUYyMEU0OUYzOTZBOEQ5MkQ4MzM7dT0xNjY1Njk5NTgwNDUwNTY3Nzk1O2g9MTI3ZGM1ODBhMmJlYzAwNzk0ZWQ1MGFjYjQ0ZmU2OGM=; _yasc=hy/1VnzudO1qIgKrPXW7SE4iBtYGgM9kAHiJGCoZ/bFEBoyUDqma+NOKRbnebQ==; _ym_visorc=b; yp=1981063732.udn.cDphcm1hbnNsYXB0b3BAZ21haWwuY29t; L=aiACdkZAUHpnTH5KTWZrDFx8YlhSVUILACUlVRk+BVAFMR4ccSAEES4HFhQ4Pg==.1665703732.15129.333190.2cabdec6a4797fadad5b7ad41fe067c2; yandex_login=armanslaptop@gmail.com; ys=udn.cDphcm1hbnNsYXB0b3BAZ21haWwuY29t#c_chck.1935191041'


cookie_2 = {}

for cook in string_cookie.split("; "):
    cookie_2[cook.split("=")[0]] = cook.split("=")[1]


headers_2 = {
    "accept": "text/html,application/json,text/plain,*/*",
    "accept-language": "ru,en;q=0.9",
    "cookie": string_cookie
}
