file=open("running-config.cfg")
list2=[]
listvalues=[]
dictionary=dict()

i=0

for line in file:
 if "access-list" in line:
  value=line
  list1=line.split()
 
  key=list1[1]
  list2.append(key)
  if key in list2:
    listvalues.append(value)
    dictionary[key]=listvalues
  else:
    dictionary[key]=value

print(dictionary)
