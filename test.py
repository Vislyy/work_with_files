import json


with open("example.json", 'r', encoding="utf=8") as file:
    content = json.load(file)
    print(content["Ім'я"])
