import random

user_wins = 0
computer_wins = 0

while user_wins<3 and computer_wins<3;

	user_choice = raw_input("Rock, paper, or scissors?")

	computer_choice = random.randint(1,3)

	computer_word = " "
	if computer_choice == 1;
		computer_word = "rock"
	elif computer_choice == 2;
		computer_word = "paper"
	elif computer_choice == 3;
		computer_word = "scissors"

	if user_choice == "rock" and computer_word == "paper";
		print("computer wins")
		computer_wins = computer_wins + 1
	elif user_choice == "rock" and computer_word == "rock";
		print("tie")
	elif user_choice == "rock" and computer_word == "scissors";
		print("user wins")
		user_wins = user_wins + 1
	if user_choice == "paper" and computer_word == "paper";
		print("tie")
	elif user_choice == "paper" and computer_word == "rock";
		print("user wins")
		user_wins = user_wins + 1
	elif user_choice == "paper" and computer_word == "scissors";
		print("computer wins")
		computer_wins = computer_wins + 1
	if user_choice == "scissors" and computer_word == "paper";
		print("user wins")
		user_wins = user_wins + 1
	elif user_choice == "scissors" and computer_word == "rock";
		print("computer wins")
		computer_wins = computer_wins + 1
	elif user_choice == "scissors" and computer_word == "scissors";
		print("tie")