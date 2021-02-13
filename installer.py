#!/data/data/com.termux/files/usr/bin/python3

from os import system as command

print("Installing everything needet")
command("pkg install python; pkg install python3; pip install termcolor; pkg install termux-api; pkg install curl;cp TermFun /data/data/com.termux/files/usr/bin && cp TermFunListener /data/data/com.termux/files/usr/bin ;cd /sdcard; curl https://f-droid.org/repo/com.termux.api_47.apk -O; pm install com.termux.api_47.apk; pkg install nmap;")
command("clear")
print("The Termux-API apk  was placed on your /sdcard install it please.")
print("You can also download the Termux-API from the appstore if you want.")
print("But Remember Termux cant run correctly without the termux-api apk.")

from termcolor import colored as c

print(c("You can now run TermFun by typing TermFun in the Terminal"))
