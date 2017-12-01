#API based on horarios app from Android. 

import urllib.request
import datetime
from html.parser import HTMLParser
class Renfe:
	def __init__(self, nucleo, origen, destino):
		now = datetime.datetime.now()
		self.nucleo = nucleo
		self.origen = origen
		self.destino = destino
		self.url = 'http://horarios.renfe.com/cer/hjcer310.jsp?nucleo={}&i=i&cp=NO&o={}&d={}&df={}&ho=00&hd=26&TXTInfo='.format(nucleo,origen,destino,now.strftime("%Y%m%d"))  #Madrid, Alpedrete > Villalba: 10, 10200 12002
		self.html_src = urllib.request.urlopen(self.url).read()
		
	def get_trains(self):
		return self.html_src
	
	def get_from_time(self, hour):
		now = datetime.datetime.now()
		self.url = 'http://horarios.renfe.com/cer/hjcer310.jsp?nucleo={}&i=i&cp=NO&o={}&d={}&df={}&ho={}&hd=26&TXTInfo='.format(self.nucleo,self.origen,self.destino,now.strftime("%Y%m%d"),hour)
		self.html_src = urllib.request.urlopen(self.url).read()
		return self.html_src
		
	def get_table(self, src):
		parser = HTMLParser()
		parser.feed(src)	
	
alpedrete_villalba = Renfe("10","10200","12002")
#print(alpedrete_villalba.get_trains())
alpedrete_villalba.get_table(alpedrete_villalba.get_trains())
