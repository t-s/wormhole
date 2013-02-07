#!/usr/bin/env python

"""
wormhole: scp's a file when file appears in directory(s) to remote host(s)

syntax: wormhole.py -d [directories] -r [remote hosts]
        wormhole.py -h to print this message

example: wormhole.py /home/user/dir1/ ../dir2/ user@remote1 user@remote2
"""

import sys
import os
from inotify import Inotify, FLAGS, mask_str

if __name__ == '__main__':

	dirList = []
	remoteList = []
	wdDirDict = {}	

	dirs = False
	remotes = False

	inotify = Inotify()

	sys.argv.pop(0)
	
	for arg in sys.argv:
		if arg == "-h":
			print __doc__
			quit()
		elif arg == '-d':
			remotes = False
			dirs = True
		elif arg == '-r':
			remotes = True
			dirs = False
		elif remotes:
			remoteList.append(arg)
		elif dirs:
			dirList.append(arg)

	for d in dirList:
		iwd = inotify.add_watch(d,0x00000180)
		wdDirDict[iwd] = d
	
	while True:
		try:
			for wd,mask,cookie,name in inotify.read():

				dirn = wdDirDict[wd]

				if mask == 256:
					print 'File ' + name + ' added in directory'\
					' ' + dirn + '.'
				if mask == 128:
					print 'File ' + name + ' moved to directory'\
					' ' + dirn + '.'

				for r in remoteList:
					os.system('scp "%s" "%s:%s"' % (str(dirn+name),r,"/tmp"))

		except KeyboardInterrupt:
			for iwd in wdDirDict.keys():
				inotify.rm_watch(iwd)
			inotify.close()
			quit()
				
