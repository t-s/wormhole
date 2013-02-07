Wormhole
=========
When a file appears in a specified director(ies), SCP that file to specfied remote host(s).

Wormhole uses inotify code from http://code.activestate.com/recipes/576375-low-level-inotify-wrapper/.

Planned to be expanded with flexible syntax.

syntax: 
wormhole.py -d [directories] -r [remote hosts] 
wormhole.py -h to print help message        

example: 
wormhole.py /home/user/dir1/ ../dir2/ user@remote1 user@remote2