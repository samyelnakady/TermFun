#!/data/data/com.termux/files/usr/bin/python3

from os import system as command

print("Installing everything needet")
command("pkg install python; pkg install python3; pip install termcolor; pkg install termux-api; pkg install curl; cd /sdcard; curl https://f-droid.org/repo/com.termux.api_47.apk -O; pm install com.termux.api_47.apk; pkg install nmap")
command("clear")
print("The Termux-API apk  was placed on your /sdcard install it please.")
print("You can also download the Termux-API from the appstore if you want.")
print("But Remember Termux cant run correctly without the termux-api apk.")
