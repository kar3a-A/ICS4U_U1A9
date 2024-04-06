## Firstly we have to collected Name, Birthplace, 
## Birthplace, School and Favourity subject  althogether with '2' variables=>Name and Birthplace_School_FavSub
Name = input("Enter your full name with space between each of them: ")
Birthplace_School_FavSub = input("Enter your birthplace, school name and favourity subject with , betwen each of them: ")

## We have to create a simple varible as list to store Name , School and Favourity Subject 
## Therefore, total of three variables only including: Name, Birthplace_School_FavSub and mylist
## Name is split into First Name, Middle Name and Last Name with .split(" ")
## Then store in the mylist "list" 
## BIrthplace, School name and Favourite subject are also split and insert into the list with above .split(",") 
mylist = []
mylist = Name.split(" ")
mylist += Birthplace_School_FavSub.split(",")

#Then print out the store data 
## such as firstname, middle name, lastname, birthplace, school, favourite subject with relavent letter
## In the output process I use 'variable insert within string' method with f"..." to output more convinient way 
## Lastly, in the last output I want to use \n to go to next line of output but 
## since the output should be six print statement I considered back to use six print statement 
print("To Whom This May Concern:")
print(f"My name is {mylist[0]} {mylist[1]} {mylist[2]}. I am orginated from {mylist[3]}. I am currently attending")
print(f"{mylist[4]} with my favourite course as {mylist[5]}.")
print()
print(f"Sincerely, " )
print(f"{mylist[0]} {mylist[1]} {mylist[2]}")
