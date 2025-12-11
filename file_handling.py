# OPen file/Create file
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","x")
f.write("Hello Python!")
f.close()

#Write file
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","w")
f.write("Hello Python!")
f.close()

#Read File
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","r")
print(f.read())
f.close()

#Append mode
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","a")
f.write("Hello World!")
f.close()

#Line() function
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","r")
for line in f:
    print(line)
f.close()

#Split() function
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","r")
for line in f:
    tokens = line.split(' ')
    print(str(tokens))
f.close()

#Wordcount using len() function
f = open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","r")
f_out = open("F:\\Python_Practice\\Python_Practice_Project\\funny_wc.txt","w")
for line in f:
    tokens = line.split(' ')
    f_out.write("Wordcount:"+str(len(tokens))+"  "+line)
f.close()
f_out.close()

#with statement
with open("F:\\Python_Practice\\Python_Practice_Project\\funny.txt","r") as f:
    print(f.read())
print(f.closed)

'''
#Without with
file = open("data.txt", "r")
content = file.read()
file.close()    #must remember

#with statement(Best practice)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
'''

