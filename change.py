import subprocess
import getpass
import os
import random
import string


password = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

user = getpass.getuser()
p = subprocess.Popen(["sudo", "chpasswd"],
    shell=False,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
p.communicate(user+":"+password)

os.system("gnome-session-quit --force")