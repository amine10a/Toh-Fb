g ='\033[92m'
r ='\033[91m'
b ='\033[94m'
y ='\033[93m'
w = '\033[0m'
m = '\033[95m'
bl = '\033[96m'
import subprocess
import time
import os
subprocess.Popen("python $HOME/Toh-Fb/install.py", shell=True).wait() 
os.system('clear')
subprocess.Popen("clear ", shell=True).wait()
time.sleep(1)
print(b,"-------------------------------------------------------------")
print(g)
os.system('figlet Toh-Fb')
print(y,'tools of hacking - facebook',w)
print(r,'author:',w,' Mr amine10a')
print(r,'youtube channel',w,'https://m.youtube.com/channel/UCDbwhUmCPpRZwpFGI96yX4A')
print(b,"--------------------------------------------------------------")
print(g,'[',w,'1',g,'] hack facebook with brute force and getting information for id')
print(g,'[',w,'2',g,'] phishing Social media')
print(g,'[',w,'3',g,'] exit')
print(y)
x = int(input('enter your choice: '))
os.system('clear')
print(r,'Loading...')
print(w)
time.sleep(2)
if x == 1 :
	subprocess.Popen("python2 $HOME/Toh-Fb/dark-fb/dark.py", shell=True).wait()
if x == 2 :
	subprocess.Popen("bash $HOME/Toh-Fb/shellphish/shellphish.sh", shell=True).wait()
if x == 3 :
   print('exiting')
   exit()
else :
	print("the programme is deat")
	exit()

