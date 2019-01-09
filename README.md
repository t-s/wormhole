wormhole
=========
When a file appears in a specified director(ies), SCP that file to specfied remote host(s) - or run an arbitrary command on that file.

Wormhole uses inotify. Wormhole does not require installation of any additional package.

__syntax:__

`wormhole.py -d [directories] -r [remote hosts] -u [username]`

`wormhole.py -d [directories] -c [command]`

`wormhole.py -h to print help message`

__examples:__

`wormhole.py -d /home/user/dir1/ ../dir2/ -r remote1 remote2 -u user`

`wormhole.py -d /home/user/dir1/ -c sed -i 's/cat/dog/g'`
