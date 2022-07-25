# blacklisted
A python script to check if multiple ips appear on any blacklists

This code I created to automate the task of looking up ips to confirm if they are blacklisted via any of the blacklists on mxtoolbox.com. This requires installing the modules for colored, termcolor, selenium and the gecko web driver for Firefox. After the installation of these, this script will open a temp file with the vi editor. It will require all ips be entered in a single column like so:

67.160.42.207
189.167.244.72
69.162.124.228
192.243.55.134
192.243.55.131
192.243.55.130
69.20.52.200
54.210.21.184

After this you should receive something simliar to the following:

67.160.42.207 Blacklisted<br>
189.167.244.72 Blacklisted<br>
69.162.124.228 Ok<br>
192.243.55.134 Blacklisted<br>
192.243.55.131 Blacklisted<br>
192.243.55.130 Blacklisted<br>
69.20.52.200 Ok<br>
54.210.21.184 Blacklisted<br>

Reference links for blacklisted ips:

https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a67.160.42.207&run=toolpage
https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a189.167.244.72&run=toolpage
https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a192.243.55.134&run=toolpage
https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a192.243.55.131&run=toolpage
https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a192.243.55.130&run=toolpage
https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a54.210.21.184&run=toolpage

An error message will be displayed if data was entered blank or incorrectly.

To run this code you just need to add execute permissions like this:

$ chmod +x blacklisted.py
