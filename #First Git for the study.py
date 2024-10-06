'''
#First Git for the study
#For fucntion
#1 step for function
test_list = ['one', 'two', 'three'] 
for i in test_list: 
     print(i)
# for 'variable' in 'list'
for i in ['one','two','three']:
     print (i)
# it is avaliable put list directly into for list
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
     print(first + last)
# (1,2) -> (first, last)
marks=[80,25,37,90,100]
number = 0
for mark in marks:
     number = number+1
     if mark>= 60:
          print("Student %d is passed." %number)
     else:
          print ("Student %d is failed"%number)
#
marks=[80,25,37,90,100]
number = 0
for mark in marks:
     number = number+1
     if mark<= 60:
          continue
     print("Student %d is passed." %number)
# continue = pass and go to next for loop
add=0
for i in range (1,11):
     add = add + i

print (add)
# range(a,b) - a~(b-1) range object
# range (a) - 0~(a-1)
marks=[80,25,37,90,100]
for number in range(len(marks)):
    if marks[number] < 60:
         continue
    print ("Student %d is passed" %(number+1))
# marks has 5 int
# range (5 = len(marks)) - repeat 0,1,2,3,4 = 5 times & print number +1 for student number
# marks[number] - bring numbers order to range (0,1,2,3,4) and compare with <60
#if the socore is under the 60, it pass and move to next number
for i in range(1,10):
     for j in range(1,10):
          print(i*j, end=" ")
     print(' ')
####### end=" " -> not keep the line / print (' ') change the line\
'''
#list add
# list.append(element) - add element to end of the list
# list.insert(index, element) - add element to location of the list
# list.extend([element, , , ...]) - add many element to end of the list
#list delete
# del list[index] / del list[x:b] delete x~b-1 index
# list.pop(index)
# list.remove(value) delete certain value in the list
# list.clear() delete all element
'''
numbers=[273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number >= 100:
        print(number)
'''
'''
#print over 100

numbers=[273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number%2==0:
       print(number, " is even number")
    else:
       print(number," is odd number")

for number in numbers:
   print(number, "is ",len(str(number))," digit number")

list_of_list=[
   [1,2,3],
   [4,5,6,7],
   [8,9],
]

for i in list_of_list:
   for number in i:
      print (number)

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
   output[(number+(len(output)-1))%len(output)].append(number)
print(output)
'''

#Dictionary
'''
products = [{
    "Name" : "Mango",
    "Price" : 2,
    "Type" : "Food",
},{
    "Name" : "Mango",
    "Price" : 2,
    "Type" : "Food",
}
]
for product in products:
     for key in product:
          print(key)
          print(product[key])
     print("-"*20)
# dictionary["new key"] = new value
# dictionary["old key"] = new value
#del dictionary["key"]
# dictionary.get("not exist key") -> outpur : None

dict_a = {
     "name" : "Cloud"
}
print (dict_a)
del dict_a["name"]
print (dict_a)
'''
pets = [
    {"name": "Cloud", "Age": 5},
    {"name": "Max", "Age": 2},
    {"name": "Coco", "Age": 1},
    {"name": "Taco", "Age": 4},
    {"name": "Bell", "Age": 7}
]

print ("# Lynnwood dogs")
for pet in pets:
    print(pet["name"], pet["Age"])

numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,5,3,4,8,9,7,2,3]
counter={}

for number in numbers:
     value=counter.get(number)
     if value is None:
          counter[number]=0
     counter[number]=counter[number]+1

print (counter)
#
character = {
     "name": "Knight",
     "level": 12,
     "items": {
          "sword": "Fire sword",
          "armor": "Full plate"
     },
     "skill": ["Slash", "Slash hard", "Slash Very hard"]
}
'''
for key in character:
     print(type(character[key]))
     if type(character[key]) is list:
          for detail in character[key]:
               print (key, " : ", detail)
     
     elif type(character[key]) is dict:
          for detail in character[key]:
               print (detail, " : ", character[key][detail])

     else:
          print (key, " : ", character[key])
'''
#for + list
array = [273,32,103,57,52]

for i in range(len(array)):
     print("{}th repeated : {}".format(i,array[i]))

#reverse
for i in range(4,0-1,-1):
     print (i, end="")
#while
i=0
while i < 10:
     print(i)
     i+=1

list_test = [1,2,1,2]
value = 2

while value in list_test:
     list_test.remove(value)

print (list_test)
