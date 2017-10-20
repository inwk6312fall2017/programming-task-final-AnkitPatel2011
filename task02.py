from builtins import print
from weather import Weather

weather = Weather()

#checking  via  location name
halifax = input("Enter the location : ")

location = weather.lookup_by_location(halifax)
condition = location.condition()
print ("The current erather is "+condition['text'])

a=[]
i=0

for forecasts in location.forecast():

	if i<5:
	 b=[]
	 b.append(forecasts['text'])
	 b.append(forecasts['date'])
	 b.append(forecasts['high'])
	 b.append(forecasts['low'])
	 i+=1
	 a.append(b)

print(a)

max=0

for lists in a:
	if int(lists[2]) > max:
	 max=int(lists[2])
	 results=lists[1]
print(results)

