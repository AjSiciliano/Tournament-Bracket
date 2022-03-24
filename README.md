# Simple-Tree-Representation-Of-A-Tournament-Bracket

Author: **Andrew Jordan Siciliano**

Reason of Birth: *University Of Miami's Chess Club*

_____________________________________________

*First order of business, cd into the 'Tournament-Bracket' directory....*

**Commands:**

*To run default tournament bracket:*
	
	> make

*For help page:*
	
	> make help

_____________________________________________

**How do I configure the bracket?**

The directory 'player_files' contains three .txt files. 

Each .txt in 'player_files' is associated with a specific instance of a bracket.

On each line of the .txt files, put a player name.
	
	Ex: John

To report a winning, add a comma to the line of the player who won.
	
	Ex: Line in .txt where 'John' has 4 winnings
		John,,,,

The number of winnings per player is the number of commas on his/her/their respective line.

Once a player has winnings >= the number of rounds,
they will be the winning player at the top of the bracket.

To add a late player put an '@' before their name.

	Ex: If John was late, the line would be...
		@John

Late players are excluded from the initial randomization to preserve the state of the game.

To update the bracket to its current state:
	
	> make

See the 'Help Page' for more clarity.

**WARNING:**
Be diligent as there is no corrective cases. 
If two opponents competing in a round are both marked as winners, 
the bottom user in the pair will be marked as the winner...

**There is a new found issue where if a bracket has 
an overflow of leaves that are passes, that player will need a
replacement tag. 

EX: 

Nayan
Aryan Jhaveri,,
Fransisco,,
Michael kavounas
Will Huggins

turns to...

Nayan,
Aryan Jhaveri,
Fransisco,,
Michael kavounas
Will Huggins
@return
@Aryan_Update,,**

*Note:* 
You may add as many players as you like, the program is dynamic.

_____________________________________________

**Scripts**

*tournament.py* -> Contains the tournament class...

*default.py* -> Default driver file for running tournaments...

_____________________________________________

*Thank you,*

*~Aj*


