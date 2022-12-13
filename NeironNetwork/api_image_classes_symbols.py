import os
import sys
from get_image_allinfo import getimage_allinfo

basedir = os.path.abspath(os.path.dirname(__file__))
filename = rf"{str(sys.argv[1])}"

result = getimage_allinfo(os.path.join(basedir,filename))

print(result)