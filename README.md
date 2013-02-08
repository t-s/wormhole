Wormhole
=========
When a file appears in a specified director(ies), SCP that file to specfied remote host(s).

Wormhole uses inotify code from http://code.activestate.com/recipes/576375-low-level-inotify-wrapper/. Wormhole does not requre installation of any additional package.
It is planned to be expanded with flexible syntax.

__syntax:__

`wormhole.py -d [directories] -r [remote hosts] `

`wormhole.py -h to print help message `

`wormhole.py -c [command]`

__examples:__

`wormhole.py /home/user/dir1/ ../dir2/ user@remote1 user@remote2`

`wormhole.py -c sed -i 's/cat/dog/g'`
