import os, sys
os.system('clear')
try:
    __import__("new").login()
except Exception as e:
    exit(str(e))

