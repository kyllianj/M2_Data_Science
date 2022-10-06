#TSE - M2 SE

#Terminal => jupyter notebook => open fichier ipynb

#Introduction

## Questions ##

#What do you get with t[:-2] and t[-2:]?
t[:-2]
t[-2:]
#An error occur bc t isn't defind

#Define t = (17, 8, 'Hello'), explain what you obtain with min(t).
t = (17, 8, 'Hello')
min(t)
#Again an error bc there is string and integer in the same list

#We can try again this
t[:-2] #We get first element of the list 
t[-2:] #We get the two last element of the list t

#Read the documentation about the function sort. How can we sort a list in decreasing order only using sort?
my_list.sort(reverse = True)

#Create the list [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0] in one line with range objects.
l = list(range(0,6)) + list(reversed(range(5)))
print(l)
#Be careful with a list of lists when you fill its content

## Questions #

#How to test if the content of a string is a number ?
string_1 = 'abcd'
string_2 = '1234'
print(string_1.isnumeric())
print(string_2.isnumeric())

#How to find the last occurence of a substring in a string ?
string_1[-1:]

## Questions ##

#Being given some variable `v`, write a conditional to test if `v `is `None` or not.
v = 1
if v is None:
    print('v is None')
else :
    print("v isn't None")
    
v_bis = None
v_bis is None

#Being given two strings `string_1` and `string_2`, write a conditional to test if they have the same length.
if len(string_1) == len(string_2):
    print ("True")
else :
    print("False")

#For some numeric value `v`, write a `if ... elif ... else` statement that prints different messages according to the positivity, nullity or negativity of `v`.
if v > 0:
    print('v is positive')
elif v == 0:
    print('v is null')
else :
    print('v is negative')
    
## Questions ##

#Write some commands to print the following picture :
*
**
***
****
*****

pic = ''
while True:
    if len(pic) > 5:
        break
    pic += '*'
    print(pic)


#Write some commands to print the following picture :
*
**
***
****
*****
#

pic = ''
while len(pic) < 5:
    if len(pic) == 6:
        break
    pic += '*'
    print(pic)
else : 
    print('#')    



#Write some commands to print the following picture :
    *
   ***
  *****
 *******
*********
    #    

stars = ('    *    ', '   ***', '  *****', ' *******', '*********', '    #')
for i in (0, 1, 2, 3, 4, 5):
    print(stars[i])

#Write some commands to print the following picture :
# # # # #
 # # # #
# # # # #

d = ('# # # # #', ' # # # #')
for i in (0, 1, 0):
    print(d[i])

#Write some commands to print the following picture :
+++++
++++
+++
++
+
++
+++
++++
+++++

cross = ('+++++', '++++', '+++', '++', '+')
for i in (0, 1, 2, 3, 4, 3, 2, 1, 0):
    print(cross[i])

#Write some commands to print the following picture :
+       +
++     ++
+++   +++
++++ ++++
+++++++++

cross = ('+       +', '++     ++', '+++   +++', '++++ ++++', '+++++++++')
for i in (0, 1, 2, 3, 4):
    print(cross[i])

## Questions ##

#Read the documentation about the function `input` we use in the first implementation of `say_hello`.
#With the help of the [documentation](https://docs.python.org/3/library/functions.html), 
# find a built-in function to compute the sum of the numeric items of a list.
#Write a function `draw_pine` that take one integer argument `n` and that draw a pine
# with n levels of characters `*` and a character `#` for the trunk similar to what you did in
# exercises about loops. See below for an example :

draw_pine(4)
*
***
*****
*******
#

def draw_pine(n):
    pine = ('*', '***', '*****', '*******', '#')
    for i in range(0, n+1):
        print(pine[i])
        

draw_pine(4)

#Do the following improvements for the function draw_pine :
    #Properly manage negative value of n or non integer value.
    #Give a default value of 5 to n.
    #Add two arguments leaf and trunk with default values that are supposed to be the characters used to draw the pine. Manage non character values for these arguments.
    #Modify the function to return a string containing the pine in addition to drawing it.
    #Add a boolean argument verbose to print or not the pine with a default value and correct behavior if a non boolean value is given.
    #Document your function.

def draw_pine(n = 5, leaf = '*', trunk = '#'):
    pine = ('*', '***', '*****', '*******', '#')
    n = abs(n)
    n = int(n)
    for i in range(0, n+1):
        print(pine[i])

## Questions ##

#What is returned by the method write ?
!touch my_text_file.txt

f = open('my_text_file.txt', 'w')
print(type(f))
f.close()

f = open('my_text_file.txt', 'r+')
content = f.read()
print(content)

f.write('Hi Pythonista!\n')
#The method write is used to write string in a file


#Understand how the line endings are handled.
# 'w' or 'r+' or 'r'

#Read the documentation about seek. How can you set a position from the end of the file ?
#We can set a position from the end of the file using :
f.seek(2)

#Add an option to your function draw_pine to draw into a file.

#Write a function draw_pine_from_file to draw a pine with options read from a file.

## Questions ##

#Create a class Pet which contains two attributes age and name and a method get_info that returns a string with informations about the pet. You should also provide a proper constructor.
class Pet:
    age = 3
    name = 'Chicken'
    
    def get_info(self):
        return str(name + ', ' + age)
    
    def __init__(self):
        self.n = 5


Pet.age
Pet.name

x = Pet()
print(x.get_info)
print(x.n)

#Derive two classes Cat and Dog from Pet and improve the method get_info in these specific cases.
#Create a custom exception BadPetAge to be raised when an error about the age occurs.
#Enhance the constructor of Pet to raise a BadPetAge if age is negative.
#Add comparison methods to the class Pet to order them according to their age. Here are some example behaviours :
#Example of comparisons
felix = Cat('Felix', 5)
puppy = Dog('Puppy', 3)

felix > puppy # Should return True
puppy > puppy # Should return False
felix <= puppy # Should return False
#Find in the documentation how to allow your class to be used through a context with ... as.



