import json
import re
import datetime

toDay = datetime.datetime.now()
print(toDay.time() )
print(toDay.strftime("%A"))
# Define the fields of a past transaction
transDict = [{'date': 'today', 'entity': 'All Trades', 'catagory': 'Dougs pay', 'rule': 'every 2 weeks', 'amount': 500 }]
assoc = [{'text piece': 'grease monkey', 'catagory': 'transportation car maintenance'}]
	
def getStrTransPiece(bigStr,smallStr,delim):
	#if start of return string if not found with index to occurance of smallString then return null
	i = bigStr.find(smallStr)
	if i < 0:
		return None
	# if final delimiter is not found then return null othewise return the string piece
	rtnStr = bigStr[ i: ]
	i = rtnStr.find(delim)
	if i < 0:	
		return None
	else:
		i -= 1
		rtnStr = rtnStr[ :i ]
		return rtnStr
# creating list       
transactions= [] 
monthTrans = []
associations = []
again = "yes"

global choice
global tFileName

# main loop
while again == "yes":
	menu = ["\nMenu", "1. Parse raw financial data to transaction lines and save in file", "2. Create transaction and catagory associations file", "3. Organize transactions using associations file and user entry", "9. Quit."]
	for x in menu:
		print(x)
	choice = input("Choose one:")	
	if choice == "1":
		#Get name of raw data file from user
		rawFile = input("\nEnter file to load:")	
		
		#Open WellsFargo file for read, load  and print
		f = open(rawFile, "r")
		rData = f.read()
		f.close()
		#print(rData)	
		print("\n Raw data file has been loaded from " + rawFile + "...")
		print("Extracting transactions from text data...")
		#Parse raw data to a trimmed, sorted list of dictionary transaction records
		matches = re.findall("(\d+/\d+/\d+\t[^\t]+\s[^\n]+\n)", rData) 
		matches.sort()
		#first get all the records
		for x in matches:
			z = x.strip("\n")
			y = z.split("\t")
			print( y )	
			transDict = {'date': y[0], 'descript': y[1], 'catagory': "undecided", 'rule': "undecided", 'debit': y[2 ],'credit': y[3], 'balance': y[4]} 			
			transactions.append( transDict )
		
		#Get name of raw data file from user
		rawFile = input("\nEnter 2nd file to load:")	
		
		#Open Discover file for read, load  and print
		f = open(rawFile, "r")
		rData = f.read()
		f.close()
		#print(rData)	
		print("\n Raw data file has been loaded from " + rawFile + "...")
		
		#get the year from the current date
		x = re.search(r"Recent Activity \(... .., ....", rData)
		print(x)
		print("Extracting transactions from text data...")
		#Parse raw data to a trimmed, sorted list of dictionary transaction records
		matches = re.findall("\n...\n...\s\d+\nMerchant name is\n[^\n]+\nMerchant category is\n[^\n]+\nAmount is\n[^\n]+\n", rData) 
		#print(matches)
		#matches.sort()
		#first get all the records
		for x in matches:
			#z = x.strip("\n")
			y = x.split("\n")
			print( y )	
			#transDict = {'date': y[0], 'descript': y[1], 'catagory': "undecided", 'rule': "undecided", 'debit': y[2 ],'credit': y[3], 'balance': y[4]} 			
			#transactions.append( transDict )

		#Get name of raw data file from user for Quick Silver
		rawFile = input("\nEnter file to load:")	
		
		#Open WellsFargo file for read, load  and print
		f = open(rawFile, "r")
		rData = f.read()
		f.close()
		#print(rData)	
		print("\n Raw data file has been loaded from " + rawFile + "...")
		print("Extracting transactions from text data...")
		#Parse raw data to a trimmed, sorted list of dictionary transaction records
		matches = re.findall("(\d+/\d+/\d+\t[^\t]+\s[^\n]+\n)", rData) 
		matches.sort()
		#first get all the records
		for x in matches:
			z = x.strip("\n")
			y = z.split("\t")
			print( y )	
			transDict = {'date': y[0], 'descript': y[1], 'catagory': "undecided", 'rule': "undecided", 'debit': y[2 ],'credit': y[3], 'balance': y[4]} 			
			transactions.append( transDict )

		print( "The transactions have been extracted...")
		print( "The start and stop dates are " + transactions[0]["date"]  + " to " +  transactions[-1]["date"] + "." )
		toDay = datetime.datetime.today()
		print ( "The day and time is " , end = " ")
		print( toDay )
		
		startDay = input("Enter the transactions starting day (mm/dd/yy):  ") 	
		endDay = input("Enter the transactions ending day (mm/dd/yy): ")
	
		#if start is less than ending day then put them in monthTrans
		if startDay < endDay:
			for x in transactions:
				if (x["date"] >= startDay and x["date"] <= endDay ):
					monthTrans.append(x)
			print("\n uncatagorized transactions for month created, time to save them.. ")

			#save the transactions in a file
		tFileName = input("\nWhat is the file name to save to of the uncatagorized transactions?")
		with open(tFileName, 'w') as json_file:
			json.dump(monthTrans, json_file)
		print("\nUncatagorized transactions saved to " + tFileName + "...")

	elif choice == "2":
		#Load catagories from a json file
		tFileName = input("\nEnter the catagory file name that you will load from?")			
		with open(tFileName, 'r') as f:
			catagories = json.load(f)
		print("\nCatagories loaded to use from " + tFileName + "...")

		#load transactions for days specified
		tFileName = input("\nEnter the month transactions file name that you will load from?")			
		with open(tFileName, 'r') as f:
  			monthTrans = json.load(f)
		print("\nUncatagorized transaction loaded from " + tFileName + "...")
		
		#load associations file
		aFileName = input("\nEnter the associations file name that you will load from?")			
		with open(aFileName, 'r') as f:
			associations = json.load(f)
		print("\nAssociations loaded from " + aFileName + "...")
		print("...")
		print(monthTrans)
		ai = 0
		i = 0
		done = 0

		for x in monthTrans:
			moreAssoc = 1
			#display current transactions
			print(str(i), end = "= " )
			print( x )
			if i % 10 == 0 and i > 0:
				while done == 0 and moreAssoc == 1:
					#display catagories
					print("\n Catagories: ")
					ic = 0 #iterator for catagories
					for y in catagories:
						print ( str(ic) + " = " + y , end = "\t" )
						if ic % 4   == 0  and ic > 0 :
							print(" ")
						ic += 1
					print("\n\n Associations: ")
					print(associations)
					
					#keep gettin input til 'c' is entered then print next 10
					while moreAssoc == 1:
						answer1 = input("\nEnter a some text (c to continue, q to quit):")
						if answer1 == "c":
							i += 1
							moreAssoc = 0
							
						elif answer1 == "q":
							done = 1
							break
						else:
							answer2 = input("Enter the number for the catagory for the association file: ")
							assoc = [{'text piece': answer1, 'catagory': catagories[int(answer2)] }]
							associations.append(assoc)
			i += 1
			if done == 1:
				break
		print("\n Done with associations file <" + aFileName + ">")
		print("saving associations to file...")

		#Save associations to a file
		with open(aFileName, 'w') as json_file:
			json.dump(associations, json_file)
			print("\nTransactions to catagory associations saved in " + aFileName)

	elif choice == "3":

		#Load catagories from a json file
		tFileName = input("\nEnter the catagory file name that you will load from?")			
		with open(tFileName, 'r') as f:
			catagories = json.load(f)
		print("\nCatagories loaded to use from " + tFileName + "...")

		#load transactions for days specified
		tFileName = input("\nEnter the month transactions file name that you will load from?")			
		with open(tFileName, 'r') as f:
  			monthTrans = json.load(f)
		print("\nUncatagorized transaction loaded from " + tFileName + "...")
		
		#load associations file
		tFileName = input("\nEnter the associations file name that you will load from?")			
		with open(tFileName, 'r') as f:
  			associations = json.load(f)
		print("\nAssociations loaded from " + tFileName + "...")
		
		#go through each record of monthTrans and add a catagory
		i = 0
		for x in monthTrans:	
			#display current transactions
			print("\n\n\nHere is transaction #" + str(i) )
			ii=0
			for y in associations:
				print (y)          
				n = x["descript"]
				md = y["text piece"]
				if n.find(md) > -1:
					x["catagory"] = y["catagory"]
					print("the catagory for transaction #" + str(i) + " is "  + y["catagory"])
					i += 1
					continue
				ii += 1
			#display catagories
			print("\nHere are the catagories: ")
			ic = 0 #iterator for catagories
			for y in catagories:
				print ( str(ic) + " = " + y , end = "\-t" )
				if ic % 4   == 0  and ic > 0 :
					print(" ")
				ic += 1
									
			ii = input("\nWhich catagory number do you choose? \n (# = choose, q = quit, d = delete record, s= split to 2, enter = accept current record)")
			if  ii.isnumeric():
				x["catagory"] = catagories[ int( ii ) ]
			elif ii == "q":
				break
			if len(ii) == 0:
				i += 1
				continue
			elif ii == "d":
				#delete current record
				monthTrans.pop( i ) 
				print("\nrecord " + str( i ) + " deleted...")
				continue
					
			elif ii == "s":
				#split record into 2 records
				cat1 = input("Input number for catagory of 1st record:")
				cat2 = input("Input number for catagory of 2nd record:")
				amnt1 = input("Input amount for first catagory:")
				amnt2 = input("Input amount for 2nd catagory:")
				transDict = x 			
				if x["debit"] == "":
					transDict["credit"] = amnt1
					x["credit"] = amnt2
				else:
					transDict["debit"] = amnt1
					x["debit"] = amnt2
				transDict ["catagory"] = catagories[int(cat1)]
				x["catagory"] = catagories[int(cat2)]
				monthTrans.insert(i,transDict)
			else:
				#continue
				print("Back to consecutive transaction updating")							
			i += 1

		#Save catagorized transactions to a file
		with open(tFileName, 'w') as json_file:
 			json.dump(monthTrans, json_file)
		print("\ncatagorized transactions saved in " + tFileName)

	elif choice == "4":
		tFileName = input("\nEnter the pay plan file name that you will load from?")			
		with open(tFileName, 'r') as f:
  			payPlan = json.load(f)
		#add rules
		print("\nHere are the pay plan rules: ")
		ir = 0 #iterator for rules
		for z in payPlan:
			print ( str(ir) + " = " + z , end = "\t" )
			if ir % 4   == 0  and ir > 0 :
				print("\n" )
				ir += 1
			ii = input("\nWhich pay plan rule number do you choose?")
			z["rule"] = payPlan[ int( ii ) ]

	elif choice == "5":
		
		#Save catagorized transactions to a file
		tFileName = input("\nWhat is the file name of the transactions?")
		with open(tFileName, 'w') as json_file:
 			json.dump(monthTrans, json_file)
		print("\ncatagorized transactions saved in " + tFileName)
		

	elif choice == "6":
		print("\ntransactions...")
		for x in transactions:
			print( x )
				
	else:
		again = "no"
	
print("adios!")	