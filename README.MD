Welcome to Version 1 of a simple Port Scanner built on Python3.


Do not use Python2.....!!!

What the scanner is capable of?

1. Port Scanning
2. Service Detection
3. Domain to IP conversion

Dependencies:

[+]  Python3

[+]  pyfiglet

[+]  termcolor

[+]  socket

[+]  optparse

[+]  threading

[+]  datetime

[+]  os

[+]  platform

#In case of any dependency error use python3 -m pip install packagename.

For Example:

python3 -m pip install pyfiglet


Usage: 

python3 scanner.py --host <targetip> --port <target ports>

#For Example:

python3 scanner.py --host 192.168.146.45 --port 80,139,443,445

python3 scanner.py --host 192.168.146.45 --port 80-445

python3 scanner.py --host 192.168.146.45 --port 1-65535

This is version 1 and might have some bugs.

Please reach out to me on Twitter @deltsandtraps or email me @ abhishekrautela@protonmail.com for any bugs or queries.

THANK YOU.
BE KIND :)
