#https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
'''
Total amount of points 8kyu

Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)

We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
'''
def points(games):
    points = 0
    for eachgames in games:
        xscore = int(eachgames.split(":")[0])
        yscore = int(eachgames.split(":")[1])
        if xscore > yscore:
            points = points + 3
        elif xscore == yscore:
            points = points + 1
    return points


print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])) #print 30
print(points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4'])) #print 10
print(points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4'])) #print 0
print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4'])) #print 15
print(points(['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4'])) #print 12


footballteamlist = ["3:1", "2:2", "0:1"]
points = 0
for eachfootballteamlist in footballteamlist:
    print(eachfootballteamlist)
    print(eachfootballteamlist.split(":"))
    xscore = int(eachfootballteamlist.split(":")[0])
    yscore = int(eachfootballteamlist.split(":")[1])
    print(xscore)
    print(yscore)
    if xscore > yscore:
        points = points + 3
    elif xscore == yscore:
        points + points + 1
    else:
        print("error")
print(points)
'''
3: 1
['3', '1']
3
1
2: 2
['2', '2']
2
2
0: 1
['0', '1']
0
1
error
3
'''
