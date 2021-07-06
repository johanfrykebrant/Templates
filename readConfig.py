import json


# ---- READ FROM CONFIG ----
with open("test.config") as json_data_file:
    data = json.load(json_data_file)

print(data["mysql"]["db"])

# ---- WRITE CONFIG ----
# First, fetch the file you want to change
data = open("test.config", "r")
jobj = json.load(data)
data.close()
print(jobj)

#Make changes in JSON object. 
jobj["API keys"]["key1"] = 1234567

#Write the changes to the file
data = open("test.config", "w")
json.dump(jobj, data, indent = 2)
data.close()


