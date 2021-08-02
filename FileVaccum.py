import os

path = input("Enter the path of the file")
#days = int(input("After how many days do you want your files to be deleted?"))

if (os.path.exists(path)):
	os.remove(path)
	print("File removed")
else:
	print("Path does not exist")
	
