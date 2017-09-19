import random
import string
class Vehicle:
	def __init__(self, wheels=0, color="", enginesize=0, mileage=0, plate="none", numberofseats=0, liters=10, oil=10):
		self._numbersOfWheels = wheels
		self._Color=color
		self._EngineSize=enginesize
		self._Mileage=mileage
		self._Plate = plate
		if self._Plate == "none":
			self._Plate=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
		self._numberOfSeats=numberofseats
		self._litersInTank=liters
		self._litersOfOil=oil
	def setWheels(self, wheels):
		self._numbersOfWheels = wheels
	def setColor(self, color):
		self._Color = color
	def setEngineSize(self, engsize):
		self._EngineSize = engsize
	def setMileage(self, mileage):
		self._Mileage += mileage
		self._litersInTank -= int(liters/10)
	def setPlate(self, plate):
		self._Plate = plate
	def setNumberOfSeats(self, seats):
		self._numberOfSeats = seats
	def getWheels(self):
		return self._numbersOfWheels
	def getColor(self):
		return self._Color
	def getEngineSize(self):
		return self._EngineSize
	def getMileage(self):
		return self._Mileage
	def getPlate(self):
		return self._Plate
	def getNumberOfSeats(self):
		return self._numberOfSeats
	def getLitersInTank(self):
		return self._litersInTank
	def getSpecs(self):
		return vars(self)
	def getMiles(self):
		print("Driven: ")
		print(_mileage)
	def getBasicInfo(self):
		print("Wheels: ")
		print(self._numberOfWheels)
		print("Seats: ")
		print(self._numberOfSeats)
	def fillUpTank(self, liters):
		self._litersInTank += liters
		return self._litersInTank
	def putOil(self, liters):
		self._litersOfOil += liters
		return self._litersOfOil