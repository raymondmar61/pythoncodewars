#https://www.codewars.com/kata/5672a98bdbdd995fad00000f/python
'''
Rock Paper Scissors! 8kyu

Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''
def rps(p1, p2):
    p1p2outcome = p1 + p2
    rpsdictionary = {"rockscissors": "Player 1 won!", "paperrock": "Player 1 won!", "scissorspaper": "Player 1 won!", "scissorsrock": "Player 2 won!", "rockpaper": "Player 2 won!", "paperscissors": "Player 2 won!", "rockrock": "Draw!", "paperpaper": "Draw!", "scissorsscissors": "Draw!"}
    return rpsdictionary[p1p2outcome]


print(rps("scissors", "paper")) #print Player 1 won!
print(rps("scissors", "rock")) #print Player 2 won!
print(rps("paper", "paper")) #print Draw!