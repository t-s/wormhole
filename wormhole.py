#!/usr/bin/env python
"""
wormhole: scp's a file when file appears in directory(s) to remote host(s)

syntax: wormhole.py -d {directories} -r {remote_hosts} -u [username]
		wormhole.py -c {command}
        wormhole.py -h to print this message

example: wormhole.py -d /home/user/dir1/ ../dir2/ -r remote1 remote2 -u user
example: wormhole.py -c sed -i 's/cat/dog/g'
"""

import sys
import os
import getpass
from inotify import Inotify, FLAGS, mask_str

if __name__ == '__main__':

	dirList = []
	remoteList = []
	commandList = []

	wdDirDict = {}	

	dirs = False
	remotes = False
	commands = False
	user = False

	# checks environment variables for username, system portable
	username = getpass.getuser()	

	inotify = Inotify()

	# we don't need to consider name of script as an arg
	sys.argv.pop(0)
	
	if len(sys.argv) == 0:
		print __doc__
		quit()

	# sort of a switching system for handling arguments
	# it may not be terribly efficient, but it makes adding arguments easy as pie
	for arg in sys.argv:
		if arg == "-h":
			print __doc__
			quit()
		elif arg == "-c":
			remotes = False
			dirs = False
			commands = True
			user = False
		elif arg == '-d':
			remotes = False
			dirs = True
			commands = False
			user = False
		elif arg == '-r':
			remotes = True
			dirs = False
			commands = False
			user = False
		elif arg == '-u':
			remotes = False
			dirs = False
			commands = False
			user = True
		elif remotes:
			remoteList.append(arg)
		elif dirs:
			arg = os.path.abspath(arg)
			dirList.append(arg)
		elif commands:
			commandList.append(arg)
		elif user:
			username = arg

	for d in dirList:
		# 180 hex is mask for both file creation and file move
		iwd = inotify.add_watch(d,0x00000180)		
		wdDirDict[iwd] = d
	
	while True:
		try:
			for wd,mask,cookie,name in inotify.read():

				dirn = wdDirDict[wd]
				path = str(dirn+"/"+name)

				if mask == 256:
					print 'File ' + name + ' added in directory'\
					' ' + dirn + '/.'
				if mask == 128:
					print 'File ' + name + ' moved to directory'\
					' ' + dirn + '/.'

				if (len(commandList) > 0):
					sys.stdout.write('%s@%s %s\n' % (username,' '.join(commandList),path))
					os.system('%s@%s %s' % (username,' '.join(commandList),path))
					break

				else:
					for r in remoteList:
						os.system('scp "%s" "%s:%s"' % (path,r,"/tmp"))

		except KeyboardInterrupt:
			for iwd in wdDirDict.keys():
				inotify.rm_watch(iwd)
			inotify.close()
			quit()
				
