def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = 0


# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
#  test that 'strawberries' in new_inventory
print('strawberries' in new_inventory)
#  test that new_inventory['strawberries'] is 10
print(new_inventory['strawberries'] == 10)
add_fruit(new_inventory, 'strawberries', 25)
#  test that new_inventory['strawberries'] is now 35)
print(new_inventory['strawberries'] == 35)
