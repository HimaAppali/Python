# same like arrow functions in JS
people = [
    {'name': 'Hima', 'house':'Jefferson'},
    {'name': 'Rag', 'house':'Jefferson garden'},
    {'name': 'Bindu', 'house':'Jefferson place'}
]

def f(person):
    return person['house']

# to sort based on values that return the above function
people.sort(key=f)

print(people)

# same like arrow functions in JS
# To simply the above process we use lambda functions
people.sort(key=lambda person: person['name'])

print(people)