#Python can be used to perofrm oprations on a file,(read and write)
'''
Types of files

Text file: .txt,.docx, .log,etc
Binary file: .mp4,.jpeg, .mov, .png etc
'''
#open read and close
'''
we have to open a file before reading and writing.
f = open("file_name","mode")
'''

f = open("demo.text","rb")
data = f.read(8)
print(data)
print(type(data))
f.close