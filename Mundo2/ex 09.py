from random import choice
player = str(input('Lets play roshambo, choose rock, paper or scissor: ')).strip().lower()
bot = choice(['rock', 'paper', 'scissor'])
bot_rock = bot == 'rock'
bot_paper = bot == 'paper'
bot_scissor = bot == 'scissor'
player_rock = player == 'rock'
player_paper = player == 'paper'
player_scissor = player == 'scissor'
if bot == player:
    print('We have a draw.')
elif bot_rock and player_paper or bot_paper and player_scissor or bot_scissor and player_rock:
    print('You win, i choose {} and you {}.'.format(bot, player))
elif bot_paper and player_rock or bot_scissor and player_paper or bot_rock and player_scissor:
    print("I win loser, i choose {} and you {}, cry human, i'm bether than you haha.".format(bot, player))
else:
    print("Do you thing that i'm donkey? Don't run away, choose rock, paper or scissor!") 
