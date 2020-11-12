#deriving one list to another using comprehension to shorten filtering or mapping
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

#try writing as a function::::
#def squares(numbers_squared):
#    squaring = [x**2 for x in a]
#    return print(squaring)

#visually nosiy example:::::::::::
squares = map(lambda x: x ** 2, a)

#easier to read then next example:::::::::::::
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

#example using map and filter:::::::::::::::::::::::::::::
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

#Dicitionaires and Sets have their own equivalents of list comprehensions.
#Making it easier for deriative data structure creation. 
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne':3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

#things to remember:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#list comprehensions are clearer than map and filter built in functions
#list comprehnsions allow you to skip items from input list, a behavior map doesn't without help from filter
#dictionaries and sets also support comprehsion expressions.

#avoid more that two expressions in list comprehension
matrix = [[1, 2, 3], [4, 5, 6 ], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

#other practice::::::::::::::::::::::::::::::::::
squared = [[x**2 for x in row] for row in matrix]
print(squared)

my_lists = [
    [[1, 2, 3], [4, 5, 6]], 
    #...
]

flat = [x for sublist1 in my_lists
    for sublist2 in sublist1
    for x in sublist2]
# another version little clearer
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
#List comprehensions also supports multiple if conitions

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x %2 == 0]
c = [x for x in a if x > 4 and x %2 == 0]

#conditions can be specifcied at each level of looping after the for expression. 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
for row in matrix if sum(row) >= 10]
print(filtered)
