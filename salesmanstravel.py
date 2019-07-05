#https://www.codewars.com/kata/56af1a20509ce5b9b000001e/train/python
#6 Kyu earned
#A traveling salesman has to visit clients. He got each client's address e.g. "432 Main Long Road St. Louisville OH 43071" as a list.
#The basic zipcode format usually consists of two capital letters followed by a white space and five digits. The list of clients to visit was given as a string of all addresses, each separated from the others by a comma, e.g.:  "123 Main Street St. Louisville OH 43071, 432 Main Long Road St. Louisville OH 43071, 786 High Street Pollocksville NY 56432".
#To ease his travel he wants to group the list by zipcode.

#Task:  The function travel will take two parameters r (addresses' list of all clients' as a string) and zipcode and returns a string in the following format:  zipcode:street and town,street and town,.../house number,house number,....  The street numbers must be in the same order as the streets where they belong.  If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"

#Examples:  r = "123 Main Street St. Louisville OH 43071, 432 Main Long Road St. Louisville OH 43071, 786 High Street Pollocksville NY 56432"
#travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"
#travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"
#travel(r, "NY 5643") --> "NY 5643:/"

#Note for Elixir:  In Elixir the empty addresses' input is an empty list, not an empty string.
#Note:  You can see a few addresses and zipcodes in the test cases.

#Sources:  Learn https://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby GroupBy.

from itertools import groupby

ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000,786 High Street Pollocksville NY 5643")
ad2 = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")
adsplit = ad.split(",")
#print(adsplit) #print ['123 Main Street St. Louisville OH 43071', '432 Main Long Road St. Louisville OH 43071', '786 High Street Pollocksville NY 56432', '54 Holy Grail Street Niagara Town ZP 32908', '3200 Main Rd. Bern AE 56210', '1 Gordon St. Atlanta RE 13000', '10 Pussy Cat Rd. Chicago EX 34342', '10 Gordon St. Atlanta RE 13000', '58 Gordon Road Atlanta RE 13000', '22 Tokyo Av. Tedmondville SW 43098', '674 Paris bd. Abbeville AA 45521', '10 Surta Alley Goodtown GG 30654', '45 Holy Grail Al. Niagara Town ZP 32908', '320 Main Al. Bern AE 56210', '14 Gordon Park Atlanta RE 13000', '100 Pussy Cat Rd. Chicago EX 34342', '2 Gordon St. Atlanta RE 13000', '5 Gordon Road Atlanta RE 13000', '2200 Tokyo Av. Tedmondville SW 43098', '67 Paris St. Abbeville AA 45521', '11 Surta Avenue Goodtown GG 30654', '45 Holy Grail Al. Niagara Town ZP 32918', '320 Main Al. Bern AE 56215', '14 Gordon Park Atlanta RE 13200', '100 Pussy Cat Rd. Chicago EX 34345', '2 Gordon St. Atlanta RE 13222', '5 Gordon Road Atlanta RE 13001', '2200 Tokyo Av. Tedmondville SW 43198', '67 Paris St. Abbeville AA 45522', '11 Surta Avenue Goodville GG 30655', '2222 Tokyo Av. Tedmondville SW 43198', '670 Paris St. Abbeville AA 45522', '114 Surta Avenue Goodville GG 30655', '2 Holy Grail Street Niagara Town ZP 32908', '3 Main Rd. Bern AE 56210', '77 Gordon St. Atlanta RE 13000']
ad2split = ad2.split(",")
#print(ad2split) #print ['123 Main Street St. Louisville OH 43071', '432 Main Long Road St. Louisville OH 43071', '786 High Street Pollocksville NY 56432', ' 54 Holy Grail Street Niagara Town ZP 32908', '3200 Main Rd. Bern AE 56210', '1 Gordon St. Atlanta RE 13000', ' 10 Pussy Cat Rd. Chicago EX 34342', '10 Gordon St. Atlanta RE 13000', '58 Gordon Road Atlanta RE 13000', ' 22 Tokyo Av. Tedmondville SW 43098', '674 Paris bd. Abbeville AA 45521', '10 Surta Alley Goodtown GG 30654', ' 45 Holy Grail Al. Niagara Town ZP 32908', '320 Main Al. Bern AE 56210', '14 Gordon Park Atlanta RE 13000', ' 100 Pussy Cat Rd. Chicago EX 34342', '2 Gordon St. Atlanta RE 13000', '5 Gordon Road Atlanta RE 13000', ' 2200 Tokyo Av. Tedmondville SW 43098', '67 Paris St. Abbeville AA 45521', '11 Surta Avenue Goodtown GG 30654', ' 45 Holy Grail Al. Niagara Town ZP 32918', '320 Main Al. Bern AE 56215', '14 Gordon Park Atlanta RE 13200', ' 100 Pussy Cat Rd. Chicago EX 34345', '2 Gordon St. Atlanta RE 13222', '5 Gordon Road Atlanta RE 13001', ' 2200 Tokyo Av. Tedmondville SW 43198', '67 Paris St. Abbeville AA 45522', '11 Surta Avenue Goodville GG 30655', ' 2222 Tokyo Av. Tedmondville SW 43198', '670 Paris St. Abbeville AA 45522', '114 Surta Avenue Goodville GG 30655', ' 2 Holy Grail Street Niagara Town ZP 32908', '3 Main Rd. Bern AE 56210', '77 Gordon St. Atlanta RE 13000']

def travelraymondmar(ad):
	adsplit = ad.split(",")
	adgroupbylist = []
	for eachadsplit in adsplit:
		#get zip code
		extractzipcode = len(eachadsplit)-5
		zipcode = eachadsplit[extractzipcode:]
		zipcode = zipcode.strip()
		#check zip code is five digits or not five digits
		if len(zipcode) == 5:
			extractaddress = len(eachadsplit)-9
			address = eachadsplit[0:extractaddress]
			extractstatezipcode = len(eachadsplit)-8
			statezipcode = eachadsplit[extractstatezipcode:]
		else:
			extractaddress = len(eachadsplit)-8
			address = eachadsplit[0:extractaddress]
			extractstatezipcode = len(eachadsplit)-7
			statezipcode = eachadsplit[extractstatezipcode:]
		#create tuple for each address and zip code add to adgroupbylist
		addtoadgroupbylist = (statezipcode, address)
		adgroupbylist.append(addtoadgroupbylist)
	print(adgroupbylist)
	#sort adgroupbylist tuple list to groupby
	adgroupbylist.sort()
	for key, group in groupby(adgroupbylist, lambda x: x[0]):
		#if invalid zip code, then print zipcode:/.  key is state and zip code.
		if len(key[3:]) == 4:
			print(key+":/")
		#group by the key state and zip code.  Separate the street address by street number and street name
		else:
			liststreetnumber = []
			liststreetname = []
			for eachadgroupbylist in group:			
				streetaddress = eachadgroupbylist[1]
				streetnumberextract = streetaddress.find(" ")
				streetnumber = streetaddress[0:streetnumberextract]
				streetname = streetaddress[streetnumberextract+1:]
				liststreetname.append(streetname)
				liststreetnumber.append(streetnumber)
			adgroupbylistnumber = ",".join(liststreetnumber)
			adgroupbylistname = ",".join(liststreetname)
			print(key + ":"+adgroupbylistname+"/"+adgroupbylistnumber)
travelraymondmar(ad)
print("\n")

adgroupbylist = []
for eachadsplit in adsplit:
	print("eachadsplit",eachadsplit)
	extractzipcode = len(eachadsplit)-5
	zipcode = eachadsplit[extractzipcode:]
	zipcode = zipcode.strip()
	print(zipcode)
	print(len(zipcode))
	if len(zipcode) == 5:
		extractaddress = len(eachadsplit)-9
		address = eachadsplit[0:extractaddress]
		print(address)
		extractstatezipcode = len(eachadsplit)-8
		statezipcode = eachadsplit[extractstatezipcode:]
		print(statezipcode)
	else:
		print(len(eachadsplit))
		extractaddress = len(eachadsplit)-8
		address = eachadsplit[0:extractaddress]
		print(address)
		extractstatezipcode = len(eachadsplit)-7
		statezipcode = eachadsplit[extractstatezipcode:]
		print(statezipcode)
	addtoadgroupbylist = (statezipcode, address)
	adgroupbylist.append(addtoadgroupbylist)
print(adgroupbylist)
adgroupbylist.sort()
for key, group in groupby(adgroupbylist, lambda x: x[0]):
	print("key",key)
	if len(key[3:]) == 4:
		print(key+":/")
	else:
		#listofadgroupbylist = ",".join([eachadgroupbylist[1] for eachadgroupbylist in group])
		# listofadgroupbylist = ",".join([eachadgroupbylist[1] for eachadgroupbylist in group])
		# print(key + ":"+listofadgroupbylist)
		lovelistname = []
		lovelistnumber = []
		for eachadgroupbylist in group:			
			streetaddress = eachadgroupbylist[1]
			print(streetaddress)
			streetnumberextract = streetaddress.find(" ")
			streetnumber = streetaddress[0:streetnumberextract]
			#print("streetnumber",streetnumber)
			streetname = streetaddress[streetnumberextract+1:]
			#print("streetname",streetname)
			lovelistname.append(streetname)
			lovelistnumber.append(streetnumber)
		listofadgroupbylistname = ",".join(lovelistname)
		listofadgroupbylistnumber = ",".join(lovelistnumber)
		print(key + ":"+listofadgroupbylistname+"/"+listofadgroupbylistnumber)
space = "3 Main Rd. Bern AE 56210"
print(space.find(" "))

#Examples:  r = "123 Main Street St. Louisville OH 43071, 432 Main Long Road St. Louisville OH 43071, 786 High Street Pollocksville NY 56432"
#travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"
#travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"
#travel(r, "NY 5643") --> "NY 5643:/"

def travel(address, statezipcode):
	zipcodecheck = statezipcode[3:]
	if len(zipcodecheck) != 5:
		print(statezipcode+":/")
		return
	else:
		pass
	print(statezipcode+":rest")
# travel("123 Main Street St. Louisville OH 43071","OH 43071")
# travel("432 Main Long Road St. Louisville OH 43071","OH 43071")
# travel("786 High Street Pollocksville NY 56432","NY 56432")
# travel("786 High Street Pollocksville NY 56432","NY 5643")
# travel(address, statezipcode)

# for eachadsplit in adsplit:
# 	extractaddress = len(eachadsplit)-9
# 	address = eachadsplit[0:extractaddress]
# 	extractstatezipcode = len(eachadsplit)-8
# 	statezipcode = eachadsplit[extractstatezipcode:]
# 	extractzipcode = len(eachadsplit)-5
# 	zipcode = eachadsplit[extractzipcode:]
# 	travel(address, statezipcode)
"""
love = "The quick brown fox"
print(love[-5:]) #print n fox
lovelist = []
blanktuple = (55, 66)
lovelist.append(blanktuple)
blanktuple = (1000, 5066)
lovelist.append(blanktuple)
print(lovelist)

#things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
things = [("vehicle", "speed boat"), ("animal", "duck"), ("plant", "cactus"), ("animal", "bear"), ("vehicle", "school bus")]
print(things)
things.sort()
print(things) #print [('animal', 'bear'), ('animal', 'duck'), ('plant', 'cactus'), ('vehicle', 'school bus'), ('vehicle', 'speed boat')]
for key, group in groupby(things, lambda x: x[0]):
	print("key {}. group{}".format(key, group))
	for thing in group:
		print("thing[0] {}".format(thing[0]))
		print("A {} is a {}".format(thing[1], key))
for key, group in groupby(things, lambda x: x[0]):
	listofthings = " and ".join([thing[1] for thing in group])
	print(key + "s:  "+listofthings+".")
"""
