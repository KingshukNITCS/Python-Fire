str = "abcde"
rep_str = str*3
print(rep_str)
print(len(rep_str))
print(str[1:3]) #bc
print(str[1:])
print(str[1:5])
print(str[1:-2]) #bc
print(str[-1]) #e
print(str[:-1]) #abcd


str = "abcde"
print(str.upper())
print("AbCdE".lower())
stri = " abc "
print(stri.strip())
print(stri.lstrip() + str)
print(stri.rstrip() + str)
print(str.replace("bcd","1245"))
print(str.find("cd"))

# Creating a String 
String1 = "GeeksForGeeks"

# Printing 3rd to 12th character 
print("Slicing characters from 5-12: ") 
print(String1[5:12]) 

# Printing between 3rd and 2nd last character 
print("Slicing characters between " +
	"3rd and 3rd last character: ") 
print(String1[3:-3]) 

string = "python program run on python IDLE, in pythonic way."
count = string.count("python")
print(count)

string = "Python is powerful and Pythonic."
index = string.find("Python")
print(index) 
index = string.find("python")
print(index) #-1

# Default order 
String1 = "{} {} {}".format('Begineer', 'in', 'Python') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Begineer', 'in', 'Python') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g='Begineer', f='in', l='Python') 
print("\nPrint String in order of Keywords: ") 
print(String1) 


