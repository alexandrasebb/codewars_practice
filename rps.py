"""
https://www.codewars.com/kata/5672a98bdbdd995fad00000f

Rules of the "Rock, Paper, Scissors" game are:

    Rock beats Scissors,
    Scissors beat Paper,
    Paper beats Rock,
    Two identical moves are a draw.

Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.
Examples:

"scissors",     "paper"     --> "Player 1 won!"
"scissors",     "rock"      --> "Player 2 won!"
"paper",        "paper"     --> "Draw!"

1:2
R:R - Draw      options[0]:option[0]
R:P - 2 wins    options[0]:options[1]
R:S - 1 wins    options[0]:options[2]

P:R - 1 wins    options[1]:options[0]
P:P - Draw      options[1]:option[1]
P:S - 2 wins    options[1]:options[2]

S:R - 2 wins    options[2]:options[0]
S:P - 1 wins    options[2]:options[1]
S:S - Draw      options[2]:option[2]

This solution is so over complicated compared to what was required.

Simple as:
"""
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
"""
player1_input = input(str.capitalize("Player 1 - pick rock, paper or scissors!"))
player2_input = input(str.capitalize("Player 2 - pick rock, paper or scissors!"))

def rps(p1, p2):
    options = ["rock", "paper", "scissors"]

    # check responses
    while p1 not in options:
        print(f"Player 1, please pick from {options}")
        p1 = input("Player 1 - pick rock, paper or scissors!").lower()
    while p2 not in options:
        print(f"Player 2, please pick from {options}")
        p2 = input("Player 2 - pick rock, paper or scissors!").lower()

    if p1 == options[0]:
        if p2 == options[1]:
            return "Player 2 won!"
        elif p2 == options[2]:
            return "Player 1 won!"
        else:
            return "Draw!"

    if p1 == options[1]:
        if p2 == options[2]:
            return "Player 2 won!"
        elif p2 == options[0]:
            return "Player 1 won!"
        else:
            return "Draw!"

    if p1 == options[2]:
        if p2 == options[0]:
            return "Player 2 won!"
        elif p2 == options[1]:
            return "Player 1 won!"
        else:
            return "Draw!"

result = rps(player1_input, player2_input)
print(result)
"""