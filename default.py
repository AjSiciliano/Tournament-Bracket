from tournament import *
from termcolor import colored

#Author: Andrew Jordan Siciliano
#Simple Tree Representation of a Tournament Bracket

devisions = ['advanced','intermediate','beginer']

print("\n" + "*"*55 + "\n")

for devision in devisions:
	
	print(colored("\n"+devision.upper()+" BRACKET", 'magenta',attrs=["underline","bold"]))

	try:

		bracket = tournament("undecided",0,None)

		bracket.run_game("player_files/"+devision+".txt")

		tree = bracket.printify()
		tree.show(line_type="ascii-em")

	except:
		print(colored('An Error Occured!', 'red'))

	print("\n" + "*"*55 + "\n")