# Playing-with-dictionaries-python
## Key features of this code
<ol>
  <li>Keys and values are feteched using different ways</li>
  <li> First Way includes, join and format with dictionary.items()</li>
  <li> Second way includes key, values and dictionary.items()</li>
  <li> Third way includes using the methods of the dictioanries</li>
</ol>  

Please have a look at the below image  

![dictionary500x300](https://user-images.githubusercontent.com/47202519/52691057-ae200280-2f85-11e9-8e4c-d32cecbe4c57.jpg)

## Implementing ways with code

### First Way
```
print("First way:")
print (' '.join(['{0}:{1}'.format(k, v) for k,v in data.items()]))
print("Second way:")
playing_with_python.py
```
### Second Way
```
for key,value ikeys = data.keys()
values = data.values()
print(keys,values,end=" ")n data.items():
    print(key,value,sep=":",end=" ")
```

### Third Way
```
keys = data.keys()
values = data.values()
print(keys,values,end=" ")
```

## How to run this file

Since this is a python file, hence it can be run using following command

```
python playing_with_python.py
python3 playing_with_python.py
```
