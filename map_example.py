def capitalize_and_ascii_sum(word: str):
    return sum(ord(x) for x in word.capitalize())

animals = ['cat', 'dog', 'cow']
#using map
animal_output = list(map(capitalize_and_ascii_sum, animals))
print(animal_output)
    

 #%%
def square(x):
   return x**2
#lambda x: x ** 2

numbers = [1,2,3,4,5]
square = list[map(square, numbers)]
print(numbers)


#%%

def is_even(num):
    return num%2==0

list_1 = [1,2,3,4,5,6,7,8,9,10]

list_2 = filter(is_even, list_1)

print(list(list_2))