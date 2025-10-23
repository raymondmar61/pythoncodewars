#https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
'''
Directions Reduction 5kyu

Once upon a time, on a way through the old wild mountainous west, a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.

The directions given to the man are, for example, the following (depending on the language):  ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]

You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:
["WEST"]
or
{ "WEST" }
or
[West]

Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
The OCaml version takes a list of type direction = | North | South | East | West.

See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.
'''
def dir_reduc(arr):
    path = arr
    answer = []
    if len(path) == 0:
        pass
    else:
        answer.insert(0, path[0])
        numberofdirections = len(path)
        for i in range(1, numberofdirections):
            answerlistlength = len(answer)
            if answerlistlength == 0:
                pass
            else:
                previouspresentdirection = answer[-1]
            presentdirection = path[i]
            answer.append(presentdirection)
            answerlistlength = len(answer)
            if len(answer) == 1:
                pass
            elif (presentdirection == "SOUTH" and previouspresentdirection == "NORTH") or (presentdirection == "NORTH" and previouspresentdirection == "SOUTH") or (presentdirection == "EAST" and previouspresentdirection == "WEST") or (presentdirection == "WEST" and previouspresentdirection == "EAST"):
                del answer[-1]
                del answer[-1]
    return answer


print(dir_reduc(["NORTH", "SOUTH", "SOUTH"])) #answer ['SOUTH']
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) #answer ['WEST']
print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])) #answer ['NORTH', 'WEST', 'SOUTH', 'EAST']
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) #answer ['WEST']
print(dir_reduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST", "EAST"])) #answer ['NORTH', 'NORTH']
print(dir_reduc([])) #answer []
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"])) #answer []
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"])) #answer ['NORTH']
print(dir_reduc(["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"])) #answer ['EAST', 'NORTH']
print(dir_reduc(["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"])) #answer ['NORTH', 'EAST']
print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])) #answer ['NORTH', 'WEST', 'SOUTH', 'EAST']
print(dir_reduc(['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH'])) #answer ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']

path = ["NORTH", "SOUTH", "SOUTH"] #answer ['SOUTH']
answer = []
if len(path) == 0:
    print(path)
else:
    answer.insert(0, path[0])
    print(path)
    numberofdirections = len(path)
    for i in range(1, numberofdirections):
        answerlistlength = len(answer)
        print(f"i={i}")
        print(f"answer list: {answer}")
        print(f"answer list length: {answerlistlength}")
        if answerlistlength == 0:
            print("love1")
            pass
        else:
            previouspresentdirection = answer[-1]
        presentdirection = path[i]
        answer.append(presentdirection)
        answerlistlength = len(answer)
        print("\n")
        print(f"path[{i}]: {path[i]}")
        print(f"answer list: {answer}")
        print(f"answer list length: {answerlistlength}")
        # print(f"answer[length]: {answer[len(answer)]}")
        print(f"presentdirection: {presentdirection}")
        print(f"previouspresentdirection: {previouspresentdirection}")
        if len(answer) == 1:
            print("love2")
        elif (presentdirection == "SOUTH" and previouspresentdirection == "NORTH") or (presentdirection == "NORTH" and previouspresentdirection == "SOUTH") or (presentdirection == "EAST" and previouspresentdirection == "WEST") or (presentdirection == "WEST" and previouspresentdirection == "EAST"):
            # print(f"delete: {answer[-1]} {answer[i-1]}")
            print(f"delete: {answer[-1]}")
            del answer[-1]
            print(f"delete: {answer[-1]}")
            del answer[-1]
    print(f"final answer list: {answer}")
    '''
    ['NORTH', 'SOUTH', 'SOUTH']
    i=1
    answer list: ['NORTH']
    answer list length: 1


    path[1]: SOUTH
    answer list: ['NORTH', 'SOUTH']
    answer list length: 2
    presentdirection: SOUTH
    previouspresentdirection: NORTH
    delete: SOUTH
    delete: NORTH
    i=2
    answer list: []
    answer list length: 0
    love1


    path[2]: SOUTH
    answer list: ['SOUTH']
    answer list length: 1
    presentdirection: SOUTH
    previouspresentdirection: NORTH
    love2
    final answer list: ['SOUTH']
    '''

#Test cases submitted by other programmers
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

#Test cases submitted by other programmers
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

#Test cases submitted by other programmers
def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]

    for i in range(len(arr) - 1):
        if set(arr[i:i + 2]) in opposites:
            del arr[i:i + 2]
            return dirReduc(arr)

    return arr


#Previous Python code trial and error
'''
path = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
answer = []
answer[0] = path[0]
if len(path) == 1:
    answer = path
else:
    for i in range(1, len(path)):
        presentdirection = path[i]
        if (presentdirection == "SOUTH" and path[i - 1] == "NORTH") or (presentdirection == "NORTH" and path[i - 1] == "SOUTH") or (presentdirection == "EAST" and path[i - 1] == "WEST") or (presentdirection == "WEST" and path[i - 1] == "EAST"):
            del path[i]
            del path[i - 1]
'''

# numberofdirectionssemifinal = len(answer)
# for i in range(1, numberofdirectionssemifinal):
#     if len(answer) == 1:
#         break
#     print(f"answer[{i}]: {answer[i]}")
#     presentdirection = answer[i]
#     if (presentdirection == "SOUTH" and answer[i - 1] == "NORTH") or (presentdirection == "NORTH" and answer[i - 1] == "SOUTH") or (presentdirection == "EAST" and answer[i - 1] == "WEST") or (presentdirection == "WEST" and answer[i - 1] == "EAST"):
#         print(f"delete: {answer[i]} {answer[i - 1]}")
#         del answer[i]
#         del answer[i - 1]
# print(answer)

'''
path = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(path) #print ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
del path[-1]
print(path) #print ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']
print(len(path)) #print 6
lengthremain = len(path)
print(lengthremain) #print 6
del path[lengthremain - 1]
print(path) #print ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST']
'''
