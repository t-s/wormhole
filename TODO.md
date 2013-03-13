& before a line means item has been done.

1. &Add ability to cp files, and not just scp.
2. Add ability to scp files to different hosts given watched directory.
3. Include possibility of using Expect to handle password entry. 
4. &Automatically find user name of logged in user, use by default.
5. &Else, parse out and use specified user name.
6. Add ability to specify remote directory destination. Key on slash character, as colons can be in hostnames, but slashes cannot be.
7. Identify groups of files closely related in time and scp all of these in one transfer session.
8. Alternatively, look into keeping SCP open in some way, so it sends files as soon as they appear. Look at http://gnuru.org/article/1522/copying-with-scp-stdin https://internal.lboro.ac.uk/mail/public/lulu/2002-10/msg00021.html http://superuser.com/questions/291829/how-do-i-scp-the-huge-output-of-a-command-directly-to-a-remote-machine
9. Catch exceptions besides interrupt - kill, for example. (is this the same interrupt as crtl-C?)
