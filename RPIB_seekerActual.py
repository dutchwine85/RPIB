from googlesearch import search
def pdfGrab():
    return search("filetype:pdf manual"+randAcronym, num_results=0)

pdfGrab()

pdfName = pdfGrab()
print("Searching ... ")
print()
print("Search complete @ "+tStamp)
print()
print("index check, list contents :")
print(pdfName)