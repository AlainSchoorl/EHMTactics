list = [1,2,3]
print(len(list))


''''import random
class Individual:
    """represents a player strategy"""
	__playerTactics = ()

	def __init__(a,b,c,d,e,f,g,h,i,j,k,l,m):
		"""initialize the class with 10 attributes between 1-5"""
		self.mentality		= random.randint(1,5)
		self.agressiveness	= random.randint(1,5)
		self.backchecking	= random.randint(1,5)
		self.gapcontrol		= random.randint(1,5)
		self.puckpressure	= random.randint(1,5)
		self.hitting		= random.randint(1,5)
		self.tempo			= random.randint(1,5)
		self.passing		= random.randint(1,5)
		self.shooting		= random.randint(1,5)
		self.dumpingthepuck	= random.randint(1,5)

	def mutate(self):
		"""WIP"""

class Population:
	"""A group of individuals"""

	def __init__(self):
		self.listofpop = []

		for range(0,18):
			self.listofpop.append(Individual.__init__())
			'''