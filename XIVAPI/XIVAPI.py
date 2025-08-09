import http.client

conn = http.client.HTTPSConnection("v2.xivapi.com")

conn.request("GET", "/api/asset?path=ui%2Ficon%2F051000%2F051474_hr1.tex&format=png")

res = conn.getresponse()
data = res.read()

file_dir = "image/test.png"

with open(file_dir, "wb") as fp:
    fp.write(data)
print("Image downloaded successfully.")
