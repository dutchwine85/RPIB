import shutil
from pathlib import Path

shutil.rmtree("/Users/tomweston/RPIB/x_images/")

Path("/Users/tomweston/RPIB/x_images").mkdir(parents=True, exist_ok=True)

shutil.rmtree("/Users/tomweston/RPIB/x_chosen/")

Path("/Users/tomweston/RPIB/x_chosen").mkdir(parents=True, exist_ok=True)