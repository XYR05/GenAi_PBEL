p="/home/harry/Internship - ibm"
# v=open(p, "w")

# v.write("This is a new line added to the file.\n")  

# v.close()


# r=open(p, "r")
# content = r.read()
# print(content)
# r.close()


# f2=open(p+"/newfile.txt", "w+")
# f2.write("Harry Gill,  \n sudo name: XYROS" )
# f2.seek(0)  # Move the file pointer back to the beginning of the file
# c=f2.read()
# print(c)
# f2.close()



with open(p+"/newfile.txt", "r") as f3:
    content = f3.read()
    print(content)


### Modes

# "r" - Read mode (default): Opens a file for reading. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.

# "w" - Write mode: Opens a file for writing. If the file already exists, it truncates the file to zero length (i.e., deletes the existing content). If the file does not exist, it creates a new file.

# "a" - Append mode: Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.

# "r+" - Read and write mode: Opens a file for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.

# "w+" - Write and read mode: Opens a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.

# "a+" - Append and read mode: Opens a file for both appending and reading. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.       

# "x" - Exclusive creation mode: Opens a file for exclusive creation. If the file already exists, it raises an error. If the file does not exist, it creates a new file.

# "b" - Binary mode: This is not a standalone mode but can be combined with other modes (e.g., "rb", "wb", "ab") to indicate that the file should be treated as a binary file rather than a text file. In binary mode, data is read and written in bytes rather than characters.    

# "t" - Text mode: This is the default mode and can be combined with other modes (e.g., "rt", "wt", "at") to indicate that the file should be treated as a text file. In text mode, data is read and written as characters, and newline characters are automatically handled.

# "U" - Universal newline mode: This mode is deprecated in Python 3. It was used in Python 2 to allow for universal newline handling, where different types of newline characters (e.g., \n, \r\n, \r) were treated as a single newline character. In Python 3, universal newline handling is enabled by default when reading files in text mode, so this mode is no longer necessary.  

# "rb" - Read binary mode: Opens a file for reading in binary mode. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.

# "wb" - Write binary mode: Opens a file for writing in binary mode. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.

# "ab" - Append binary mode: Opens a file for appending in binary mode. The file pointer is placed at the end of the file. 

