#https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
'''
Add Length 8 kyu
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element.

Note: String will have at least one element; words will always be separated by a space.
'''
def add_length(str_):
    str_ = str_.split(" ")
    solution = []
    for eachstr_ in str_:
        wordandlength = eachstr_ + " " + str(len(eachstr_))
        solution.append(wordandlength)
    return solution


print(add_length('apple ban')) #print ['apple 5', 'ban 3']
print(add_length('you will win')) #print ['you 3', 'will 4', 'win 3']
print(add_length('you')) #print ['you 3']
print(add_length('y')) #print ['y 1']

sample = "you will win"
samplelist = sample.split(" ")
print(samplelist) #print ['you', 'will', 'win']
solution = []
for eachsamplelist in samplelist:
    print(eachsamplelist, len(eachsamplelist))
    '''
    you 3
    will 4
    win 3
    '''
    wordandlength = eachsamplelist + " " + str(len(eachsamplelist))
    solution.append(wordandlength)
print(solution) #print ['you 3', 'will 4', 'win 3']
