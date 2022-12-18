import json
 
with open ('config.json','r',encoding="utf-8") as file:
    data = json.load(file)
 
data["author"] ="Jamil"
data["server"]["port"] = 2024
data["server"]["port2"] = 2025
data["openInBrowser"] = True
data["dist"]["fonts"] = "Arial"
 
with open("my_config.json", "w") as file:
    json.dump(data, file)
