"""
Mutations
"""
from copy import copy, deepcopy


if __name__ == "__main__":
    # indexed reassignment
    my_precalc_grades = [91, 87, 41]  # instantiating a list object
    my_precalc_grades[2] = 65         # indexed assignment

    print("Indexed reassignment:", my_precalc_grades)  # [91, 87, 65]


    # append
    brit_pop = ["Oasis", "Blur"]  # instantiating a list object
    brit_pop.append("Pulp")       # appending a new str object to it

    print("Append:", brit_pop)  # ['Oasis', 'Blur', 'Pulp']


    # insert
    brit_pop.insert(2, "Suade") # "Suade" becomes the 2nd element, pushing "Pulp" to the 3rd index

    print("Insert:", brit_pop)  # ['Oasis', 'Blur', 'Suade', 'Pulp']


    # pop
    outlier = brit_pop.pop(2)  # removes the 2nd element and returns it

    print("Pop:", outlier)      # Suade
    print("Pop:", brit_pop)     # ['Oasis', 'Blur', 'Pulp']


    # reverse
    brit_pop.reverse()  # reverses the order of the elements in the list

    print("Reverse:", brit_pop)  # ['Pulp', 'Blur', 'Oasis']


    # sort
    brit_pop.sort()  # sorts the elements in the list

    print("Sort:", brit_pop)  # ['Blur', 'Oasis', 'Pulp']

    # sort() method does not work with lists that contain elements of different types
    # lst = [1, 2, "3"]
    # lst.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'


    # extend
    brit_pop.extend(["The Verve", "Radiohead"])  # extends the list with the elements of another list

    print("Extend:", brit_pop)  # ['Blur', 'Oasis', 'Pulp', 'The Verve', 'Radiohead']


    # += operator
    brit_pop += ["The Stone Roses", "The Smiths"]  # same as extend

    print("+= operator:", brit_pop)  # ['Blur', 'Oasis', 'Pulp', 'The Verve', 'Radiohead', 'The Stone Roses', 'The Smiths']


    """
    Creating a new list object
    """
    # list literal
    six_moral_tales = ["The Bakery Girl", "Suzanne's Career", "My Night at Maud's"]


    # list constructor
    six_moral_tales = list(("The Bakery Girl", "Suzanne's Career", "My Night at Maud's"))  # same as above


    # the copy() function
    french_films = copy(six_moral_tales)  # creates a new list object with the same elements

    print("Copy:", french_films)  # ['The Bakery Girl', "Suzanne's Career", "My Night at Maud's"]


    # the deepcopy() function
    french_films = deepcopy(six_moral_tales)  # creates a new list object with the same elements

    print("Deepcopy:", french_films)  # ['The Bakery Girl", "Suzanne's Career", "My Night at Maud's"]


    # list concatenation
    french_films = six_moral_tales + ["La Collectionneuse", "Claire's Knee", "Love in the Afternoon"]

    print("Concatenation:", french_films)  # ['The Bakery Girl', "Suzanne's Career", "My Night at Maud's", 'La Collectionneuse', "Claire's Knee", 'Love in the Afternoon']


    # list repetition
    french_films = six_moral_tales * 2

    print("Repetition:", french_film)  # ["The Bakery Girl", "Suzanne's Career", "My Night at Maud's", "The Bakery", "Suzanne's Career", "My Night at Maud's"]


    # list slicing
    french_films = six_moral_tales[1:]  # creates a new list object with the elements starting from the 2nd index

    print("Slicing:", french_films)  # ["Suzanne's Career", "My Night at Maud's"]


    # list comprehension
    french_films = [film for film in six_moral_tales]  # creates a new list object with the same elements

    print("List comprehension:", french_films)  # ["The Bakery Girl", "Suzanne's Career", "My Night at Maud's"]