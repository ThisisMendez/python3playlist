grades = ['A', 'B', 'F', 'C', 'F', 'A']

def remove_fails(grade):
    return grade != 'F'

print(list(filter(remove_fails, grades)))

#Using ForLoop
filtered_grades =[]
for grade in grades: 
    if grade != 'F':
        filtered_grades.append(grade)
print(filtered_grades)

#Using Comprehension 
print([grade for grade in grades if grade != 'F'])





# Filters gives a easy way to take a collection and filter some of the values from a function result and gives a new filter collection 
#