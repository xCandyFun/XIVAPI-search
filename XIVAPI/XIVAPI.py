import http.client

def search_API(sheet):
    conn = http.client.HTTPSConnection("v2.xivapi.com")

    conn.request("GET", f"/api/sheet{sheet}")

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


search_API("/Item/3")