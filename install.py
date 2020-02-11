# author : Mr amine10a
# youtube channel :
# facebook page : http://www.facebook.com/Mr.amine10a
b ='\033[94m'
import subprocess
import time
subprocess.Popen("apt install php && apt install curl && apt install git && apt install figlet && apt install python2 && apt install wget && apt install unzip  -y ", shell=True).wait()
# install requirements
subprocess.Popen(" pip install requests  ", shell=True).wait()
subprocess.Popen(" pip2 install requests  ", shell=True).wait()
# git scripts
subprocess.Popen(" git clone https://github.com/amine10a/shellphish", shell=True).wait()
subprocess.Popen("git clone https://github.com/V4N654T/dark-fb ", shell=True).wait()
# install ngrok 
subprocess.Popen(" wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip ", shell=True).wait()
subprocess.Popen("unzip ngrok-stable-linux-arm.zip ", shell=True).wait()
subprocess.Popen("rm -rf ngrok-stable-linux-arm.zip ", shell=True).wait()
subprocess.Popen("cp ngrok $HOME/Toh-Fb/shellphish", shell=True).wait()
print(b,'you can creat account for ngrok ')
auth = input('please paste your authtoken for ngrok here: ')
subprocess.Popen("$HOME/Toh-Fb/shellphish/ngrok authtoken",auth, shell=True).wait()
print(w)
# my youtube channel
print(b,'please go to subscriber my channel')
time.sleep(3)
subprocess.Popen("termux-open-url https://m.youtube.com/channel/UCDbwhUmCPpRZwpFGI96yX4A ", shell=True).wait()
subprocess.Popen("rm -rf $HOME/Toh-Fb/install.py", shell=True).wait()




