import requests
import json
gel=requests.get("http://api.open-notify.org/astros.json")

insan = gel.json()["number"]


print(f"su anda uzaya {insan} var")

print("uzaydaki insnaların isimleri")


print("--------------------------")

for a in gel.json()["people"]:
    print(a["name"],"----->",a["craft"])