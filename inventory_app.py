"""Implements household inventory control features."""
import json
import sys

class InventoryApp():
	"""Implements household inventory control features."""

	def __init__(self):
		print("----Welcome to your Home Inventory Application----")
		self.created = False #Boolean value to check and make sure that a dictionary has been created
		self.added_items = False
		self.user_choice()

	def user_choice(self):
		valid_quit_input = False #Validation Check
		while valid_quit_input == False:
			print("--------------------------------------------------")
			print("Use the following commands to utilize its features")
			print("-start\n-read\n-save\n-add_items\n-search\n-display\n-quit")
			choice = input("Please input your command: ")
			print(choice)
			if choice == "start":
				print("Inventory Created")
				self.start_inventory()
			elif choice == "read":
				print("Chose Read")
				self.read_inventory()
			elif choice == "save":
				print("Chose save")
				self.save_inventory()
			elif choice == "add_items":
				print("Chose add_items")
				self.add_items()
			elif choice == "search":
				print("Chose search")
				self.search_inventory()
			elif choice == "display":
				print("Chose display")
				self.display_inventory()
			elif choice == "quit":
				valid_quit_input = True
				print("You have terminated the program")
				break
			else:
				print("That is not a valid, input. Please try to input another command")

	def start_inventory(self): #Creating the dictionary
		title = input("Please input the name of your new inventory: ")
		self.inventories = {}
		self.inventories['title'] = title
		print("Creating Inventory...")
		print(f"Your current dictonary is as follows {self.inventories}")
		self.inventory_dict = {}
		self.inventory_dict['title'] = self.inventories
		self.created = True
		print("Inventory is created")
    
	def print_inventories(self):
		counter = 1
		for i in self.inventories.values():
			print(f"{counter}.{i}")
			counter+=1
		if self.added_items:
			for j in self.inventory_dict['item'].keys():
				print(f"{counter}.{j}")

	def read_inventory(self): #Reading the inventory, which reads what is in the dictionary
		if self.created == True:
			#print(self.inventory_dict)
			self.print_inventories()
			'''
			if 'item' in self.inventory_dict['item'].values():
				for x in self.inventory_dict['item'].values():
					print(x)
			else:
				print('You have not added any items to this inventory')
			'''
		else:
			print("You have not added items into the inventory. Please use the 'add_items' command to add values.")
    

	def save_inventory(self): #Saving the inventory into a json file
		if self.created == True:
			print("Saving the inventory into the json file called inventory.json")
			#js = json.dumps(self.inventory_dict)
			#self.inventory_file = open('inventory.json', 'w')
			#self.inventory_file.write(js)
            #self.inventory_file.close()
			with open('inventory_file.json', 'w') as self.inventory_file:
				#for i in self.inventories:
					#print(i)
				json.dump(self.inventory_dict, self.inventory_file)
			print("Data is saved")
		else:
			print("You have not created the inventory. Please use the 'start' command to create an inventory")


	def add_items(self): #Adding items into the dictionary
		self.added_items = True
		if self.created == True:
			item_dict = {}
			while True:
				key = input("Please input the key for your item: ")
				value = input("Please input the value for your item: ")
				item_dict[key] = value
				self.inventory_dict['item'] = item_dict
				print(item_dict)
				choice = input("To continue entering values press 'c', to quit press 'q'")
				if choice == 'q':
					break
		else:
			print("You have not created the inventory. Please use the 'start' command to create an inventory")

	def search_inventory(self): #Searching the inventory to see if the key value is present in the dictonary
		if self.created == True:
			search_term = input('Please input the keyword you would like to search: ')
			if search_term in self.inventory_dict['item'].keys():
				print("This search term is in the inventory")
			else:
				print("This search term is not in the inventory")
		else:
			print("You have not created the inventory. Please use the 'start' command to create an inventory")

	def display_inventory(self): #Displaying what is present in the json file
		if self.created == True:
			#self.inventory_file = open('inventory_file.json', 'r')
			data = []
			for line in open('inventory_file.json', 'r'):
				data.append(json.loads(line))
			print(data)
			
			#for i in data:
				#print(i)
			self.inventory_file.close()
		else:
			print("You have not created the inventory. Please use the 'start' command to create an inventory")
			
					



		


