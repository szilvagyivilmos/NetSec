import socket
import knocker
import os
import re
import hashlib
import requests

ip = "152.66.249.144"
ports=["1337","2674","4011"]

#knocking
os.system("python3 knocker.py "+ip+" 1337 2674 4011")

#tcp connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 8888))
print("connected")

print(s.recv(1024))
s.send("BP88RR".encode())

print(s.recv(1024))

#calc
equasions= str(s.recv(1024))
print(equasions)

numbers=re.findall(r'\d+',equasions)

count=numbers[0]

signs=re.findall(r'\-|\+',equasions)

for j in range (1,int(count)+1):
    print(str(j)+". feladat")

    d=2
    if(j==1): d=3
    else:equasions = str(s.recv(1024))



    numbers = re.findall(r'\d+', equasions)
    signs = re.findall(r'\-|\+', equasions)
    solution=int(numbers[d-1])



    for i in range(0,len(signs)):
        if(signs[i]=="+"):
            solution+=int(numbers[i+d])
    #        print("+ "+numbers[i+3]+" = "+str(solution))
        else:
            solution-=int(numbers[i+d])
    #        print("- " + numbers[i + 3] + " = " + str(solution))
    print(solution)
    s.send(str(solution).encode())



#Hash
print(s.recv(1024))
print(s.recv(1024))
s.send(hashlib.sha1(str("BP88RR"+str(solution)).encode('utf-8')).hexdigest().encode())
print(hashlib.sha1(str("BP88RR"+str(solution)).encode('utf-8')).hexdigest())


#0000Hash
print(s.recv(1024))
print(s.recv(1024))

for i in range(0,100000):
    k=str("BP88RR"+str(solution) + str(i))
    h=hashlib.sha1(k.encode('utf-8')).hexdigest()
    if (h[:4]=="0000"):
        print(k+"\n"+str(i)+" : "+h)
        break
s.send(k.encode())

#Cert
print("Cert\n")
print(s.recv(1024))
print(s.recv(1024))
print(s.recv(1024))




s.close()