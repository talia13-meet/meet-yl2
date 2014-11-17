class animal:
	def __init__(self, name,age):
		self.name=name
		self.age=age
	def sleep(self):
		print self.name +" of "+ str(self.age) +" years old is sleeping"
	def hello(self):
		if(self.age>3):
			print self.name + " is too old "
		else:
			print self.name + " is too young"	
	def look (self):
		print self.name + " has " + self.fur_color + " fur "			
class Bird(animal):
	def __init__(self, name,age,wings_color):
		animal.__init__(self,name,age)
		self.wings_color=wings_color
class Dog(animal):
	def __init__(self,name,age,fur_color):
		animal.__init__(self,name,age)
		self.fur_color=fur_color
a=Dog("bobi",6,"brown")
a.sleep()
a.hello()
a.look()
b=Dog("MIKY",2,"Blonde")
b.sleep()
b.hello()
b.look()

	
