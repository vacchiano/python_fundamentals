# =============== Numero 1 ==================

# iterate through lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1 change the value 10 in x to 15
# print(x)
# x[1][0] = 15
# print(x)

#2 change last name of the first student from Jordan to Bryant
# print(students)
# students[0]['last_name'] = 'Bryant'
# print(students)

#3 in the sports directory change Messi to Andres
# print(sports_directory)
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

#4 Change value 20 in z to 30
# print(z)
# z[0]['y'] = 30
# print(z)

# =============== Numero 2 ================
# Iterate Through a List of Dictionaries

def iterateDictionary(myList):
    for i in myList:
        print("\n")
        for x,y in i.items():
            print(x,"-",y)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

my_dict = {'first_name':  'Michael', 'last_name' : 'Jordan'}
#iterateDictionary(students) 

# eachStudent = my_dict.items()
# print(eachStudent)

# ========== number 3 ===============
# get values from a list of dictionaries

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

#iterateDictionary2(key_name='last_name', some_list=students)

# ================ Number 4 ============
#Iterate through a dictionary with list values

def printInfo(some_dict):
    for x,y in some_dict.items():
        print(len(y),x.upper())
        for item in y:
            print(item)
        print("") #adds new line between lists

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#printInfo(dojo)