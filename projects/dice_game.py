# This is a simple dice game where players take turns rolling a six-sided die.
# The first player to reach a score of 20 or more wins the game.
# Each player's score is the sum of their rolls, and they can choose to roll again or hold to keep their current score. 
# If a player rolls a 1, they lose all points for that turn and their turn ends.

import random

# function to simulate rolling a six-sided die
def roll():
	min_value = 1
	max_value = 6
	roll = random.randint(min_value, max_value)
	return roll

# function to get number of players through user input
def getAmountOfPlayers():
	while True:
		number_of_players = input("How many players are playing? ")
		if number_of_players.isdigit():
			number_of_players = int(number_of_players)
			if 2 <= number_of_players <= 4:
				break
			else:
				print("The number of players must be greater than 2 and less than 4.")
		else:
			print("Invalid, try again")
	return number_of_players

# function to play the game
def play_game():
	print("\n" + "="*50)
	print("       Welcome to the Dice Game!")
	print("  First to 30 points wins!")
	print("="*50 + "\n")
	
	# init var
	max_score = 30

	# get number of players
	players = getAmountOfPlayers()

	player_scores = [
		0 for _ in range(players)
	]
	
	while max(player_scores) < max_score:
		for player_index in range(players):
			if max(player_scores) >= max_score:
				break
			print("\n" + "-"*50)
			print(f"🎲 PLAYER {player_index + 1}'S TURN 🎲")
			print("-"*50)
			print(f"Total Score: {player_scores[player_index]} points\n")

			current_score = 0
			while True:
				player_turn = input("Would you like to roll (y)? ")
				if player_turn.lower() != 'y':
					break

				player_value = roll()
				if player_value == 1:
					print("\n❌ OH NO! You rolled a 1! Your turn ends and you lose your points!")
					current_score = 0
					break 
				else:
					current_score += player_value
					print(f"   → You rolled: {player_value}")
				
				print(f"   Round Score: {current_score} points")
		
			player_scores[player_index] += current_score
			print(f"\n✓ Total Score Updated: {player_scores[player_index]} points")
	
	max_score = max(player_scores)
	winning_idx = player_scores.index(max_score)

	print("\n" + "="*50)
	print("🏆 GAME OVER 🏆")
	print("="*50)
	print(f"\n🎉 Player {winning_idx + 1} WINS! 🎉")
	print(f"Final Score: {max_score} points\n")
	print("="*50 + "\n")

play_game()