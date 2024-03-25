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
