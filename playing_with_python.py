data = {"Mouse":150,"LED":7500,"Keyboard":200,"CPU":10000}

#representing dictionary key and values using the format method

print("First way:")
print (' '.join(['{0}:{1}'.format(k, v) for k,v in data.items()]))
print("Second way:")

#representing dictionary key and values using for loop

for key,value in data.items():
    print(key,value,sep=":",end=" ")

#representing the keys and values using the methods of dictionary

print("\n")
print("Third way:")
keys = data.keys()
values = data.values()
print(keys,values,end=" ")

















