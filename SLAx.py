#!/usr/bin/python3
# -*- Coding: utf-8 -*- #
try:
    import os, sys
    from externaltools import  _nikto, _nmap, _wpscan, _joomscan, _uniscan, _dirsearch, _turbolist3r, _sqlmap
    from internal import _checkforinternet, _checkavailablity
except ImportError:
    raise ImportError("[!] You Need To Run : pip3 install -r req.txt")
    sys.exit(0)
              ########
              #      #
              # MENU # 
              #      #
              ########
os.system('clear')
print("\n\t\t\t\t[  SLAx  ] v0.0-1 ")
print("\t\t\t\t-----------\n")
print(" 1 - Nikto\n 2 - Nmap\n 3 - Wpscan\n 4 - Joomscan\n 5 - Uniscan\n 6 - Dirsearch\n 7 - Sqlmap\n 8 - Turbolist3r\n 9 - CheckForInternet\n 10 - CheckAvailablity")
what = input("\n[+] Choice: ") 
if what == "1":
    _nikto()
if what == "2":
    _nmap()
if what == "3":
    _wpscan()
if what == "4":
    _joomscan()
if what == "5":
    _uniscan()
if what == "6":
    _dirsearch()
if what == "7":
    _sqlmap()
if what == "8":
    _turbolist3r()
if what == "9":
    _checkforinternet()
if what == "10":
    _checkforinternet()
else:
    print("\n[+] Out Of Range")
    sys.exit(0)

