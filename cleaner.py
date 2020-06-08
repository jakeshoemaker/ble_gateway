#   jake shoemaker 06.07.2020
#
#   this program cleans data and removes
#   unwanted characters that were causing the
#   json files to not format correctly

import json
import string
from shutil import copyfile

# file containing soon to be json data
f = open(r"C:\Users\jakes\OneDrive\Desktop\unclean_log.txt", "r").read()
f = f.replace(']\n[', ',\n')  # replacing faulty characters
f.replace('[', '')
f.replace(']', '')

# writing to file
clean_file = open(r"C:\Users\jakes\OneDrive\Desktop\unclean_log.txt", "w")
clean_file.write(f)
clean_file.close()

# assumes correct file pattern from BLE gateway
copyfile(r"C:\Users\jakes\OneDrive\Desktop\unclean_log.txt",
         r"C:\Users\jakes\OneDrive\Desktop\clean_data.json")
