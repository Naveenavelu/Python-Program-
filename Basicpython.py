# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 10:29:44 2023

@author: Naveena Palanivelu
"""
print (" 1. Read the file and return the no of word occurence")
fil2=open("file1.txt","r")
print("file opened successfully")
fil3=open("file1.txt","r") 
l='navee'  
#passfil=open("output.txt","w")
for x in fil3:
    spli= x.split()
    print("count of the particular word", (spli.count('navee'))   )
x1=str(spli.count('paris'))    
fi1=open("output.txt","w")
print(x1)
fi1.write(x1)
fi1.close()

print ("**************2.Reading the line from text file****************")
fi2=open("file2.txt","r")  
c1=fi2.readline()
c2=fi2.readline()
print(c1)
print(c2)

print ("**************3.Handling the File not found error****************")
try:
    fi2=open("file5.txt","r")   
    print ("file found in the location")
except:
    print("file not found")    
print ("**************3.merging two sorted list into one****************")
a= ['Nov','Benz','Yummy']
n=['Apple','Eva','Incecube','Ox']
a.sort(key=len)
n.sort(key=len)
for i in n:
    a.append(i)
print("After the merging of sorted list",a)
print(n)
print ("**************4.Count of occurence of character in a string and print them in Dictinoary****************")
word="programming"
ct=dict()
x1=""
for r in word:
    if r in ct:
        ct[r]+=1
    else:
        ct[r]=1
print ("occurence of character in dictionary format", ct)        
        
print ("**************5.Intersection of 2 Sets****************")
print ("-----union in set---")
c={"London","Greece","Italy","Paris","Finland"}
d={"India","China","Japan","Paris"}
e=c.union(d)
print("Print the union of sets",e)
print ("-------------")
n1={"London","Greece","Italy","Paris","Finland"}
d1={"India","China","Japan","Paris"}
e1=n1.intersection(d1)
print("-----intersection in set--",e1)


import re

print ("6.)*************************String Reverse and palindrome*************************")
#1 Way
"""
x="naveena"
x1=x[::-1]
print (x1)
if (x1==x):
        print("The input value is palindrome")
else  :
            print("The input value is not palindrome")
"""
#2 Way
x1="naveena"
y=""

x=len(x1)-1

while (x >=0):
    y+=x1[x]  
    x-=1
print (y)
if y==x1:
    print("The input value is palindrome")
else:
    print("The input value is not  palindrome")

   
   
print ("7.)*************************Counting Vowels in a Given Word *************************")
##if data should validate across the list use the if condition as x in y 
##if data should validate across the string  use the if condition as x in y or x==y  

vowel = ['a', 'e', 'i', 'o', 'u']
vowel1 = "a"
print (type(vowel1))
word = "programming"
x= 0
for y in word:
    if y in vowel:
   # if y == vowel1:
        x+=1
        print (y)
        print(x)
print ("counting the vowels from the Input Letter",(x))        

 

print ("8.)*************************Counting Consonants in a Given Word *************************")
##if data should validate across the list use the if condition as x not in y 
##if data should validate across the string  use the if condition as x in y or x!==y  

vowel = ['a', 'e', 'i', 'o', 'u']
vowel1 = "a"
print (type(vowel1))
word = "Naveena"
x= 0
for y in word:
    if y not in vowel:
   # if y !== vowel1:
        x+=1
        print (y)
        print(x)
print ("counting the consonants from the Input Letter",(x))   

print ("9.)*************************Counting the Number of Occurances of a Character in a String *************************")
##if data should validate across the list use the if condition as x not in y 
##if data should validate across the string  use the if condition as x in y or x!==y  


x1 = "m"
print (type(x1))
word = "programmingsmmmm"
x= 0
for y in word:
    if y == x1:
            #if y  in x1:
        x+=1
        print (y)
        print(x)
print ("counting the string from the Input Letter",(x))   

print ("9.)*************************Counting the Maximun nos in a list*************************")
##if data should validate across the list use the if condition as x not in y 
##if data should validate across the string  use the if condition as x in y or x!==y  


nos = ['1', '2', '3', '7', '5']
print (type(nos))
print (nos[0])
lst=nos[0]
print (type(lst))
for y in nos:
   # print(y)
    if y > lst:
        lst=y
       
print (y)

print ("10.)*************************Counting the Minimum nos in a list*************************")
##if data should validate across the list use the if condition as x not in y 
##if data should validate across the string  use the if condition as x in y or x!==y  


nos = ['1', '2', '3', '7', '5']
print (type(nos))

lst=nos[0]
print (type(lst))
for y in nos:
   # print(y)
    if y > lst:
        y=lst
       
print (y)

print ("11.)*************************Finding the Middle Element in a List*************************")


# way 1 using while loop
nos = ['1', '2', '3', '7', '5','8','9']
print (type(nos))

lst= int (len(nos)/2)
print (type(lst))
x=0
while (x <= lst-1):
    print(x)
    x+=1  
if x==lst:
            print("Middle element is :",nos[x])
   
else:
  
    print("Middle element not found from the list ")


# way 2 without while loop
nos = ['1', '2', '3', '7', '5','8','9']
print (type(nos))

lst= int (len(nos)/2)
print ("Middle element from way 2 :",(nos[lst]))

print ("9.)************************* Converting a List into a String*************************")
lst = ["P", "Y", "T", "H", "O", "N"]
y=""

x=0
print ("length of the index:",len(lst))
while (x <=len(lst)-1):
    y+=str(lst[x] ) 
    x+=1
print(" Output of the value converted into String -->" ,y)    

print ("12.)************************* Adding Two List Elements Together from array list*************************")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 
x=[]
y=0
while (y < len(lst1)):
    print(y)
    x.append(lst1[y]+lst2[y])
    y+=1
print ("Adding Two List Elements Together from array list",x)
    
print ("13.)************************* 15. Counting the White Spaces in a String*************************")
string = "P y th on pgm "
print(string.count(' '))   
word = "p y th on pgm "
print("count of the particular letter", (word.count('p'))   )

print ("14.)************************* Counting Special Characters in a String*************************")
word = "P y +-th #on pgm "  
readstr1= re.findall(r'[^a-zA-Z0-9\s]', word) # search the character other than upper case, lower case, space, nos
print ("No of spcl chrtr in the word",(readstr1))
print ("No of spcl chrtr in the word",len(readstr1))


print ("15.)************************* Coverting into list--> tuple, sets*************************")
lstdays = ['S','M','T','W','Tr','F','St'] 
lst =tuple(lstdays)
print ("Date type of the variable after conversion into tuple  ",type(lst))
print ("Date conversion into tuple ",(lst))


lst1 =set(lstdays)
print ("Date type of the variable after conversion into sets  ",type(lst1))
print ("Date conversion into sets ",(lst1))

print ("16.)************************* Randomizing the Items of a List in Python*************************")
"""nos2 = ['word', 'nave','velu']
aftrshuffle= shu(nos2)
print(aftrshuffle)"""

print ("17.)*************************Write a program to print the given number is odd or even. *************************")
num = 7
if (num %2)==0:
    print ("The entered no is even no")
else:
     print ("The entered no is odd no")
     
print ("18.)*************************Write a program to print the given number  list is odd or even. *************************")     
nos = ['9', '8', '11', '7', '5']
print (type(nos))
print (nos[0])
lst=nos[0]
print (type(lst))
for y in nos:
    if (int(y) %2)==0:
        print ("The entered no is even no",y)
    else:
         print ("The entered no is odd no",y)
print ("19.)*************************Write a program to print the given number  positive or negative . *************************")     
nos1 = ['9', '8', '11', '0', '-5']
print (type(nos1))
print (nos1[0])
for x in nos1:
    if (int(x) <0):
        print ("The entered no is negative no",x)
    else:
         print ("The entered no is positive no",x)
print ("20.)*************************Write a program to print the given number  prime no or not . *************************")              
nos2 = ['9', '8', '11', '4', '13']

for x in nos2:
    
    if int(x) >1:
        y= int(x)
        for i in range (2,y):
            if (y %i)==0:
                print ("The entered no is primeno",y)
                break
    else:    
        print ("The entered no is not  primeno",y)
print ("21.)*************************Write a program to print the given number  is palindrome. *************************")        
p=1234
rev=p
div=0
while p>0:
    x=(p%10)
    div=(div*10)+x
    #print (div)
    p=p//10
    print("remaining no",p)
    if (p)<0:
        break
if div ==rev:
    print ("Given no is palindrome")    
else:
     print ("Given no is not a palindrome")         
    
print ("22.)*************************Write a program to check if the given strings are anagram or not. *************************")           

word1="read"
word2='dear'
if sorted(word1)==sorted(word2):
    print ("The given word are anagram")
else: 
    print ("The given word is not a anagram")
print ("23.)*************************Write a program to print a pattern. *************************")           

"""
def num(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
"""
x=[]
print ("24.)*************************Nos which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).*************************")      
for i in range(2000,3200 ):
    if (i%7==0) and (i%5!=0):
        x.append(str(i))
print ("list of elements",x)
        
print ("7.)************************* output should be:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}*************************")      
n=10
dt={}
for i in range(1,n+1):
    dt[i]=i*i  # o/p {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
   # dt=i*i  # o/p 100
print ("Output of the element in dict format",dt)

print ("25.)*************************coverting the comms sepearated values into list 6 tuple *************************")      

n=[10,20,30]
print (type(n))
tu=tuple(n)
print ("after the conversion from list into tuple",(tu))


print ("addition of matrix")
a=[[0,1,2],
   [2,3,4],
   [5,6,7]]
b=[[3,4,5],
   [5,6,7],
   [9,0,5]]
n=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range (len(a)):
    print("Value of i:",i)
    for j in range(len(a[0])):
        print("Value of J:",j)
       # print(i)
        n[i][j]=a[i][j]+b[i][j]
       
print (n)


print("26.)**********************************************Multiplication of matrix*****************")
a=[[0,1,2],
   [2,3,4],
   [5,6,7]]
b=[[3,4,5],
   [5,6,7],
   [9,0,5]]
n=[[1,1,1],
   [1,1,1],
   [1,1,1]]
for i in range (len(a)):
    for j in range(len(a[0])):
        #print(j)
       # print(i)
        n[i][j]=a[i][j]*b[i][j]
       
print (n)



print("27.)*********************transpose of matrix'''''''''''''''''''''''''")
a=[[1,2,3],
   [4,5,6]]
n=[[0,0],[0,0],[0,0]]
for i in range (len(a)):
    print(i)
    for j in range(len(a[i])):
        print ("value of j:",j)
        n[j][i]=a[i][j]
for r in n:
    print(r)
   #print ("The value of n is ;",n) 
   
"""    
#Vertical concertination
a=["matrix","join"]

for i in a:
    print(i)
"""

#diciotnary 
# pass the values with keys 
# dont use the duplicate key 
emp={'Name' :'Nave','exp':5,'role': 'Analyst','salary':100}
print (type(emp))
print (emp )
print (emp.keys())
print (emp.values())
print (emp.items())
print(emp.get('exp'))

# getting the values in for loop 

for i in emp:
    print ("value of i:",emp[i])
    print (i ,":", emp[i])
for x in emp.values():
  
    print ( "only the value using looping" ,x)
for x,y in emp.items():
  
    print ( x, ":",y)
 # to update the particauar values
emp["Salary"]=200
print("To update the salary",emp.get('Salary'))
   
# if function 
if ("Name") in emp:
    print ("Present")
else:
    print("not present")
emp.update({'Team': 1})
print(emp)
emp.pop('Team')
print(emp)
#emp.clear()
#print (emp)



# nested 
emp1={"em1":{'Name' :'Nave','exp':5,'role': 'Analyst','salary':100},
      "em2":{'Name' :'Nave1','exp':50,'role': 'Analyst1','salary':1000}}
#print (emp1)
for x,y in emp1.items():

