#!/usr/bin/python
# -*- coding: utf -*-

import sys
import re
import time
import gntp.notifier

lyx = ["\\", "LatexCommand", "bibfiles", "options", "eqs-within-sections", "figs-within-sections"]

# More complete example
growl = gntp.notifier.GrowlNotifier(
    applicationName = "LyX Document Length",
    notifications = ["Length"],
    defaultNotifications = ["Length"]
)
growl.register()

if __name__ == '__main__':
    if len(sys.argv) > 2:
    	last = 0
    	while True:
    		length = 0.
	    	with open(sys.argv[1], 'r') as f:
		    	for line in f.read().split("\n"):
		    		if len(line) > 0:
			    		text = True
			    		for na in lyx:
			    			if line.startswith(na):
			    				text = False
			    				break
			    		if text:
		    				length += len(re.findall(r'\w+', line))
			f.closed

			length = round((length/int(sys.argv[2]))*100, 2)
			if length != last:
				growl.notify(
					noteType = "Length",
					title = sys.argv[1].split("/")[-1],
					description = str(length) + "% done",
					icon = "file:///" + sys.path[0] + "/" + "icon.png",
					sticky = False,
					priority = 0,
				)
				last = length
			time.sleep(1)