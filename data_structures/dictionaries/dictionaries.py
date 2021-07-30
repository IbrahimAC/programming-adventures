#Understanding Dictionaries, by implementing and testing them
#LINK to notes on dictionaries --> https://docs.google.com/document/d/1O4eur-XMKVq8v-qmDrUl9vmQ8F8SvWVCsbAITX_Z73I/edit?usp=sharing

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)

planes = {
    21 : 7,
    "senna" : 11,
    "raptor" : "hello",
    'raptor' : False
}
print(planes.fromkeys(planes,'sold'))
for gg in planes:
    print(gg)

for k,v in planes.items():
    if v >0:
        print(k,v)
        


