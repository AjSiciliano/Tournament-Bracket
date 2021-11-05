import math
from treelib import Node as printed_node
from treelib import Tree as printed_tree
import uuid
import random
from termcolor import colored

#Author: Andrew Jordan Siciliano
#Simple Tree Representation of a Tournament Bracket

class tournament:

	def __init__(self,name,r,num_of_players):
		self.name = name
		self.player1 = None
		self.player2 = None
		self.round = r
		self.num_of_players = num_of_players

		#This uuid makes life easier when printing the bracket using treelib :)
		self.uuid = str(uuid.uuid4()) 

	def __str__(self):
		last_round = math.floor(math.log2(self.num_of_players - 1)) + 1

		#Logic for the coloring of names in bracket
		def colorfy(): #returns the marked color depending on the value of self.name

			#green -> winner
			#yellow -> 
			#cyan -> name, first round no winner

			if(self.name != 'undecided' and self.name != "pass" and last_round != self.round): return 'green' 
			elif(self.round == last_round and self.name != "pass"): return 'cyan'
			elif(self.round == last_round and self.name == "pass"): return 'yellow'
			else: return None

		#text-logic for printing rounds
		header = colored(
				"Round " + str(last_round - self.round + 1) if self.round != 0 else "\nWinner!",
				'red', attrs=["underline", "bold"]
				)

		foot = colored(self.name.upper(), colorfy(), attrs=["bold"])

		#combine the stylized text, header+footer, for improved readibility when 
		#outputting to the console
		return  header + " -> " + foot + "\n"

	def next_iteration(self, num_of_players, player_names):
		#builds the bracket based on the input variables

		#calculate the last round for tournament
		#the last round indicates all the leaf nodes
		last_round = math.floor(math.log2(num_of_players - 1)) + 1

		for player in player_names:
			#for each player in the player_names input, check the number of wins
			number_of_wins = player.count(',')

			if(self.round in range(last_round - number_of_wins,last_round+1)):
				#if this nodes round is the last round or in the range of it's respective winning rounds...
				#then the name of this node should be the winning player

				self.name = player.replace(',','')

		if(self.round <= math.floor(math.log2(num_of_players - 1))):
			#if we are not at the last round then create more nodes, 
			#link them to the current by setting self.player1 and self.player2 

			self.player1 = tournament("undecided",self.round + 1, num_of_players)
			self.player2 = tournament("undecided",self.round + 1, num_of_players)

			#run the iteration again, except by splitting the array of players by two
			#Analagous, this will keep running until there is one player in each passed array
			#We corrected the length of the players array to fit the number of leaf nodes...

			self.player1.next_iteration(num_of_players, player_names[:len(player_names)//2])
			self.player2.next_iteration(num_of_players, player_names[len(player_names)//2:])
		
	def run_game(self,file_name):

		list_of_players = None

		#read the rows of players and their respective winnings
		#from the inputed name for the text.file

		with open(file_name) as f: list_of_players = f.read().splitlines()
		
		if(len(list_of_players) <= 1):

			print(colored("At Least 2 Players Needed In Each Bracket!", 'red'))

		else:
			#use random seed to allow for replication when updating bracket
			#the seed still allows our tournament to be randomized

			random.seed(14)

			#shuffle the list of competing players
			random.shuffle(list_of_players)

			#find the next largest power of 2, inclusive of the num of players
			#this is the size of the tree we need, since each node has two children 

			corrected = 2**(math.ceil(math.log2(len(list_of_players))))

			#update the list of players to have proper length while also
			#filling empty places with passes

			list_of_players += ['pass']*(corrected - len(list_of_players))
			#allows for the root users interpretation of a bi 
			#rather than hardcoding arbitrary rules

			#this is the number of players, including non-existent opponents
			self.num_of_players = len(list_of_players) #init the number of leaf nodes

			#we can use denote the number of commas in each player row,
			#as the number of winnings per player name

			self.next_iteration(self.num_of_players, list_of_players)

			#This allows for memory of winnings by utilizing the static file (.txt files)
			#If human error occurs when setting the winnings, each player's tally of winnings 
			#won't be lost if the program is terminated


	def printify_helper(self,tree,parent_uid):
		#utilizes the 'treelib' Python library to print and style tree to the console

		#using uuid per node makes linking each child/parent easier...
		tree.create_node(self.__str__(),self.uuid,parent=parent_uid)
		if self.player1 != None: self.player1.printify_helper(tree,self.uuid)
		if self.player2 != None: self.player2.printify_helper(tree,self.uuid)

	def printify(self):
		#run this method to construct a treelib tree based upon the roots values
		#intended to be run from the root node

		ptree = printed_tree()
		if(self.num_of_players > 1): self.printify_helper(ptree, None)
		return ptree

