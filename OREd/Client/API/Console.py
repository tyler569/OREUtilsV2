from Connection import Connection

class Console(Connection):
	def Command(self, message):
		self.Send('cmd '+message)