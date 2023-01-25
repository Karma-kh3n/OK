import os, sys
os.system('clear')
try:
    __import__("OKE").AutoFolder()
except Exception as e:
    exit(str(e))
