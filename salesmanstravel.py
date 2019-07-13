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
		#extract zip code, address, and city
		extractzipcode = len(eachadsplit)-5
		zipcode = eachadsplit[extractzipcode:]
		zipcode = zipcode.strip()
		extractaddress = len(eachadsplit)-9
		address = eachadsplit[0:extractaddress]
		extractstatezipcode = len(eachadsplit)-8
		statezipcode = eachadsplit[extractstatezipcode:]
		#create tuple for each address and zip code add to adgroupbylist
		addtoadgroupbylist = (statezipcode, address)
		adgroupbylist.append(addtoadgroupbylist)
	#sort adgroupbylist tuple list to groupby
	adgroupbylist.sort()
	for key, group in groupby(adgroupbylist, lambda x: x[0]):
		#if invalid zip code, then print zipcode:/.  key is state and zip code.
		if (key[0]) == " ":
			print(key[1:]+":/")
		#group by the key state and zip code.  Separate the street address by street number and street name.
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
'''
NY 5643:/
AA 45521:Paris St. Abbeville,Paris bd. Abbeville/67,674
AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670
AE 56210:Main Rd. Bern,Main Al. Bern,Main Rd. Bern/3,320,3200
AE 56215:Main Al. Bern/320
EX 34342:Pussy Cat Rd. Chicago,Pussy Cat Rd. Chicago/10,100
EX 34345:Pussy Cat Rd. Chicago/100
GG 30654:Surta Alley Goodtown,Surta Avenue Goodtown/10,11
GG 30655:Surta Avenue Goodville,Surta Avenue Goodville/11,114
NY 56432:High Street Pollocksville/786
OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432
RE 13000:Gordon St. Atlanta,Gordon St. Atlanta,Gordon Park Atlanta,Gordon St. Atlanta,Gordon Road Atlanta,Gordon Road Atlanta,Gordon St. Atlanta/1,10,14,2,5,58,77
RE 13001:Gordon Road Atlanta/5
RE 13200:Gordon Park Atlanta/14
RE 13222:Gordon St. Atlanta/2
SW 43098:Tokyo Av. Tedmondville,Tokyo Av. Tedmondville/22,2200
SW 43198:Tokyo Av. Tedmondville,Tokyo Av. Tedmondville/2200,2222
ZP 32908:Holy Grail Street Niagara Town,Holy Grail Al. Niagara Town,Holy Grail Street Niagara Town/2,45,54
ZP 32918:Holy Grail Al. Niagara Town/45
'''