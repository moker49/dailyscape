import requests, json

myItems = {
   "1607":"Cut Saphire",
   "1617":"Uncut Diamond",
   "1619":"Uncut Ruby",
   "1621":"Uncut Emerald",
   "1623":"Uncut Saphire",
   "3420":"Limestone Brick",
}

# generate url
url = 'https://api.weirdgloop.org/exchange/history/rs/latest?id='
for key, value in myItems.items():
   url += key + '|'
url = url[0:-1]


# grab old data
old_data = {}
try:
   with open('myrsdata.json') as f:
      old_data = json.load(f)
except Exception:
   pass


# fetch new data
new_data = {}
try:
   headers = {"user-agent": "ge-prices-to-see-if-dailies-worth"}
   new_data = requests.get(url, headers=headers)
   new_data = new_data.json()
except Exception:
   pass


# generate and store script with old a new prices
with open("read.js", "w") as f:
   for key, value in myItems.items():
      f.write(f'rsapidata["{key}"] = {{')
      f.write(f'"name": "{value}",')

      old_price = 0
      try:
         old_price = old_data[key]["price"]
      except KeyError:
         pass

      new_price = old_price
      try:
         new_price = new_data[key]["price"]
      except KeyError:
         pass

      f.write(f'"last": {old_price},')
      f.write(f'"price": {new_price},')
      f.write(f'}}\n')


# store new data
with open('myrsdata.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)


