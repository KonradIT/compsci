#API based on horarios app from Android. 

import urllib.request
import datetime
import re
import time
import sys
class Renfe:
	def __init__(self, nucleo, origen, destino):
		now = datetime.datetime.now()
		self.nucleo = nucleo
		self.origen = origen
		self.destino = destino
		self.url = 'http://horarios.renfe.com/cer/hjcer310.jsp?nucleo={}&i=i&cp=NO&o={}&d={}&df={}&ho=00&hd=26&TXTInfo='.format(nucleo,origen,destino,now.strftime("%Y%m%d"))  
		self.html_src = urllib.request.urlopen(self.url).read().decode('utf-8','ignore').encode("utf-8")
		self.tabla_horarios=[]
	def get_trains(self):
		return self.html_src
	
	def get_from_time(self, hour):
		now = datetime.datetime.now()
		self.url = 'http://horarios.renfe.com/cer/hjcer310.jsp?nucleo={}&i=i&cp=NO&o={}&d={}&df={}&ho={}&hd=26&TXTInfo='.format(self.nucleo,self.origen,self.destino,now.strftime("%Y%m%d"),hour)
		self.html_src = urllib.request.urlopen(self.url).read().decode('utf-8','ignore').encode("utf-8")
		return self.html_src
		
	def get_table(self, src, remaining=False):
		#print(src)
		#Get HTML table: <table border="0" width="95%" cellpadding="1" cellspacing="1" align="center" id="tabla" class="horarios"> and </table>
		start= "<table border=\"0\" width=\"95%\" cellpadding=\"1\" cellspacing=\"1\" align=\"center\" id=\"tabla\" class=\"horarios\">"
		end="</table>"
		now = datetime.datetime.now()
		table = src.split(start)[1].split(end)[0]
		#print(table)
		#Iteration to print a decent ascii table.
		for index, line in enumerate(src.split('\n')):
			if "<tr class" in line:
				if remaining:
					departure=src.splitlines()[index+9].replace("<td align=center>","").replace("</td>","").strip()
					if now.strftime("%H.%M") < departure:
						pass
					diff = total_time=(datetime.datetime.strptime(departure,'%H.%M') - datetime.datetime.strptime(now.strftime("%H.%M"),'%H.%M'))
					if str(diff).startswith("0:0"):
						remain=" NOW"
					else:
						remain=str(diff)[:-3]
					now = datetime.datetime.now()
					time=now.replace(hour=int(departure.split(".")[0]), minute=int(departure.split(".")[1]))
					if now < time:
						self.tabla_horarios.append([src.splitlines()[index+2].strip(), departure.replace(".",":") + " - " + remain, src.splitlines()[index+10].replace("<td align=center>","").replace("</td>","").strip()])
				else:
					self.tabla_horarios.append([src.splitlines()[index+2].strip(), src.splitlines()[index+9].replace("<td align=center>","").replace("</td>","").strip(), src.splitlines()[index+10].replace("<td align=center>","").replace("</td>","").strip()])
		if remaining:
			print("|Linea|  Departure   |Arrival|")
		else:
			print("|Linea|  Dep  |Arrival|")
		for i in self.tabla_horarios:
			
			line = str(i).replace("[","| ").replace("]"," |").replace("\'","").replace(","," |")
			print(line)
			print("-"*len(line))
	def get_next_train(self, src):
		start= "<table border=\"0\" width=\"95%\" cellpadding=\"1\" cellspacing=\"1\" align=\"center\" id=\"tabla\" class=\"horarios\">"
		end="</table>"
		table = src.split(start)[1].split(end)[0]
		for index, line in enumerate(src.split('\n')):
			if "<tr class" in line:
				next_train=  [src.splitlines()[index+2].strip(), src.splitlines()[index+9].replace("<td align=center>","").replace("</td>","").strip(), src.splitlines()[index+10].replace("<td align=center>","").replace("</td>","").strip()]
				break
		return next_train
alpedrete_villalba = Renfe("10","10200","12002")# Madrid, Alpedrete > Villalba: 10, 10200 12002
now = datetime.datetime.now()
#print(alpedrete_villalba.get_trains())
print("Renfe cercanias\nAlpedrete to Villalba")
choice=""
if len(sys.argv) > 1:
	choice=sys.argv[1]
else:
	input("Full table or starting from " + now.strftime("%H hour") + "?: [full/now]: ").lower()
if choice == "full":
	alpedrete_villalba.get_table(alpedrete_villalba.get_trains().decode("utf-8"))
else:
	alpedrete_villalba.get_table(alpedrete_villalba.get_from_time(now.strftime("%H")).decode("utf-8"), remaining=True)
