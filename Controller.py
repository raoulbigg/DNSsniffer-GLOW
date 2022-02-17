#!usr/bin/python

from scapy.all import *
import serial
import time
from hitCounter import save
from device import *




current = []

def liveView(pkt):
	if pkt.haslayer(DNSQR):
		if "facebook" not in pkt[DNSQR].qname[0:-1] or "twitter" not in pkt[DNSQR].qname[0:-1] or "snapchat" not in pkt[DNSQR].qname[0:-1]:
			packet = splitter(pkt[DNSQR].qname[0:-1])
		else:
			packet = pkt[DNSQR].qname[0:-1]
		try:

			if packet not in current:
				for platform in whitelist:
					if plaftorm[0] in packet and platform[0] not in blacklist:
						print packet
						current = packet
						write(platform[1])
						save(plaftorm[0])

		except Exception, e:
			print e
			pass

def splitter(pkt):

	try:
		if ".com" in pkt:
			return pkt.split(".com")[0].split(".")[1]
		elif ".net" in pkt:
			return pkt.split(".net")[0].split(".")[1]
		else:
			return pkt
	except:
		pass


if __name__ == '__main__':
	time.sleep(1)
	ser = getDevice()
	with open("json/whitelist.json") as wl:
		whitelist = json.load(wl)["whitelist"]

	with open("json/blacklist.json") as wl:
		blacklist = json.load(wl)["whitelist"]



	sniff(filter="udp port 53", prn=liveView)
  

        
