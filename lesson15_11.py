import fileinput

#file=open('students.csv',encoding='utf-8',mode='r',newline='')
file=open('students.csv','r')
print(file.readline)
print(file.readline)
print(file.readline)
file.close()