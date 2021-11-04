
Author: **Andrew Jordan Siciliano**

Title: **Simple Tree Representation of a Tournament Bracket**

Reason of Birth: *University Of Miami's Chess Club*

_____________________________________________

**Commands:**

*To run default tournament bracket:*
	
	> make

*For help page:*
	
	> make help

_____________________________________________

**How do I configure the bracket?**

The folder player_files contains three .txt files. 

Each .txt in 'player_files' is associated with a specific instance of a bracket.

On each line of the .txt files, put a player name followed by a comma.
	
	Ex: John,

To report a winning, add another comma to the line of the player who won.
	
	Ex: Line in .txt where 'John' has 4 winnings
		John,,,,,

The number of winnings per player is the (number of commas-1) on each respective line

Once a player has winnings >= the number of rounds,
they will be the winning user at the top of the bracket.

To update the bracket:
	
	> make

See the 'Help Page' for more clarity.

**WARNING:**
Be diligent as there is no corrective cases. 
If two opponents competing in a round are both marked as winners in the txt file, 
the bottom user,in the pair, will be marked as the winner...

_____________________________________________

**Scripts**

*tournament.py* -> contains the tournament class

*default.py* -> default driver file for constructing tournament

_____________________________________________

Thank you,

~Aj






# Simple-Tree-Representation-of-a-Tournament-Bracket
