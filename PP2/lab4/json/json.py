import json
import requests

with open('json/sample_data.json', 'r') as file:
    data = json.load(file)

imdata = data["imdata"]
headers = ["dn", "descr", "speed", "mtu"]
print("=" * 90)
print(f"{headers[0]:<50} {headers[1]:<20} {headers[2]:<10} {headers[3]:<10}")
print("-" * 80)
for item in imdata:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes.get("dn")
    descr = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")

    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")M