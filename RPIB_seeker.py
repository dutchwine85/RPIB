import random
import string

def acronym(y=3):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
randAcronym = (acronym(3))
print("Looking for " + randAcronym + " manual ...")
print()

exec(open("/Users/tomweston/RPIB/RPIB_seekerActual.py").read())

if not pdfName:
    print("empty, re-run ...")
    pdfGrab()

import requests
try:
    PDFurl = pdfGrab()[0]
except IndexError:
    exec(open("/Users/tomweston/RPIB/RPIB_seekerActual.py").read())

try:
    r = requests.get(PDFurl, allow_redirects=True)
    print(">> PDFurl error !")
except NameError:
    exec(open("/Users/tomweston/RPIB/RPIB_seekerActual.py").read())
print(r)

print("- - - ")
print(">>"+PDFurl)
print("\n")

import io
for i in range(1):
    with io.open("/Users/tomweston/RPIB/x_thePDF/thePDF_" + str(i) + ".pdf", 'w', encoding='utf-8') as f:
        f = open("/Users/tomweston/RPIB/x_thePDF/thePDF_"+str(i)+".pdf","w")

open("/Users/tomweston/RPIB/x_thePDF/thePDF_"+str(i)+".pdf", "wb").write(r.content)
"/Users/tomweston/RPIB/x_thePDF/thePDF_%s.pdf" % i
"/Users/tomweston/RPIB/x_thePDF/thePDF_{}.pdf".format(i)
