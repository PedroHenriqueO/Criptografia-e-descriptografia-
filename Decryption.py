from crypto.cipher import XOR
import base64
import os
import sys

def decrypt():
    key = 'RM83594'
    cipher = XOR.new(key)
    pathfile = '/Users/Pedro/documentos/rm.txt, rm.pdf, rm.doc'
    openfile = open(pathfile, 'rb')
    readfile = openfile.read()
    openfile.close()
    encoding = cipher.decrypt(base64.b64decode(readfile))
    os.system('rm'+pathfile)
    openfile2 = open(pathfile, 'wb')
    openfile2.write(encoding)
    openfile2.close()

decrypt()