
from abc import ABC, abstractmethod
# create a base class
class library(ABC):
	def read(self):
		pass

class Treasure_island(library):

	def read(self):
		print("buy this adventorous book")

class dairy_of_the_wimpy_kid(library):

	def read(self):
		print("buy this kid book")
		
class magzine(library):

	def read(self):
		print("buy this magzine")

class APJ_Abdul_kalam(library):

	def read(self):
		print("buy this biography book")

class HarryPotter(library):

	def read(self):
		print("buy this fictional book")
        