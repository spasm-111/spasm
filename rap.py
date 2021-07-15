import os
import  re, os,time,getpass,sys
from platform import system
print ("\33[95m hello +_+")
print ('[1] rap')
print ('[2] sad')
print ('[3] gust')
s = input ('Enter Here : ')
if s == '1':
    print ('[1] didin')
    print ('\33[0;31m[2] you')
    a = input ('\33[95mEnter Here : ')
    if a == '1':
        print ('\33[95m ok ')
        os.system('termux-media-player play /data/data/com.termux/files/home/spasm/spasm.mp3')
    elif a == '2':
        print ('\33[95mrou7 3end mou7')
        os.system('xdg-open https://instagram.com/spasm_111?igshid=ntufxicx6es')
    else:
        print ('\33[0;31mnot spasm !!')
elif s == '2':
    print ('Ok')
    os.system('termux-media-player play /data/data/com.termux/files/home/spasm/hack.mp3')
elif s == '3':
    print ('Ok')
    os.system('termux-media-player play /data/data/com.termux/files/home/spasm/tegga.mp3')
else:
    print ('\33[0;31mnot spasm !!')