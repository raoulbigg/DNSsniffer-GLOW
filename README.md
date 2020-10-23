# DNSsniffer-GLOW
This repository contains DNS sniffer I created that I used on my project: "CrowdCloud" on GLOW 2019 in Eindhoven

The controller.py uses scapy to monitor traffic on port 53(dns) and compares the dns query to the queries in the whitelist.json. It will send an integer to the arduino when it has a match.  
  
  
Working demo:
https://www.youtube.com/watch?v=Ggsr-_8FsdI
  
https://www.gloweindhoven.nl/nl/festival/projecten-2019/lichtkunstprojecten/crowd-cloud
