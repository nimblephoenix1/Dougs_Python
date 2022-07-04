import json

# Define the fields of a past transaction
transDict = [{'date': 'today', 'entity': 'All Trades', 'catagory': 'Dougs pay', 'amount': 500 }]

		
   
# creating list       
transaction= [] 
global again
again = "yes"
global choice
global tFileName

# main loop
while again == "yes":
	menu = ["\nMenu", "1. List records.", "2. Add records.", "3. Delete a record.", "4. Save records.", "5. Load records.", "6. Quit."]
	for x in menu:
		print(x)
	choice = input("Choose one:")	
	if choice == "1":
		print("\nDate", "With", "Catagory", "Amount" ) 

		# show records
		iter=0
		for x in transaction:
			print(iter, x['date'], x['entity'], x['catagory'], x['amount'])
			iter += 1
	elif choice == "2":
		#Enter transactions
		a = "loop"
		while a == "loop":
			tDate = input("\nEnter date:")
			tEntity = input("Enter with:")
			tCatag = input("Enter catagory:")
			tAmount = input("Enter amount:")
			transDict = {'date':tDate, 'entity':tEntity, 'catagory':tCatag, 'amount':tAmount } 
			transaction.append( transDict )
			print("transaction entered...");
			userInput = input("Enter another (Y/N)?")
			if userInput == "N":
				a = " stop"

	elif choice == "3":
		ch = input("\nChoose record to delete(0 indexed)->")
		num = int(ch)
		transaction.pop(num)
		print("record has been deleted...")

	elif choice == "4":
		#Save transactions to a file
		tFileName = input("\nWhat is the file name?")
		with open(tFileName, 'w') as json_file:
 			json.dump(transaction, json_file)
		print("\ntransactions saved in " + tFileName)

	elif choice == "5":
		#Load transactions from a json file
		tFileName = input("\nEnter the file name that you will load from?")			
		with open(tFileName, 'r') as f:
  			transaction = json.load(f)
	else:
		again = "no"
	
print("adios!")	
