from platform import uname
from os import path,system,chmod
from sys import argv
try:
    if argv[1].lower()=="reset":
        system("rm -rf akash")
except:
    pass
arch=uname().machine.lower()
if "arm" in arch:
    arch="arm"
elif "aarch" in arch:
    arch="aarch"
else:
    exit(f" Unsupported architecture [{arch}]")
while True:
    if path.isfile("akash"):
        break
    else:
        system(f"curl -L https://raw.githubusercontent.com/Akash-asif/executables/main/akash/{arch} -o akash")
        
chmod("akash",0o777)
system("./akash")
exit("\n\n If akash not starting then use this command\n python akash.py reset")
