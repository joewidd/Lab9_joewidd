"""
Matching Coin Game,
Joe Widdifield,
Create a coin matching game between 2 players,
9/22/2026
"""
from player import Player


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    play_again = "y"
    while play_again == "y" or play_again == "Y":
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"\n\n{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"\n\n{player1.get_name()} wins this round!")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"\n\n{player2.get_name()} wins this round!")

        print(f"\n\n{player1.get_name()}'s wallet: {player1.get_wallet()}")
        print(f"{player2.get_name()}'s wallet: {player2.get_wallet()}")

        if player1.get_wallet() <= 0:
            print(f"\n\n{player1.get_name()} is out of coins! {player2.get_name()} wins the game!")
            break
        elif player2.get_wallet() <= 0:
            print(f"\n\n{player2.get_name()} is out of coins! {player1.get_name()} wins the game!")
            break

        play_again = input("\n\nPlay again? (y/n): ")

    print("\n\nFinal Results:")
    print(f"{player1.get_name()}: {player1.get_wallet()} coins")
    print(f"{player2.get_name()}: {player2.get_wallet()} coins")

    if player1.get_wallet() > player2.get_wallet():
        print(f"\n\n{player1.get_name()} finished with more coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"\n\n{player2.get_name()} finished with more coins!")
    else:
        print("\n\nBoth players finished with the same number of coins!")



main()