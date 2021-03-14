# Blackjack game simulator
Simple Blackjack game simulator with only one player. The simulator is developed with these rules in mind:

  - The ‘player’ takes all his turns first and then the dealer afterward
  - The player will automatically hit (take another card) if the total they have is less than 17, otherwise, they will stand (stick with the cards they have).  The player could hit multiple times
  - If the player hits and goes bust, then the dealer will win
  - If the player has the same value as the dealer then it’s a draw
  - If the player has more than the dealer, then the dealer will hit.  The dealer could hit multiple times
  - Ace is 11.
  - After each simulation, the deck is recreated and shuffled so no card counting is possible.

You will need `python 3` installed to run the app. No external packages are used.

The application can be run with:
```
python3 start.py -s 10
```
and the tests with :
```
python3 test_classes.py
```

A number of simulations can be passed to the application but it's not mandatory.
| Parameters | Type | Description | Example | Mandatory | Default
| ----- | ----- | ----- | ----- | ----- | -----
| --simulations or -s | int | Number of Blackjack simulations/rounds | 10 | No | 5
 
## Note
 
1. Application can be easily updated so the Dealer can use multiple Decks. The deck wrapper only needs to have the cards array and logic won’t have to change a bit.
2. Game with multiple Players can be supported by only changing the Game class to use lists of players instead of the player object.
 
