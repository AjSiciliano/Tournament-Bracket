
Author: **Andrew Jordan Siciliano (Aj)**

Title: **Simple Tree Representation of a Tournament Bracket**

Reason of Birth: *University Of Miami's Chess Club*

_____________________________________________

**Commands:**

*To run default tournament bracket:*
	
	> make

*For Help Page:*
	
	> make help

_____________________________________________

**How do I configure the bracket?**

The folder player_files contains three .txt files. 

Each .txt in 'player_files' is associated with an specific instance of a bracket.

These put a name on each line of the .txt files, followed by a comma

To report winnings add another comma on the line of the player who won
	
	Ex: Line in .txt where 'John' has 4 winnings
		*John,,,,,*

The number of winnings per player is the (number of commas-1) on each respective line


Once a player has winnings >= the number of rounds,
they will be the winning user at the top of the bracket.

See the 'Help Page' for more clarity. 

**WARNING:**
Make sure to be diligent as there is no corrective cases to allow for ease of manipulation. 
If two users competing in a round are both marked as winners, 
the user last in the order of players will be marked as the winner...

_____________________________________________

**Scripts**

*tournament.py* -> contains the tournament class

*default.py* -> default driver file for constructing tournament

_____________________________________________

Thank you,

~Aj






# Simple-Tree-Representation-of-a-Tournament-Bracket
