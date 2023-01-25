import os, sys
os.system('clear')
try:
    __import__("OKE").menu()
except Exception as e:
    exit(str(e))

