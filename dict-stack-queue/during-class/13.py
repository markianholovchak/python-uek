import json

# data.json contains information about apps in some app store
with open("data.json") as f:
    apps = json.load(f)

for app in apps:
    for key,val in app.items():
        print(f"{key} : {val} ")
    print("----------------------------")
    