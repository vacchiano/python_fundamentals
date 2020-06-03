# Numero Uno

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

# Numero Dos
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
iterateDictionary(students) 

# eachStudent = my_dict.items()
# print(eachStudent)