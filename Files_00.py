'''
Opening a File

It is done using the open() function. No module is required to be imported for this function.

File_object = open(r"File_Name","Access_Mode")
The file should exist in the same directory as the python program file else, the full address of the file should be written in place of the filename. Note: The r is placed before the filename to prevent the characters in the filename string to be treated as special characters. For example, if there is \temp in the file address, then \t is treated as the tab character, and an error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in the same directory and the address is not being placed.
'''

