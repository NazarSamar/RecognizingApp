import os
import sys
from get_images import extract_images

filename = rf"{str(sys.argv[1])}"

result = extract_images(filename)

print(result)