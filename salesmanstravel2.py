#Examples:  r = "123 Main Street St. Louisville OH 43071, 432 Main Long Road St. Louisville OH 43071, 786 High Street Pollocksville NY 56432"
#travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"
#travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"
#travel(r, "NY 5643") --> "NY 5643:/"
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

def travel(r, zipcode):
	#return :/ if zipcode is null
	if (len(zipcode)) == 0:
		return (":/")
	#return zipcode+":/" if zipcode is invalid
	if (len(zipcode[3:]) < 5):
		return (zipcode+":/")
	#return zipcode+":/" if two digit state is not in the ad
	if zipcode[0:2] not in r:
		return (zipcode+":/")
	#change variable zipcode to returnzipcode
	returnzipcode = zipcode
	adsplit = r.split(",")
	adgroupbylist = []
	for eachadsplit in adsplit:
		#get zip code
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
	#sort adgroupbylist tuple list by state and zip code tuple to groupby
	adgroupbylist.sort(key=lambda x: x[0])
	for key, group in groupby(adgroupbylist, lambda x: x[0]):	
		if key == returnzipcode:
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
			return (key + ":"+adgroupbylistname+"/"+adgroupbylistnumber)

print(travel(ad, "OH 43071"))
print(travel(ad, "NY 56432"))
print(travel(ad, "NY 5643"))
print(travel(ad, "AA 45522"))
print(travel(ad, "EX 34342"))
print(travel(ad, "EX 34345"))
print(travel(ad, "AA 45521"))
print(travel(ad, "AE 56215"))
