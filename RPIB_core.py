# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  R A N D O M  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  P D F  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  I M A G E  %%%%%%%%%%%%%.     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  B O T  %%%%%%%%%%%%%%%%%  %%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  v2 %%%%%%%%%%%%%%%%%%%%%%  %%   %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%. #*   %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%(//#%%%%     #%%**//**%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%*/    *(%%/    %%*/    .#%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%#*    #%%(     ,%%##..(#%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%##%%%#    %,  #%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%/    %%%%.  *%(*.   ../%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%.              .%%%%%%%.   /%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%      #////////,&%     ..   /%%%%%%%%%%
# %%%%%%%%%%%%%%%%    %    %,////////%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%   %%%.   /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%  %%%    (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%     ,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import os
import random
import fitz
from fitz import TOOLS
from PIL import Image
import shutil
import fnmatch
from datetime import datetime

tStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

exec(open("/Users/tomweston/RPIB/RPIB_cleaner.py").read())

exec(open("/Users/tomweston/RPIB/RPIB_seeker.py").read())

file = "/Users/tomweston/RPIB/x_thePDF/thePDF_0.pdf"

try:
    pdf_file = fitz.open(file)
except RuntimeError:
    exec(open("/Users/tomweston/RPIB/RPIB_seeker.py").read())

print(fitz.TOOLS.mupdf_warnings())

try:
    pdf_file = fitz.open(file)
except NameError:
    exec(open("/Users/tomweston/RPIB/RPIB_seeker.py").read())

for page_index in range(len(pdf_file)):
    page = pdf_file[page_index]
    image_list = page.getImageList()

    if image_list:
        print(f"PAGE", page_index, "contains", [len(image_list)], "images")
    else:
        print("PAGE", page_index, "is EMPTY")
    for image_index, img in enumerate(page.getImageList(), start=1):

        xref = img[0]

        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]

        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image.save(open(f"/Users/tomweston/RPIB/x_images/pic{page_index+1}_{image_index}.{image_ext}", "wb"))


def chosen():
    return random.choice(os.listdir(r"/Users/tomweston/RPIB/x_images"))


def size(fn):
    return os.path.getsize(r"/Users/tomweston/RPIB/x_images/"+fn)

c = 1

print("\n")

threshold = 6000
while True:  # fail check;
    z_file = chosen()
    file_size = size(z_file)
    if file_size < threshold:
        print(z_file + " is too small")
        while c < 200:
            c = c + 1
            break
    else:  # pass check;
        break
print(z_file + " is at least 6KB")

src_path = r"/Users/tomweston/RPIB/x_images/"+z_file
dst_path = r"/Users/tomweston/RPIB/x_chosen"
shutil.move(src_path, dst_path)

head, tail = os.path.split(str(pdfName))
docName = tail
print()
print("---> " + z_file +"in"+ docName[:-6] , "is ready to tweet! <---")
print()

exec(open("/Users/tomweston/RPIB/RPIB_tweeter.py").read())

print()
print("Post complete @ "+tStamp)
proc = proc + 1
print((str(proc))+" consecutive posts with no errors")
