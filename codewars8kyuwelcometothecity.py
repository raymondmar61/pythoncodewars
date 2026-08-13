#https://www.codewars.com/kata/5302d846be2a9189af0001e4/train/python
'''
Welcome to the City 8 kyu

Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!
'''
def say_hello(name, city, state):
    fullname = (" ".join(name))
    return f"Hello, {fullname}! Welcome to {city}, {state}!"


print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')) #print Hello, John Smith! Welcome to Phoenix, Arizona!'
print(say_hello(['Franklin', 'Delano', 'Roosevelt'], 'Chicago', 'Illinois')) #print Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!'
print(say_hello(['Wallace', 'Russel', 'Osbourne'], 'Albany', 'New York')) #print Hello, Wallace Russel Osbourne! Welcome to Albany, New York!'
print(say_hello(['Lupin', 'the', 'Third'], 'Los Angeles', 'California')) #print Hello, Lupin the Third! Welcome to Los Angeles, California!'
print(say_hello(['Marlo', 'Stanfield'], 'Baltimore', 'Maryland')) #print Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!'

inputarray = (['Franklin', 'Delano', 'Roosevelt'], 'Chicago', 'Illinois')
inputarray = (['John', 'Smith'], 'Phoenix', 'Arizona')
print(inputarray) #print (['John', 'Smith'], 'Phoenix', 'Arizona')
print(inputarray[0]) #print ['John', 'Smith']
print(" ".join(inputarray[0])) #print John Smith
fullname = (" ".join(inputarray[0]))
print(f"Hello, {fullname}! Welcome to {inputarray[1]}, {inputarray[2]}!") #Hello, John Smith! Welcome to Phoenix, Arizona!
