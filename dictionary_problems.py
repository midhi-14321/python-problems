# Given two lists, one with keys and one with values, create a dictionary.
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
dic={}
for i in range(len(keys)):
    dic[keys[i]]=values[i]

print(dic)
