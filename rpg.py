import sys
import pprint

def displayInventory(inventory):
	amount = 0
	for key,value in inventory.items():
		print(str(value) + ' ' + key)
		amount += value
	print('Total number of items: ' + str(amount))

def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1

monsterLoot = ['gold coin', 'gold coin', 'shield of endurance', 'health potion', 'mana potion']
inventory = {}
displayInventory(inventory)
addToInventory(inventory, monsterLoot)
displayInventory(inventory)


