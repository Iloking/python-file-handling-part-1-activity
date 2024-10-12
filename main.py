#create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if New_File exists or not....")
if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
else:
    print("The file does not exist")

#create a new if it doesn't
my_file = open("New_File.txt", 'w')
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()

#delete file named codingal
os.remove('Codingal.txt')

#delete the folder
os.rmdir('Folder')