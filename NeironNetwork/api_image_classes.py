import os
import sys
from get_images import extract_image_classes

filename = rf"{str(sys.argv[1])}"

result = extract_image_classes(filename)

print(result)