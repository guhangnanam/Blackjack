from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
tie_num = 0
player_win = 0
dealer_win = 0

while game_continue:
    # 1. set up initial message
    game_num += 1
    print(" ")
    print("START GAME #", game_num)
    print(" ")
    player_hand = 0

    # 2. Deal card to the player
    card = rng.next_int(13) + 1
    # use if/elif/else chain
    if card == 1:
        print("Your card is a ACE!")
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a Jack!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10

    player_hand += card
    # print hand value information for player
    print(f"Your hand is: {player_hand}")
    print(" ")

    # 3. Keep asking users to choose the menu option
    no_winners = True
    while no_winners:

        # print menu

        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")

        # ask player for choice
        choice = int(input())

        # deal a new card
        if choice == 1:
            card = rng.next_int(13) + 1
            # use if/elif/else chain
            if card == 1:
                print("Choose an option:")
                print("Your card is a ACE!")
            elif 2 <= card <= 10:
                print("Choose an option:")
                print(f"Your card is a {card}!")
            elif card == 11:
                print("Choose an option:")
                print("Your card is a JACK!")
                card = 10
            elif card == 12:
                print("Choose an option:")
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Choose an option:")
                print("Your card is a KING!")
                card = 10
            player_hand += card
            print(f"Your hand is: {player_hand}\n")

            # Win/lose condition

            if player_hand == 21:
                print("BLACKJACK! You win!")
                no_winners = False
                player_win += 1


            elif player_hand > 21:
                print("You exceeded 21! You lose.")
                no_winners = False
                dealer_win += 1


            #dealer_hand = rng.next_int(11) + 16

        elif choice == 2:

            dealer_hand = rng.next_int(11) + 16

            if 21 >= dealer_hand > player_hand:
                print("Choose an option:")
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}\n")
                print("Dealer wins!")
                no_winners = False
                dealer_win += 1


            elif 21 < dealer_hand > player_hand :
                print("Choose an option:")
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}\n")
                print("You win!")
                no_winners = False
                player_win += 1


            elif dealer_hand == player_hand:
                print("Choose an option:")
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}")
                print("It's a tie! No one wins!")
                tie_num += 1
                no_winners = False



        elif choice == 3:
            print("Choose an option:")
            print(f"Number of Player wins:{player_win}")
            print(f"Number of Dealer wins:{dealer_win}")
            print(f"Number of tie games:{tie_num}")
            total_games = player_win + dealer_win +tie_num
            print(f"Total # of games played is:{total_games}")
            percentage_wins = (float(player_win) / float(total_games)) * 100
            print(f"Percentage of Player wins:{percentage_wins} %\n")



        elif choice == 4:
            no_winners = False
            game_continue = False
            print("Choose an option:")
        else:
            print("Choose an option:")
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")

