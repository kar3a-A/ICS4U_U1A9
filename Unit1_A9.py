## Firstly we have to collected Name, Birthplace, 
## School and Favourity subject  althogether with only '3' variables
Name = input("Enter your full name with space between each of them: ")
Birthplace = input("Enter your birthplace: ")
School_FavSub = input("Enter your school name and favourity subject with , betwen each of them: ")

## We have to create a simple dictionary to store Name , School and Favourity Subject
## Name is split into First Name, Middle Name and Last Name with .split(" ")
## Then store in the mydict "dictionary" 
## School name and Favourite subject is also split and insert into the dictionary with above .split(",") 
mydict = {}
mydict = Name.split(" ")
mydict += School_FavSub.split(",")

#Then print out the store data 
## such as firstname, middle name, lastname, birthplace, school, favourite subject with relavent letter
## In the output process I use 'variable insert within string' method with f"..." to output more convinient way 
## Lastly, in the last output I want to use \n to go to next line of output but 
## since the output should be six print statement I considered back to use six print statement 
print("To Whom This May Concern:")
print(f"My name is {mydict[0]} {mydict[1]} {mydict[2]}. I am orginated from {Birthplace}. I am currently attending")
print(f"{mydict[3]} with my favourite course as {mydict[4]}.")
print()
print(f"Sincerely, " )
print(f"{mydict[0]} {mydict[1]} {mydict[2]}")
