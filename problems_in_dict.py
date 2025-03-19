# find the highest value of key in the dictionary
values={'1':2,'str':4,'55':12,'apple':11}
max_value=float('-inf')
max_key=""
for key,value in values.items():
    if (value)>(max_value):
        max_value=(value)
        max_key=key
print(max_key)
    
#swap key value pairs and append to a new dictionary and print
values={'1':2,'str':4,'55':12,'apple':11}
dic={}
for key,value in values.items():
    key,value=value,key
    dic[key]=value
print(dic)

# merge two unique key dictionary's
dict1={'k1':2,'k2':4,'k3':-2}
dict2={'k1':2,'k4':10}
output={}
for key,value in dict1.items():
    output[key]=value
for key,value in dict2.items():
    if key in output:
        output[key]+=value
    else:
        output[key]=value
print(output)

# iterate the list and count the values and append in new_dict
lst=[1,2,1,4,2,1]
dic={}
dic2={}
for key in lst:
    if key not in dic:
        dic[key]=1
    else:
        dic[key]+=1
for key,value in dic.items():
    if value>1:
        dic2[key]=value
print(dic2)