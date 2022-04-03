my_File = open("hello.txt",mode='r')
content = my_File.read()
print(content)
my_File.close()
# In this we have to closew the file otherwise burden on our computer

# or

with open("hello.txt") as file :
    content2 = file.read()
    print(content2)

with open("hello.txt", 'w') as file2:
    file2.write("hello again")

with open("hello.txt", 'a') as file2:
    file2.write("hello again")


