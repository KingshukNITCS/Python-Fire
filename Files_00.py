'''
Opening a File

It is done using the open() function. No module is required to be imported for this function.

File_object = open(r"File_Name","Access_Mode")
The file should exist in the same directory as the python program file else, the full address of the file should be written in place of the filename. Note: The r is placed before the filename to prevent the characters in the filename string to be treated as special characters. For example, if there is \temp in the file address, then \t is treated as the tab character, and an error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in the same directory and the address is not being placed.
'''
# Open function to open the file "MyFile1.txt" 
# (same directory) in append mode and
file1 = open("MyFile.txt","a")
  
# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt","w+")

# Here, file1 is created as an object for MyFile1 and file2 as object for MyFile2
'''
Closing a file

close() function closes the file and frees the memory space acquired by that file. It is used at the time when the file is no longer needed or if it is to be opened in a different file mode. File_object.close() 
'''

'''
Writing to a file

There are two ways to write in a file.

write() : Inserts the string str1 in a single line in the text file.
File_object.write(str1)
writelines() : For a list of string elements, each string is inserted in the text file.Used to insert multiple strings at a single time.
File_object.writelines(L) for L = [str1, str2, str3] 
Reading from a file

There are three ways to read data from a text file.

read() : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
File_object.read([n])
readline() : Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.
File_object.readline([n])
readlines() : Reads all the lines and return them as each line a string element in a list.
  File_object.readlines()
Note: ‘\n’ is treated as a special character of two bytes 

'''