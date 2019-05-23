class IDM1_SB(object):


	def __init__(self, name, gender, department, S_level, SB_level):
		self.name = name
		self.gender = gender
		self.department = department
		self.S_level = S_level
		self.SB_level = SB_level
	def information(self):
		print("name:%s,gender:%s,department:%s,S_level:%s,SB_level:%s"%(self.name,self.gender,self.department,self.S_level,self.SB_level))
