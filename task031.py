#to append in file a is used, + is used to create a file if it is not there .
 
newfile=open("RUNNING-CONFIG.CFG","a+")

#open the given file 

file=open("running-config.cfg")

for line in file:
 editeddata=line.replace("172.","192.")
 newfile.write(editeddata)




