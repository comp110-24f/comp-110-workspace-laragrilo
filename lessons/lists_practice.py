# creating lisst
my_numbers: list[float] = []
# lets add ("append") a valie to the end of the list
my_numbers.append(1.5)
print(my_numbers)


# make a lists of numbers
game_points: list[int] = [102, 86, 94]
print(game_points[2])


# indexing
grocery_list: list[str] = ["bananas", "milk", "bread"]
grocery_list[0]
# changing value of an item
grocery_list[1] = "eggs"
print(grocery_list[1])

# changing individual chars in strings? doesn't work
my_name: str = "Lara"
# my_name[3]= "y" doesnt work
name_as_list: list[str] = list(my_name)
print(name_as_list)
name_as_list[2] = "n"
name_as_list.append("e")
print(name_as_list)

# length of list
print(len(grocery_list))

# removing something from list
grocery_list.pop(2)
print(grocery_list)

name_as_list.insert(4, "i")
print(name_as_list)


# comment big code:
# control#?
