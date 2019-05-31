#https://www.codewars.com/kata/statistics-for-an-athletic-association
'''
You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. There are no traps in this format.

To compare the results of the teams you are asked for giving three statistics; range, average and median.

Range: difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.
Mean or Average: To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.
Median: In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above, the string result will be "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34" of the form:  "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"  where hh, mm, ss are integers (represented by strings) with each 2 digits.

Remarks:  If a result in seconds is ab.xy... it will be given truncated as ab.  If the given string is "" you will return ""
'''
#Sources:  https://stackoverflow.com/questions/38555327/extract-hours-and-minutes-from-string-python, https://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times, https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings

times = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17, 21|8|55.23"
timeslist = times.split(", ")
print(timeslist) #print ['01|15|59', '1|47|6', '01|17|20', '1|32|34', '2|3|17']

from datetime import datetime
from statistics import mean, median
def functionname(times):
	if times == "":
		return ""
	timeslist = times.split(", ")
	#Convert list to time
	timemathlist = []
	for eachreadytimeslist in timeslist:
		microsecondsperiod = eachreadytimeslist.find(".")
		if microsecondsperiod > 0:
			eachreadytimeslist = eachreadytimeslist[0:microsecondsperiod]
		print(eachreadytimeslist)
		time = datetime.strptime(eachreadytimeslist,"%H|%M|%S").strftime("%H|%M|%S")		
		timemathlist.append(time)
	#Convert list to time in seconds
	timelistinseconds = list(map(lambda s: int(s[6:8]) + 60*(int(s[3:5]) + 60*int(s[0:2])), timemathlist))
	#Calculate range
	s1 = min(timemathlist)
	s2 = max(timemathlist)
	formatrangetime = '%H|%M|%S'
	calculaterangetime = datetime.strptime(s2, formatrangetime) - datetime.strptime(s1, formatrangetime)
	calculaterangetimeproper = datetime.strptime(str(calculaterangetime),"%H:%M:%S").strftime("%H|%M|%S")  #RM:  convert calculaterangetime as datetime to string to manipulate time as string
	rangetime = ("Range: "+calculaterangetimeproper)
	#Calculate average
	average = sum(timelistinseconds)/len(timelistinseconds)
	bigmins, secs = divmod(average, 60)
	hours, mins = divmod(bigmins, 60)
	averagetime = ("Average: "+"%02d|%02d|%02d" % (hours, mins, secs))
	#Calculate median
	calculatemedian = median(timelistinseconds)
	bigmins, secs = divmod(calculatemedian, 60)
	hours, mins = divmod(bigmins, 60)
	mediantime = ("Median: "+"%02d|%02d|%02d" % (hours, mins, secs))
	#Range: 00|47|18 Average: 01|35|15 Median: 01|32|34	
	teamresults = rangetime+" "+averagetime+" "+mediantime
	return teamresults
print(functionname(times))
print(functionname(""))

"""
timemathlist = []
from datetime import datetime
from statistics import mean, median
for eachreadytimeslist in timeslist:
	time = datetime.strptime(eachreadytimeslist,"%H|%M|%S").strftime("%H|%M|%S")
	#print(time)
	timemathlist.append(time)
print("Convert list to time",timemathlist) #print Convert list to time ['01|15|59', '01|47|06', '01|17|20', '01|32|34', '02|03|17']
time_list = list(map(lambda s: int(s[6:8]) + 60*(int(s[3:5]) + 60*int(s[0:2])), timemathlist))
print("Convert list to time in seconds",time_list) #print Convert list to time in seconds [4559, 6426, 4640, 5554, 7397]
average = sum(time_list)/len(time_list)
bigmins, secs = divmod(average, 60)
hours, mins = divmod(bigmins, 60)
print("Average "+"%02d|%02d|%02d" % (hours, mins, secs)) #print Average 01|35|15
s1 = min(timemathlist)
s2 = max(timemathlist)
FMT = '%H|%M|%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta) #print 0:47:18
print(type(tdelta)) #print <class 'datetime.timedelta'>
tdeltaproper = datetime.strptime(str(tdelta),"%H:%M:%S").strftime("%H|%M|%S")  #RM:  convert tdelta as datetime to string to manipulate time as string
print("Range "+tdeltaproper) #print Range 00|47|18
list3 = [4559, 6426, 4640, 5554, 7397]
print(median(list3))
mediantime = median(list3)
bigmins, secs = divmod(mediantime, 60)
hours, mins = divmod(bigmins, 60)
print("Median "+"%02d|%02d|%02d" % (hours, mins, secs)) #print Median 01|32|34
"""

stringlove = "search.53"
print(stringlove.find("."))

# import time
# start = "00:00:00".time()
# done = "30:15:20".time()
# elapsed = done - start
# print(elapsed)