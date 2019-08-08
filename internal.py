#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------- #
#  IMPORTATION   #
# -------------- # 
import sys, time
try:
    import requests
except:
    print("[!] (requests) Module Is Not Installed")
try:
    import socket
except:
    print("[!] (socket) Module Is Not Installed")
# 
# Check For Internet 
# 
def _checkforinternet():
    """ Check For Internet Here """
    try:   
        print("\n[+] Internet Connection Tester ... \n")
        time.sleep(1)
        print("[!] The Engine Is Started ... ")
        time.sleep(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = s.connect(('www.google.com', 80))
        if result==0:
          print("\n[+] You Have An Internet Connection, Happy HunTinG ... ")
        s.close()

    except KeyboardInterrupt:
      print("\n[!] Scan stopped by user... ")
      sys.exit()
    except socket.gaierror:
      print("\n[!] The target's hostname could not be resolved... Or Your Internet Is Down")
      sys.exit()
# 
# Check The Availability Of Your Target
#
def _checkavailablity():
    target_che = input("\n[+] Your Target: ")
    try:
        request = requests.get(target_che)
        response = request.status_code
        if response == "200":
            print('\n[+] Your Target Is Online: %s')%(target_che)
        if response == "404":
            print('\n[+] Your Target Is Offline: %s')%(target_che)
    except:
        print('\n[+] Your Target Is Not Resolved: %s')%(target_che)