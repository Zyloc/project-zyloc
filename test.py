class Test(object):
	
	def random_function(self,*args,**kwargs):
		self.name = data['name']
		self.intrest = data['intrest']

	def __init__(self):
		pass

if __name__=="__main__":
	test = Test()
	data = {
			"name": "kunal",
			"intrest": "coding"
	}
	test.random_function(data)
