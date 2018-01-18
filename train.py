import time
import datetime
class Train:
	def __init__(self):
		self.stations=[["Alpedrete","12:49"],["Los Negrales","13:13"],["Villalba","15:00"],["Galapagar","15:30"],["Torrelodones","16:00"],["Las matas","22:00"]]
		
	def print_table(self):
		time_now = datetime.datetime.now()
		now = time_now.strftime("%H:%M")
		print(now)
		for i in self.stations:
			time.sleep(0.5)
			if time_now.time() < datetime.time(hour=int(i[1].split(":")[0]), minute=int(i[1].split(":")[1])):
				if i[1].split(":")[0] == now.split(":")[0]:
					if int(i[1].split(":")[0]) - int(now.split(":")[0]) <= 3:
						print(i," DUE SOON!")
					else:
						print(i)
				else:
					print(i)
		
trains = Train()
while True:
	print("UPDATE")
	print("----------------------")
	time.sleep(1)
	trains.print_table()
