import os, sys
os.system('clear')
try:
    __import__("run").MulaiTools()
except Exception as e:
    exit(str(e))
