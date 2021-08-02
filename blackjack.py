import random, sys

# Set up constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"


def main():
    print(
        """
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
    """
    )

    money = 5000
    while True:  # main game loop
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            sys.exit()

        # Let the player enter their bet for this round:
        print("Money:", money)
        bet = get_bet(money)

        # Give the dealer and player two cards from the deck
        deck = get_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print(f"Bet: {bet}")
        while True:  # # Keep looping until player stands or busts
            display_hands(player_hand, dealer_hand, True)
            print()

            # Check if the player has bust:
            if get_hand_value(player_hand) > 21:
                break

            # Get the player's move, either H(hit), S(stand), D(double down)
            move = get_move(player_hand, money - bet)

            # Handle the player's move:
            if move == "D":
                # Player can increase the bet
                additional_bet = min(bet, (money - bet))
                bet += additional_bet
                print(f"New bet: {bet}")

            if move in ("H", "D"):
                # Hit/ double downing takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print("You drew a {} of {}.".format(rank, suit))
                player_hand.append(new_card)
                if get_hand_value(player_hand) > 21:
                    continue  # the player has busted

            if move in ("S", "D"):
                # Stands/doubling down stops the player's turn
                break

        # Handle the dealer's action
        if get_hand_value(dealer_hand) <= 21:
            while get_hand_value(dealer_hand) > 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break  # The dealer has bursted
                input("press Enter to continue...")
                print("/n/n")

        # Show final hands
        print("Final hands")
        display_hands(player_hand, dealer_hand, True)

        # Handle whether the player won, lost, or tied:
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        if dealer_value > 21:
            print(f"Dealer bursts. You win {bet}")
            money += bet
        elif player_value > 21:
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You win {bet}")
            money += bet
        elif player_value == dealer_value:
            print("Its tie, the bet is returned to you.")

        input("Press Enter to continue...")
        print("\n\n")


def get_move(player_hand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand, 'D' for double down."""
    while True:  # keep looping untill the player enters a correct move
        moves = ["(H)it, (S)tand"]
        # The player can double down on the first move
        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # Get the player's move
        move_prompt = ", ".join(moves) + ">"
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "D(ouble) down" in moves:
            return move  # Player has entered a valid move


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Show cards. Hide the dealers first card if show_dealer_hand is False."""
    # Show the dealer's cards
    if show_dealer_hand:
        print("DEALER:", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("DEALER: ????")  # hide the first card
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards
    print("PLAYER:", get_hand_value(player_hand))
    display_cards(player_hand)


def display_cards(cards):
    """Display all cards in cards list."""
    rows = ["", "", "", "", ""]  # The text to display on each row

    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            # Print card's back
            rows[1] += "|## |"
            rows[2] += "|###|"
            rows[3] += "|###|"
        else:
            # Print card's front
            rank, suit = card
            rows[1] += f"|{rank}  |"
            rows[2] += f"| {suit} |"
            rows[3] += f"|__{rank}|"

    for row in rows:
        print(row)


def get_hand_value(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1."""
    value = 0
    num_of_aces = 0

    # Add the value for the non_ace cards:
    for card in cards:
        rank = card[0]  # card is a tuple
        if rank == "A":
            value += 1
            num_of_aces += 1
        elif rank in ("Q", "K", "J"):
            value += 10
        else:
            value += int(rank)

    for i in range(num_of_aces):
        # If another 10 can be added with busting, do so
        if value + 10 <= 21:
            value += 10

    return value


def get_bet(max_bet):
    """Ask the player how much they want to bet for this round"""
    while True:  # Keep asking until they enter a valid amount.
        print(f"How much would you like to bet?(1) - {max_bet} or QUIT")
        bet = input(">").upper().strip()
        if bet == "QUIT":
            print("Thanks for playinpg!")
            sys.exit()

        if not bet.isdecimal():
            continue  # ask again

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    """Return the deck of cards for the game as the list of 52 elements: (rank, suit)."""
    deck = []
    for suit in (HEARTS, SPADES, DIAMONDS, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("Q", "K", "J", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    main()
