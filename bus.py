import vehicle
class Bus(vehicle.Vehicle):
	def __init__(self, windows, max_standing):
		super(Bus, self).__init__()
		self._windows = windows
		self._max_standing = max_standing
	def getNumberOfWindows(self):
		print(self._windows)
	def setNumberOfWindows(self, windows):
		print(self._windows)