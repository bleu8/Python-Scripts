import requests
import json

gelen_cevap= requests.get("http://api.open-notify.org/astros.json")

number_of_people= gelen_cevap.json()["number"]

print(f"uzaydaki insanlar {number_of_people} kisi")

print("uzaydaki insanların isimleri")
print("------------------------")

for kisi in gelen_cevap.json()["people"]:
	print(kisi["name"],"----->",kisi["craft"])


