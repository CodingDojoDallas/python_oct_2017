class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = 0
	
	#adds a call to the end of the queue
	def add(self, call):
		self.calls.append(call)
		self.queue_size+=1
		return self
	
	#removes a call by phone number
	def remove_by_number(self, number):
		for call in self.calls:
			if call.number == number:
				self.calls.remove(call)
				self.queue_size -= 1
				return self
		else:
			print("call does not exist")
			return self
	
	#sorts the queue by caller time
	def sort_queue(self):
		if len(self.calls) > 1:
			for pointer in range(len(self.calls)):
				earliest = 0
				for index in range(pointer,len(self.calls)):
					if self.calls[index].compare(self.calls[earliest]) == 1:
						earliest = index
				temp = self.calls[pointer]
				self.calls[pointer] = self.calls[earliest]
				self.calls[earliest] = temp
		return self
	
	#removes calls from index 0 of the queue
	def remove(self):
		if self.queue_size != 0:
			self.calls.pop(0)
			self.queue_size -= 1
		else:
			print("no calls in queue")
		return self
	
	#	prints call center info
	def info(self):
		print("The Queue Length is {} \nCalls:".format(self.queue_size))
		for call in self.calls:
			call.display()
			print()
	
	
	
class Call(object):
	unique_id = 0
	def __init__(self, name, number, time, reason):
		Call.unique_id+=1
		self.id = self.unique_id
		
		self.name = name
		self.number = number
		self.time = time
		self.reason = reason

	def display(self):
		print("id: {}\nName: {} \nNumber: {} \nTime: {} \nReason: {}".format(self.id, self.name, self.number, self.time,self.reason))
	
	def compare(self, other):
		split_time1 = self.time.split(":")
		split_time2 = other.time.split(":")
		if split_time1[0] > split_time2[0]:
			return -1
		elif split_time1[0] < split_time2[0]:
			return 1
		else:
			if split_time1[1] > split_time2[1]:
				return -1
			elif split_time1[1] < split_time2[1]:
				return 1
		return 0
		

call1 = Call("Mom", 2145552326, "23:51", "You are out past curfue")
call1.display()
print("---------")
cc = CallCenter()
call2 = Call("Mom", 2145552326, "23:50", "You are out past curfue")
cc.add(call2)
cc.add(call1).add(Call("Dad", 9725554321, "3:20", "where are you?")).info()

print("---------")
cc.sort_queue().info()
print("---------")
cc.remove_by_number(4695551234).info()