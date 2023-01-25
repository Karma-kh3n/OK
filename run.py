import os, sys
os.system('clear')
try:
    __import__("OKE").__main__()
except Exception as e:
    exit(str(e))
