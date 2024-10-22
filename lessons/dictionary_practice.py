"""examples of dictionary syntax with ice cream ship order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
# len evaluates to noumber of key-value entries
print(f"{len(ice_cream)}flavors")
# add key value using subsciption
ice_cream["mint"] = 3
# access values by their key using subscription
print(ice_cream["chocolate"])
# reassing values by their key using assignem.....
ice_cream["vanilla"] += 10
# or
ice_cream["vanilla"] = 28
# remove items by using pop method
ice_cream.pop["strawberry"]
# when you pop something it returns the value and you can store that value
# test if key is in dictionary
has_pbj: bool = "pbj" in ice_cream
# loop through items using for-in loops
# finding total number of orders example
total_orders: int = 0
for flavor in ice_cream:
    print(flavor)
    # loops through keys,not values
    total_orders += ice_cream[flavor]
