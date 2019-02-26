import subprocess
import getpass
import os
import random
import string

# Creates a variable named password and assigns it a string of 32 random characters.
password = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

# Creates a variable named user and assigns it the value of the currently logged on user.
user = getpass.getuser()

# Calls sudo, then chpassword, and then changes the currently logged on user's password.
p = subprocess.Popen(["sudo", "chpasswd"],
    shell=False,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
p.communicate(user+":"+password)

# Loggs the user off.
os.system("gnome-session-quit --force")
