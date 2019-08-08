#!/usr/bin/python3
# -*- Codin: utf-8 -*- 
# ------------------------------------------ #
# Name :   SLAx [ SouFianE]                  #
# Mail : [ slax.soufiane@gmail.com ]         #
# Date : Tue 06 Aug 2019 12:05:53 PM +01     #
# OS   : DeepinOs Linux 15.11                #
# ------------------------------------------ #
from os import system           # 
#------------------------------ #
# _nikto, _nmap, _wpscan, _joomscan, _uniscan, _dirsearch, _turbolist3r, _sqlmap
def _nikto():
    """ HERE THE WAY WE WANT TO USE NIKTO """
    print('\nNIKTO | Scan web server for known vulnerabilities\n')
    target_host = input("\n[+] Target UrL: ") 
    cmd = 'nikto -host %s'%(target_host)
    system(cmd)
def _nmap():
    """ HERE THE WAY WE WANT TO USE NMAP """
    print("")
    print('NMAP | Network exploration tool and security / port scanner\n')
    target = input("\n[+] Target UrL: ") 
    nmapcmd = 'nmap -sC -sV -oA %s %s'%(target, target) # first one is file output second one is target
    system(nmapcmd)
def _wpscan():
    """ HERE THE WAY WE WANT TO USE WPSCAN """
    print('\nWPSCAN | WordPress Security Scanner by the WPScan Team\n')
    target_wp = input("\n[+] Your WordPress Url: ")
    cmd_wp = 'wpscan --url %s --enumerate u'%(target_wp)
    system(cmd_wp)
def _joomscan():
    """ HERE THE WAY WE WANT TO USE JOOMSCAN """
    print('\nJOOMSCAN | joomla security scanner by OWASP')
    target_joom = input("\n[+] Your WordPress Url: ")
    cmd_joom = 'joomscan -u %s'%(target_joom)
    system(cmd_joom)
def _uniscan():
    """ HERE THE WAY WE WANT TO USE UNISCAN """
    print('\nUNISCAN | All-In-One Scanner [ dir|files|vulns ]')
    target_uni = input("\n[+] Your Url: ")
    cmd_unis = 'uniscan -u %s -qweds'%(target_uni)
    system(cmd_unis)
def _dirsearch():
    """ HERE THE WAY WE WANT TO USE DIRSEARCH """
    print('\nDIRSEARCH | brute force directories and files in websites')
    target_dir = input("\n[+] Your Url: ")
    cmd_dir = 'python3 /opt/Tools/dirsearch/dirsearch.py -u %s -e php,asp,aspx,txt,sql'%(target_dir)
    system(cmd_dir)
def _turbolist3r():
    """ HERE THE WAY WE WANT TO USE TURBOLIST3R """
    print('\nTURBOLIST3R | subdomain discovery tool')
    target_tur = input("\n[+] Your Url: ")
    cmd_trbo = 'python /opt/Tools/Turbolist3r/turbolist3r.py -d %s -o %s'%(target_tur, target_tur+'_dns.txt')
    system(cmd_trbo)
def _sqlmap():
    """ HERE THE WAY WE WANT TO USE SQLMAP """
    print('\nSQLMAP | automatic SQL injection tool')
    target_sql = input("\n[+] Your SqlInject Url: ")
    cmd_sqlmap = 'sqlmap -u %s --dbs --hex --random-agent'%(target_sql)
    system(cmd_sqlmap) 
# End Of The Pentest Tools #
# @CLASS BRUTEFORCE LATER | hydra | medusa | ncrack ANd More Inshae Allah