#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import uuid
import sys
import time
import errno
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Worker functon to call mxtoolbox and parse data:
def mxget( x ):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get('https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a'+ x + '&run=toolpage')
    time.sleep(3) # Lowering or removing this time may cause data to be returned incorrectly.
    src = driver.page_source

    global bl

    if re.search(r"\bLISTED\b", src):
        A = colored('Blacklisted', 'red')
        print("%s %s" % (x, A))
        bl.append(x)
    else:
        B = colored('Ok', 'green')
        print("%s %s" % (x, B))

    driver.quit()

# Grandiose Banner
print(' ')
print('                     Злой Русский!               ')
print(' ')

print(colored('                 Ascii Banner Redacted              \n','red'))

input("Press Enter to continue with entering ips...")

# Create a random named temp file and open it in vi to paste ips to.
temp_name = str(uuid.uuid4())
file = open("/tmp/" + temp_name, "w")
file.close()
os.environ['test_tmp'] = "/tmp/" + temp_name
os.system("vi $test_tmp")

logfile = "/tmp/" + temp_name

if os.path.isfile("/tmp/" + temp_name) and os.path.getsize("/tmp/" + temp_name) > 0:
	pass
else:
	print("\nAll I need is one column of ips. Please try again...")
	sys.exit(1)
try:
    file = open(logfile, "r")
    # create some empty lists
    ips = []
    bl = []
    #print('Checking... This could take some time to complete.')
    for text in file.readlines():
        # strip off the \n
        text = text.rstrip()
        # this is probably not the best way, but it works for now
        regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$', text)
        # if the regex is not empty and is not already in ips list append
        if regex is not None and regex not in ips:
            ips.append(regex)
        else:
            print("\nAll I need is one column of ips. Please try again...")
            sys.exit(1)

    # loop through the list and if not empty call the worker function with each ip. 
    print("Checking... This could take a sec.\n")
    for ip in ips:
        addy = "".join(ip)
        if addy != '':
            mxget(addy)

    # Print links to ips found:
    print("\nReference links for blacklisted ips:\n")
    for l in bl:
        print("https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a"+ l +"&run=toolpage")

    #cleanup and close file
    file.close()

# catch any standard error (we can add more later)
except IOError:
    print("An I/O Error occured with temp file.\n") 

os.system("rm $test_tmp >/dev/null")

def main():
    mxget()

if __name__ == '__main__':
    main()
