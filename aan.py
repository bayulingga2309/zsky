# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator
from PyDictionary import PyDictionary
from mergedict import MergeDict
from mergedict import ConfigDict
from pyowm import OWM
from enum import Enum 
#from django.http import HttpResponse
from random import randint
import time, random, sys, re, os, json
import urllib3
import certifi
import ssl
import html5lib,shutil
import subprocess as cmd
import csv
import os
import errno
import imp
import StringIO
import traceback
import linecache
import stat
import cStringIO
import urlparse
import logging
import argparse
#import mimic
import xml
import base64
import ast
from selenium import webdriver

import six

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

cl = LINETCR.LINE()
cl.login(token="EoqsJHouTdxe1cO6R5qa.fYGEY+OhxYNTkT0NKbud6G.5eCL92g1XzaTq31pGTk02bnRbLoh6KAGAgqd15SgcmA=")
cl.loginResult()

ki = LINETCR.LINE() #1
ki.login(token="EokJL3WLZGMBqsH1aLj3.NVEqbkE0eTU6xX4Nr9h20W.UJI/esAcuyquIkCwiU2139sl1gdnX1uM3okYDrQoBho=")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token="Eoc5iX7SZZTiYwZHEyJ7.24QHb1GfX0hmwXIVuZgJDW.ni7Sh+PG4vwUo/1P+U+kNF+rLkQcacdhQ16c0OkR2NA=")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token="EoWjFH1EpAPYYRNr54L9.DeXtwYuqoJU8Aoa2v6kRoq.+f9M2UE9SKemKaRCUu2wcG3b4/ILi+qA7u9IsO/Tkgo=")
kc.loginResult()

ks = LINETCR.LINE()
ks.login(token="EohQlGkOEwgA4CPL1Kt9.XmKY74LSTF1p3LQvDocmYq.57dmRBiFD+WfjCIwasJiMZUiWnRiKreIwo26RYsfAnY=")
ks.loginResult()

k1 = LINETCR.LINE()
k1.login(token="EoVKGwAMunsO6xKOQBaa.HUUIMlQNxdsmONvdTTHxIG.meuQqHdfAmW0BXDg8YLOPertbn019HS5Ks4mhAsIIGs=")
k1.loginResult()

k2 = LINETCR.LINE()
k2.login(token="EoAD5mz6KFbzidsLkqxd.AlE61U2dAf/57USGxrlx7q.pY/M6k/FhfDGzm4SYq/DE6wTY96JAlQ+Q3N7FUqRwPs=")
k2.loginResult()

k3 = LINETCR.LINE()
k3.login(token="EoOC7cF1gNIYqaC0o4q1.XGIyiGdITFvdTcC6/xyw8q.z+RotB5I7si3lxSBn8st87qH8PWhw1E9zdLTninUao8=")
k3.loginResult()

k4 = LINETCR.LINE()
k4.login(token=" EomZOpcgfoDc8cK6W8Y7.8hQ+tz/U7LjzpTtrOJFZvW.2l5fKQrUe2HAQZrSPmVv0kc76uS9yCjJaz0D1ph66lo=")
k4.loginResult()

k5 = LINETCR.LINE()
k5.login(token="EoVvmlGMdkKKbnVrBJh9.ndpqq7qTWifeaVk57HCbwq.nGMZlIfBNCgjjrVF6vVAp8FZHu456KuBgORyyA6Jn/o=")

satpam1 = LINETCR.LINE()  #linggga
satpam1.login(token="EoXHf5q7gxXiPv0skutf.fDP3x5LMIJAXGy0kDKt5+W.ruL+DjzYl74kQnkxv3um0Y1UYWJfwINoGNwWFZHJwOY=")
satpam1.loginResult()


print "login success bos"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ

╔═════════════
║   ◄]·♦·Menu For Public·♦·[►
║╔════════════
║╠[•]Help
║╠[•]Key
║╠[•]Mimin
║╠[•]Creator
║╠[•]Time
║╠════════════
║╠[•]Say....
║╠[•]Wkwkwk/Wkwk/Wk
║╠[•]Hehehe/Hehe/He
║╠[•]Galau
║╠[•]You
║╠[•]Hadeuh
║╠[•]Please
║╠[•]Haaa
║╠[•]Lol
║╠[•]Hmmm/Hmm/Hm
║╠[•]Welcome
║╠[•]Woy
║╠════════════
║╠[•]Wiki 
║╠[•]Lyric
║╠[•]Instagram
║╠[•]Music
║╠[•]Youtube
║╠[•]Vidio
║╠════════════
║╠[•]Bc
║╠[•]Up
║╠[•]Berapa besar cinta
║╠[•]Apakah
║╠[•]Siapakah cewek 
║╠[•]Siapakah cowok
║╠[•]Adakah
║╠[•]Cakepkah
║╠════════════
║╠[•]T-eng
║╠[•]T-japan 
║╠[•]T-thai
║╠[•]T-id
║╚════════════
║ Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ
╚═════════════
"""
Keyowner ="""
╔═════════════
║ Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ
╠═════════════
║   ◄]·♦·Menu For Admin·♦·[►
║╔════════════
║╠[•]Kick ...
║╠[•]Invite (by mid)
║╠[•]Undang (Invite by kontak)
║╠[•]Tarik/Jepit (Invite by kontak)
║╠[•]Adminlist
║╠[•]Bot Add @
║╠[•]Spam... (spam on 10 tes)
║╠[•]Bot? (cek kontak bot)
║╠[•]Cancel (cncl undngn trtunda)
║╠[•]clean invites
║╠[•]clear invites
║╠════════════
║╠[•]Message change:...
║╠[•]Message add:...
║╠[•]Message
║╠[•]Comment:...
║╠[•]Add comment:...
║╠════════════
║╠[•]Jam on/off
║╠[•]Change clock
║╠[•]Jam Update
║╠════════════
║╠[•]Status (cek status room)
║╠[•]Cctv
║╠[•]Intip
║╠[•]Toong
║╠[•]Nk
║╠[•]Tajong
║╠[•]Vkick
║╠[•]Emak/Abah
║╠[•]Kill
║╠[•]Absen/Respon
║╠════════════
║╠[•]Ifconfig
║╠[•]System
║╠[•]Cpu
║╠[•]Kernel
║╠[•]Debug speed
║╠[•]Bot speed
║╠[•]Speed respon
║╠[•]Sp turunin
║╠[•]Sp naikin
║╠[•]Turun lagi
║╠[•]Spbot
║╠[•]Sp asli
║╠[•]Speedbot
║╠[•]Speed
║╚════════════
║ Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ
╚═════════════
"""
Setgroup ="""
╔═════════════
║ Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ
╠═════════════
║   ◄]·♦·Menu For Admin·♦·[►
║╔════════════
║╠[•]Cancel
║╠[•]Buka qr/Open qr
║╠[•]link open
║╠[•]Tutup qr/Close qr
║╠[•]link close
║╠[•]Rejectall (reject semua invite)
║╠[•]Protect:hight/low
║╠[•]Auto blockqr:off/on
║╠[•]Namelock:on/off
║╠[•]Blockinvite:on/off
║╠[•]Joinn on/off (kick protect join)
║╠[•]Cancel on/off(cncl all undngan)
║╠[•]Qr on/off (protect qr)
║╠[•]Contact On/off
║╠[•]Join on/off (auto join bot)
║╠[•]Gcancel:on/off (invite grup)
║╠[•]Leave on/off
║╠[•]Share on/off
║╠[•]Add on/off
║╠[•]Cancelall (canccel all invite)
║╠[•]Comment off/on
║╠[•]Backup:on/off
║╠[•]Mode on
║╠════════════
║╠[•]Info Group
║╠[•]ginfo
║╠[•]Group id
║╠[•]TL:....
║╠[•]Gn
║╠[•]LG
║╠[•]LG2
║╠[•]group list
║╠════════════
║╠[•]My mid
║╠[•]Mid Bot
║╠[•]Bot restart
║╠[•]Turn off bots
║╠[•]Allbio: (ganti bio stat bot)
║╠[•]Myname: (ganti nama bot)
║╠════════════
║╠[•]Banlist
║╠[•]Cek ban
║╠[•]Kill ban
║╠[•]Blacklist @ 
║╠[•]Banned @
║╠[•]Mid @"
║╠[•]Unban @
║╠[•]Ban
║╠[•]Unban
║╠════════════
║╠[•]Steal group pict
║╠[•]Steal cover @
║╠[•]Midpict:..
║╠[•]Steal pict 
║╠[•]Steal bio
║╠[•]Steal mid
║╠[•]Steal contact
║╠[•]Mimic on/off
║╠[•]Targetlist
║╠[•]Mimic target
║╠[•]Target @
║╠[•]Del target @
║╠[•]copy @
║╠[•]Backup
║╠════════════
║╠[•]Spamcontact @
║╠[•]GBc
║╠[•]Pm cast
║╠[•]Bot like
║╠════════════
║╠[•]One piece
║╠[•]Kabur all
║╠[•]Kabur
║╠[•]Bot kadieu
║╠[•]Asupka:
║╠[•]Invite me
║╠════════════
║╠[•]Remove all chat
║╠[•]Admin add @ (by tag)
║╠[•]Admin remove @
║╠[•]Cleanse
║╠[•]Ready op
║╠[•]Greet
║╚════════════
║ Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ
╠═════════════
"""
KAC=[cl,ki,kk,kc,ks,k1,k2,k3,k4,k5]
DEF=[ki,kk,kc,ks,k1,k2,k3,k4,k5]
kicker=[satpam1]
mid = cl.getProfile().mid 
Amid = ki.getProfile().mid 
Bmid = kk.getProfile().mid 
Cmid = kc.getProfile().mid 
Dmid = ks.getProfile().mid 
Emid = k1.getProfile().mid
Fmid = k2.getProfile().mid
Gmid = k3.getProfile().mid
Hmid = k4.getProfile().mid
Imid = k5.getProfile().mid
Smid1 = satpam1.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
induk=[mid]
Creator=["u15da775f99668a36b1818d0a7644f9ff"]
admin=["u2c1bd948e598a0cf1315aefc1e1a0f79","ufb26ef4375cb21ad3f762f8e26b67d11","ueb8dd347e531ab0c7cdd28fe19461833","u518745f362a03f99d7f43bf386f2fbd9","ua39d2f19ef4874476722a30c337247d6","u6dc83f54c240eaa0cf90bc6c80015603","u017043023d41299924ff3cf9271e5e3e","u2833b0608d39405b37fa69a5141ca127","u8d7f5f6959ab3711aeca4cf3c9682d8e","uf0cf3743b0c73b3daf0152683512ae18","ub76a498ab8760f1e280a784c7949b796","u6ec720003a2bc6defce8a8c036483d44","uf407c45bcc144b4f500ac5d4b6d2b8f9","udbe7fad195cbbdef7d61fbca16ae65f4","u78b98e255f0d40e96a0a208088d48749","u15da775f99668a36b1818d0a7644f9ff","u5922a5de980d24fa90b3c57a3fd86e18","ubc27c2d853659ffa0d3dca69e781a381","ub8ce9a0e16a457aff34c9427eba3a0bb","u8fb37e6221f3050b92f8ec51482e6c1d","u0bbf2cfa8ebc5abf9a43322fb9ee512e","ueb44ec47ae559d25dd3a332dc7e68669","u134b7a47b9b8a14a7fbea4e9b4652807","u9c0d8892eb488bad5f228ef9187900b7","u96c8117797972801d52cb0f528d6de08","u3050b18d7059ab9bed603dc3d4a1eb96","u6ec720003a2bc6defce8a8c036483d44","u52198d07559fb8a5ec91f2809e9ca9d4","u6c315426f230bb17f64232e6bca56228","uf407c45bcc144b4f500ac5d4b6d2b8f9","u58a73da7e0446cca8a13f78c888f1776","u97326643c6d54ebf62997093d48416a9","uf3e918a10e65d5662bd1a05d9ef14fed","ueb90b5cf4ad851eb3dbb090b3a9f6bb1","u0a9a5aab2eb2c48858714fffd9eb6501","uc27eb33827fdd155c48e3ff4f19b4dd0","ub8ad41d531c50f9bf0046a0edc5681c3","u80e001d052ceaef5fda75ee33725be46","udbe7fad195cbbdef7d61fbca16ae65f4","ucab5f5dfc251eaa8791d218495a5a513","u96ea7f2c1e87e7af9ec03f1453608ea0","u8fb37e6221f3050b92f8ec51482e6c1d","u3daa595c7df397ad2e2edfe8ab38cfbf","ufe763dfb064d1594ffa56eee6b2a0618","u2ff2e80f81ecaccc5c761647f3cb6573","u00ac50671c6128943fbe595abfcc08c4","u516b107eb00d6827946642dfe44279f0","u317bb3aa422353af6a1d0eeaebcaa868","u0fdae0ad9c4d4274d52381eac54066fb","u36c43e4527b9f524b8786ae2a20d2e72","ua5143a761257e124b2c18aadb13528dc","uc969d66d3f0b9483d5df49477deee1c8","uaea971fa376607280d555fae98fdbc56","u672a98aeb3acbb02f88f3490f7226729","ue07dc1ad0a920040df88cd86502e3d6d","u1c7067b70baa00878cf5b873683b8df1","u1f84cf8751a75a719d4421c9f2b26f9b","u24535cc4cb6b79c9a6b764bf8d6a70a6","u5fbc3d9b970aff4935db3da167bf29a7","ueb44ec47ae559d25dd3a332dc7e68669","ue07dc1ad0a920040df88cd86502e3d6d"] #Krisna,kris,
owner=["ua39d2f19ef4874476722a30c337247d6","u017043023d41299924ff3cf9271e5e3e","ub07f6d4181b2e0c4f04d6e416efcc075","u0452d018812c8a8b3027fc58e65ceba9","u8d7f5f6959ab3711aeca4cf3c9682d8e","u15da775f99668a36b1818d0a7644f9ff","ubc27c2d853659ffa0d3dca69e781a381","ub8ce9a0e16a457aff34c9427eba3a0bb"]
#staff=["u2833b0608d39405b37fa69a5141ca127","u8d7f5f6959ab3711aeca4cf3c9682d8e","ub76a498ab8760f1e280a784c7949b796","u6ec720003a2bc6defce8a8c036483d44","uf407c45bcc144b4f500ac5d4b6d2b8f9","udbe7fad195cbbdef7d61fbca16ae65f4","u78b98e255f0d40e96a0a208088d48749","u15da775f99668a36b1818d0a7644f9ff","u5922a5de980d24fa90b3c57a3fd86e18","ubc27c2d853659ffa0d3dca69e781a381","ub8ce9a0e16a457aff34c9427eba3a0bb","u8fb37e6221f3050b92f8ec51482e6c1d","u0bbf2cfa8ebc5abf9a43322fb9ee512e","ueb44ec47ae559d25dd3a332dc7e68669","u134b7a47b9b8a14a7fbea4e9b4652807","u9c0d8892eb488bad5f228ef9187900b7","u96c8117797972801d52cb0f528d6de08","u3050b18d7059ab9bed603dc3d4a1eb96","u6ec720003a2bc6defce8a8c036483d44","u52198d07559fb8a5ec91f2809e9ca9d4","u6c315426f230bb17f64232e6bca56228","uf407c45bcc144b4f500ac5d4b6d2b8f9","u58a73da7e0446cca8a13f78c888f1776","u97326643c6d54ebf62997093d48416a9","uf3e918a10e65d5662bd1a05d9ef14fed","ueb90b5cf4ad851eb3dbb090b3a9f6bb1","u0a9a5aab2eb2c48858714fffd9eb6501","uc27eb33827fdd155c48e3ff4f19b4dd0","ub8ad41d531c50f9bf0046a0edc5681c3","u80e001d052ceaef5fda75ee33725be46","udbe7fad195cbbdef7d61fbca16ae65f4","ucab5f5dfc251eaa8791d218495a5a513","u96ea7f2c1e87e7af9ec03f1453608ea0","u8fb37e6221f3050b92f8ec51482e6c1d","u3daa595c7df397ad2e2edfe8ab38cfbf","ufe763dfb064d1594ffa56eee6b2a0618","u2ff2e80f81ecaccc5c761647f3cb6573","u00ac50671c6128943fbe595abfcc08c4","u516b107eb00d6827946642dfe44279f0","u317bb3aa422353af6a1d0eeaebcaa868","u0fdae0ad9c4d4274d52381eac54066fb","u36c43e4527b9f524b8786ae2a20d2e72","ua5143a761257e124b2c18aadb13528dc","uc969d66d3f0b9483d5df49477deee1c8","uaea971fa376607280d555fae98fdbc56","u672a98aeb3acbb02f88f3490f7226729","ue07dc1ad0a920040df88cd86502e3d6d","u1c7067b70baa00878cf5b873683b8df1","u1f84cf8751a75a719d4421c9f2b26f9b","u24535cc4cb6b79c9a6b764bf8d6a70a6","u5fbc3d9b970aff4935db3da167bf29a7","ueb44ec47ae559d25dd3a332dc7e68669","ue07dc1ad0a920040df88cd86502e3d6d"] #Krisna,kris,
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪""",
    "lang":"JP",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "namelock":True,
    "Backup":True,
    "AutoKick":False,
    "Mimic":False,
    "pname":True,
    "qr":True,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "protectionOn":True,
    "Protectcancel":True,
    "winvite":False,
    "winvite2":False,
    "Tag":True,
    "Sider":{},
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
} 
wait3 = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
profile = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
profile = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
profile = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
profile = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
profile = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k1.getProfile()
backup = k1.getProfile()
profile = k1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k2.getProfile()
backup = k2.getProfile()
profile = k2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k3.getProfile()
backup = k3.getProfile()
profile = k3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k4.getProfile()
backup = k4.getProfile()
profile = k4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

contact = k5.getProfile()
backup = k5.getProfile()
profile = k5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

setTime = {}
setTime = wait2['setTime']


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def mention2(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def MENTION(to,nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nama:
     akh = akh + 2
     aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
     strt = strt + 6
     akh = akh + 4
     bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[COMMAND] Tag All"
    try:
      cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
          with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
      else:
          raise Exception('Download Audio failure.')
      try:
          self.sendAudio(to_, path)
      except Exception as e:
        print e

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)       
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += '\n ☞ ' + Name
                    wait2['ROM'][op.param1][op.param2] = '☞ ' + Name
            else:
                pass
#-------------------------------------------
 #       if op.type == 55:
 #               try:
 #                   if cctv['cyduk'][op.param1]==True:
 #                       if op.param1 in cctv['point']:
#                            Name = cl.getContact(op.param2).displayName
#                            if Name in cctv['sidermem'][op.param1]:
#                                pass
#                            else:
#                                cctv['sidermem'][op.param1] += "\n• " + Name
#                                if " " in Name:
#                                    nick = Name.split(' ')
#                                    if len(nick) == 2:
#                                        kk.sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
#                                    else:
#                                        kk.sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
#                                else:
#                                    kk.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
#                        else:
#                            pass
#                    else:
#                        pass
#                except:
#                    pass
#
#        else:
#            pass    	      
#------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ks.getGroup(op.param1)
				    except:
					try:
                                            G = k1.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ks.updateGroup(G)
                                    except:
                                        try:
                                            k1.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        kk.sendText(op.param1,"please do not change group name-_-")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
#=============================================================================
        #------Protect Group Kick finish-----#
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["Protectgr"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    ki.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 11:
            if wait["Protectgr"] == True:
                if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.kickoutFromGroup(op.param1,[op.param3])
                    cl.updateGroup(G)
        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              try:
                random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                random.choice(KAC).sendText(op.param1, "sᴇʙᴇʟᴜᴍ ɪɴᴠɪᴛᴇ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ɢʀᴏᴜᴘ😛")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              except:
                random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
         #       random.choice(KAC).sendText(op.param1, "ᴍᴀᴜ ɴɢᴜɴᴅᴀɴɢ sɪᴀᴘᴀ ᴋᴀ?\nᴋᴋ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ\nᴊᴀᴅɪ ᴀᴋᴜ ᴄᴀɴᴄᴇʟ😛")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Creator:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Creator:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Creator:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Creator:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Creator:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Creator:
		    k5.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Dmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Emid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Fmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Gmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Hmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Imid:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Dmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Emid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Fmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Gmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Hmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Imid:
		    ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Dmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Emid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Fmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Gmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Hmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Imid:
		    kk.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Bmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Dmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Emid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Fmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Gmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Hmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Imid:
		    kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in Dmid:
		if op.param2 in mid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Amid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Bmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Cmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Emid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Fmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Gmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Hmid:
		    ks.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Imid:
		    ks.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in Emid:
		if op.param2 in mid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Amid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Bmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Cmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Dmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Fmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Gmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Hmid:
		    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		if op.param2 in Imid:
		    k1.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in Fmid:
		if op.param2 in mid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Amid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Bmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Cmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Dmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Emid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Gmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Hmid:
		    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		if op.param2 in Imid:
		    k2.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Gmid:
		if op.param2 in mid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Amid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Bmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Cmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Dmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Emid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Fmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Hmid:
		    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		if op.param2 in Imid:
		    k3.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Hmid:
		if op.param2 in mid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Amid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Bmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Cmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Dmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Emid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Fmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Gmid:
		    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		if op.param2 in Imid:
		    k4.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Imid:
		if op.param2 in mid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Amid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Bmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Cmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Dmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Emid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Fmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Gmid:
		    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		if op.param2 in Hmid:
		    k5.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Emid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k1.acceptGroupInvitation(op.param1)
                else:
                  k1.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Fmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k2.acceptGroupInvitation(op.param1)
                else:
                  k2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Gmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k3.acceptGroupInvitation(op.param1)
                else:
                  k3.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Hmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k4.acceptGroupInvitation(op.param1)
                else:
                  k4.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Imid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  k5.acceptGroupInvitation(op.param1)
                else:
                  k5.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Bots:
			    pass
		        if op.param2 in Bots:
			    pass
		        else:
		            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
			    kk.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass
		
#-----------------------------------------------------------------
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
			kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
			k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ks.updateGroup(G)
                    Ti = ks.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
			kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k1.updateGroup(G)
                    Ti = k1.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
			k3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k2.updateGroup(G)
                    Ti = k2.reissueGroupTicket(op.param1)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k1.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
			k4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k3.updateGroup(G)
                    Ti = k3.reissueGroupTicket(op.param1)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k2.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
			k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k4.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k4.updateGroup(G)
                    Ti = k4.reissueGroupTicket(op.param1)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k3.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
			kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = k5.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    k5.updateGroup(G)
                    Ti = k5.reissueGroupTicket(op.param1)
                    k4.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k4.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    k5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = k5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    k5.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

#--------------------------------------------------------
                if Smid1 in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.kickoutFromGroup(op.param1,[op.param2])
			random.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    satpam1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#--------------------------------------------------------
        if op.type == 19:
            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in admin or owner:
              if op.param2 in Bots:
                try:
                  cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  k1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True

            if op.param3 in induk:
              if op.param2 not in Bots:
                try:
                  random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                  cl.acceptGroupInvitationt(op.param1)
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
#-----------------------------------------------
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in Bots:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
#--------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
#--------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite2"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = random.choice(KAC).getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 random.choice(KAC).sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 random.choice(KAC).sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 random.choice(KAC).sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     random.choice(KAC).findAndAddContactsByMid(target)
                                     random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                     wait["winvite2"] = False
                                     break
                                 except:
                                     try:
                                         random.choice(KAC).findAndAddContactsByMid(invite)
                                         random.choice(KAC).inviteIntoGroup(op.param1,[invite])
                                         wait["winvite2"] = False
                                     except:
                                         random.choice(KAC).sendText(msg.to,"Error Boss, di tunggu beberapa saat lagi boss")
                                         wait["winvite2"] = False
                                         break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        ki.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        kk.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        ks.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        kc.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k1.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k2.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k3.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k4.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k5.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        ks.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        ki.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        kk.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        ks.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        kc.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        k1.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        k2.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        k3.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        k4.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        k5.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        ki.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        kk.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        ks.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        kc.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        k1.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        k2.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        k3.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        k4.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")
                        k5.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ sᴜᴄᴄᴇssғᴜʟ")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        ki.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        kk.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        ks.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        kc.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k1.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k2.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k3.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k4.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        k5.sendText(msg.to,"ᴢs ʙᴀɴɴᴇᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴇʟᴇᴛᴇᴅ")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        ks.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Zs:help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Zs:key"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Keyowner)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Zs:admin"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Zs:mode add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Zs:mode add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = k1.getGroup(msg.to)
                gs = k2.getGroup(msg.to)
                gs = k3.getGroup(msg.to)
                gs = k4.getGroup(msg.to)
                gs = k5.getGroup(msg.to)
                gs = satpam1.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            ki.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            kk.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            kc.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            ks.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            k1.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            k2.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            k3.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            k4.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                            k5.sendText(msg.to,"ᴍᴏᴅᴇ sᴜᴄᴄᴇs ᴀᴅᴅ")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"ᴘᴇʀɪɴᴛᴀʜ ᴅɪᴛᴏʟᴀᴋ.")
                cl.sendText(msg.to,"Hʜᴀɴʏᴀ ᴏᴡɴᴇʀ ʏᴀɴɢ ʙɪsᴀ ɢᴜɴᴀɪɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ.")
                
            elif "Zs:mode dell @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("ᴍᴏᴅᴇ ʀᴇᴍᴏᴠᴇ sᴜᴄᴇs..","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = k1.getGroup(msg.to)
                gs = k2.getGroup(msg.to)
                gs = k3.getGroup(msg.to)
                gs = k4.getGroup(msg.to)
                gs = k5.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            ki.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            kk.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            kc.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            ks.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            k1.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            k2.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            k3.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            k4.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                            k5.sendText(msg.to,"ᴍᴏᴅᴇ ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜs")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"ᴘᴇʀɪɴᴛᴀʜ ᴅɪᴛᴏʟᴀᴋ.")
                cl.sendText(msg.to,"ʜᴀɴʏᴀ ᴏᴡɴᴇʀ ʏᴀɴɢ ʙɪsᴀ ɢᴜɴᴀɪɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ.")
                
            elif msg.text in ["Zs:modelist","Modelist"]:
              if admin == []:
                  cl.sendText(msg.to,"ᴛʜᴇ sᴛᴀғғʟɪsᴛ ɪs ᴇᴍᴘᴛʏ")
              else:
                  cl.sendText(msg.to,"ᴡᴀɪᴛɪɴɢ......")
                  mc = "ᴍᴏᴅᴇ ᴏɴ ᴀᴅᴍɪɴ ✰ ᴛᴇᴀᴍ ᴢs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ✰||\n=============\n"
                  for mi_d in admin:
                      mc += "✒️" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            
            elif msg.text in ["Admin list","admin list"]:
                if admin == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"
#batas__________________

            elif "zs" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Zs:staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
#---------------------------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = k1.getGroup(msg.to)
                  gs = k2.getGroup(msg.to)
                  gs = k3.getGroup(msg.to)
                  gs = k4.getGroup(msg.to)
                  gs = k5.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        k1.findAndAddContactsByMid(target)
                        k2.findAndAddContactsByMid(target)
                        k3.findAndAddContactsByMid(target)
                        k4.findAndAddContactsByMid(target)
                        k5.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")                
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k1.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k2.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k3.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k4.getProfile()
                    profile.statusMessage = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k5.getProfile()
                    profile.statusMessage = string
                    k5.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"Update Name Menjadi : " + string + "")
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam " in msg.text:
              if msg.from_ in admin and owner:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
    #-----------------=Selesai=------------------
            elif msg.text in ["Zs:bots"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                k1.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                k2.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                k3.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                k4.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                k5.sendMessage(msg)
#====================================================
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Zs:cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = ks.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ks.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ks.sendText(msg.to,"No one is inviting")
                        else:
                            ks.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ks.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Zs:mid all" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                k1.sendText(msg.to,Emid)
                k2.sendText(msg.to,Fmid)
                k3.sendText(msg.to,Gmid)
                k4.sendText(msg.to,Hmid)
                k5.sendText(msg.to,Imid)
#--------------------------------- GIFT -------------------------------------
            elif msg.text.lower() in ["gift","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '40ed630f-22d2-4ddd-8999-d64cef5e6c7d',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#----------------------------------------------------------------------------                
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Invite:on"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
#==================================================
            elif 'Lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('Lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'Wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("Wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == 'Kr restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'Ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'System':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'Kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'Cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif 'Instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("Instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'Music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('Music ','')
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            elif 'Clean invites' in msg.text.lower():
               if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#================================================================================
            elif 'Clear invites' in msg.text.lower():
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                        cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif 'Link open' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================================================
         
            elif 'Link close' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#============================================================
          
            elif msg.text.lower() == 'Ginfo':
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[display name]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nmembers:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
#===============================================================
            elif 'Zs:gruplist' in msg.text.lower():
              if msg.from_ in admin:
                gs = cl.getGroupIdsJoined()
                L = "『 Groups List 』\n"
                for i in gs:
                    L += "[≫] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
 
            elif "Zs:invitemeto" in msg.text:
              if msg.from_ in owner:
                         gid = cl.getGroupIdsJoined()
		         for i in gid:
			        cl.findAndAddContactsByMid(msg.from_)
                                cl.inviteIntoGroup(i,[msg.from_])
			        cl.sendText(msg.to, "successfully invited you to all groups")
            elif "Turn off bots" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#==================================================================
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)

#===========================================================
            elif "T-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-eng ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "T-japan " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-japan ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ja')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate japan'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "T-thai " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-thai ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'th')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate thai'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "T-id " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("T-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except Exception as error: 
                    cl.sendText(msg.to,(error))          

            elif "Zs:say " in msg.text:
              if msg.from_ in  admin:
				bctxt = msg.text.replace("Zs:say ","")
				cl.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
				k1.sendText(msg.to,(bctxt))
				k2.sendText(msg.to,(bctxt))
				k3.sendText(msg.to,(bctxt))
				k4.sendText(msg.to,(bctxt))
				k5.sendText(msg.to,(bctxt))
#==========================================================================	
            elif msg.text in ["Zs:mode on","mode on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"ᴢs  ǫʀ ᴄᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ")
                    else:
                        random.choice(KAC).sendText(msg.to,"ᴢs  ǫʀ ᴄᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ")
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ᴢs  ᴀʟʟ ɪɴᴠɪᴛᴇs ʜᴀs ʙᴇᴇɴ ʀᴇᴊᴇᴄᴛᴇᴅ")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴄᴀɴᴄᴇʟ ᴀʟʟ ɪɴᴠɪᴛᴇs ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴄᴀɴᴄᴇʟ ᴀʟʟ ɪɴᴠɪᴛᴇs ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴋɪᴄᴋ ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴛᴜʀɴᴇᴅ ɪɴᴛᴏ ʜɪɢʜ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ")
                    else:
                        cl.sendText(msg.to,"ᴢs ᴛᴜʀɴᴇᴅ ɪɴᴛᴏ ʜɪɢʜ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ")
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴛᴜʀɴᴇᴅ ɪɴᴛᴏ ʜɪɢʜ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ")
                    else:
                        cl.sendText(msg.to,"ᴢs ᴛᴜʀɴᴇᴅ ɪɴᴛᴏ ʜɪɢʜ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ")
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ǫʀ ᴘʀᴏ ᴏɴ")
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ǫʀ ᴘʀᴏ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"ᴢs ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ᴢs ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                else:
                    cl.sendText(msg.to,"ᴢs ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                    wait['pname'][msg.to] = True
                    wait['pname'][msg.to] = cl.getGroup(msg.to).name
              if msg.from_ in admin:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴀᴛɪᴏɴ ᴏɴ")
				if msg.to in protection:
					cl.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ Protect ᴏɴ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏɴ")
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʏᴀɴɢ ᴄᴀɴᴄᴇʟ ᴜɴᴅᴀɴɢᴀɴ ᴋᴀᴍɪ ᴋɪᴄᴋ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʏᴀɴɢ ᴄᴀɴᴄᴇʟ ᴜɴᴅᴀɴɢᴀɴ ᴋᴀᴍɪ ᴋɪᴄᴋ")
                    else:
                        cl.sendText(msg.to,"done")
#==========================================================================	
            elif msg.text in ["Zs:mode off","mode off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴄᴀɴᴄᴇʟ ᴀʟʟ ɪɴᴠɪᴛᴀᴛɪᴏɴ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴄᴀɴᴄᴇʟ ᴀʟʟ ɪɴᴠɪᴛᴀᴛɪᴏɴ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴋɪᴄᴋ ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴋɪᴄᴋ ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴏғғ")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off")
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off")
                    else:
                        cl.sendText(msg.to,"Already off")
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection")
                    else:
                        cl.sendText(msg.to,"turned into low protection")
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection")
                    else:
                        cl.sendText(msg.to,"turned into low protection")
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ɴᴀᴍᴇʟᴏᴄᴋ ᴏғғ")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ɴᴀᴍᴇʟᴏᴄᴋ ᴏғғ")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ")
                    else:
                        cl.sendText(msg.to,"done")

            if "Zs:mode off" == msg.text:
              if msg.from_ in admin:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ᴢs ɪɴᴠɪᴛᴀᴛɪᴏɴ ᴏғғ")
				except:
					pass
	
            if "Zs:mode off" == msg.text:
				try:
					if msg.from_ in admin:
						protection.remove(msg.to)
						cl.sendText(msg.to,"ᴢs ᴘʀᴏᴛᴇᴄᴛ ᴛᴜʀɴᴇᴅ ᴏғғ")
					else:
						cl.sendText(msg.to,"ᴢs ɴᴏ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴘʀᴏᴛᴇᴄᴛ")
				except:
					pass

#==========================================================================	
            elif msg.text in ["Zs:invite on","invite on"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
#======================================
            elif msg.text in ["Protect:hight","protect:hight"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection")
                    else:
                        cl.sendText(msg.to,"turned into high protection")
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:off","auto blockqr:off"]:
              if msg.from_ in admin:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:on","auto blockqr:on"]:
              if msg.from_ in admin:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:low","Protect:low"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
					
            elif "Blockinvite:on" == msg.text:
              if msg.from_ in admin:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
              if msg.from_ in admin:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass
					
            elif "Protect on" == msg.text:
				if msg.to in protection:
					cl.sendText(msg.to,"Protect ᴀʟʀᴇᴀᴅʏ ᴏɴ")
				else:
					wait["pnharfbot"][msg.to] = cl.getGroup(msg.to).name
					f=codecs.open('pnharfbot.json','w','utf-8')
					json.dump(wait["pnharfbot"], f, sort_keys=True, indent=4,ensure_ascii=False)
					protection.append(msg.to)
					cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏɴ")
            elif "Protect off" == msg.text:
				try:
					if msg.from_ in admin:
						protection.remove(msg.to)
						cl.sendText(msg.to,"Protect ᴛᴜʀɴᴇᴅ ᴏғғ")
					else:
						cl.sendText(msg.to,"Protect ᴀʟʀᴇᴀᴅʏ ᴏғғ")
				except:
					pass
 #================================================================           
            elif msg.text in ["Zs:invite"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["Tarik"]:
              if msg.from_ in admin:
                 wait["winvite2"] = True
                 random.choice(KAC).sendText(msg.to,"Kirim contact Boss")
            elif msg.text in ["Jepit"]:
              if msg.from_ in admin:
                 wait["winvite2"] = True
                 random.choice(KAC).sendText(msg.to,"Kirim contact Boss")
#============================================================
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)#=================
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Invite on","invite on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Invite off","Invite off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join on","Auto join on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","Auto join off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç���¨è‡ªåŠ¨é‚€è¯·æ���’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Leave on","Auto leave:on"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Leave off","Auto leave:off"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","status"]:
              if msg.from_ in admin:
                md = "  zѕ ρяσтє¢тισи ѕтαтυѕ\n  *===============*\n"
                if wait["Protectgr"] == True: md+="⌚️ ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏɴ\n\n"
                else: md+="⌚ ️ ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏғғ\n\n"
                if wait["Protectcancl"] == True: md+="⌚️ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ\n\n"
                else: md+="⌚ ️ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏғғ\n\n"
                if wait["contact"] == True: md+="⌚️ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ\n\n"
                else: md+="⌚️ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ\n\n"
                if wait["autoJoin"] == True: md+="⌚️ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ\n\n"
                else: md +="⌚️ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏғғ\n\n"
                if wait["pname"] == True: md+="⌚️ ɴᴀᴍᴇʟᴏᴄᴋ ᴏɴ\n\n"
                else: md +="⌚️ ɴᴀᴍᴇʟᴏᴄᴋ ᴏғғ\n\n"
                if wait["Sider"] == True: md+="⌚️ sɪᴅᴇʀ ᴏɴ\n\n"
                else: md +="⌚️ sɪᴅᴇʀ ᴏғғ\n\n"
                if wait["autoCancel"]["on"] == True:md+="⌚️ ɢʀᴏᴜᴘ ᴄᴀɴᴄᴇʟ ᴏɴ" + str(wait["autoCancel"]["members"]) + "\n\n"
                else: md+= "⌚️ ɢʀᴏᴜᴘ ᴄᴀɴᴄᴇʟ ᴏғғ\n\n"
                if wait["leaveRoom"] == True: md+="⌚️ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ\n\n"
                else: md+="⌚️ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏғғ\n\n"
                if wait["timeline"] == True: md+="⌚️ sʜᴀʀᴇ ᴏɴ\n\n"
                else:md+="⌚️ sʜᴀʀᴇ ᴏғғ\n\n"
                if wait["autoAdd"] == True: md+="⌚️ ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ\n\n"
                else:md+="⌚️ ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ\n\n"
                if wait["Backup"] == True: md+="⌚️ ʙᴀᴄᴋᴜᴘ : on\n\n"
                else:md+="⌚️ ʙᴀᴄᴋᴜᴘ : ᴏғғ\n\n"
                if wait["qr"] == True: md+="⌚️ ᴀᴜᴛᴏʙʟᴏᴄᴋ ǫʀ: on\n\n"
                else:md+="⌚️ ᴀᴜᴛᴏʙʟᴏᴄᴋ ǫʀ : ᴏғғ\n\n"
                if wait["commentOn"] == True: md+="⌚️ ᴄᴏᴍᴍᴇɴᴛ ᴏɴ\n\n"
                else:md+="⌚️ ᴄᴏᴍᴍᴇɴᴛ ᴏғғ\n\n"
                if wait["Protectcancel"] == True: md+="⌚️ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ\n\n"
                else: md+="⌚️ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏғғ\n\n"
                if wait["protectionOn"] == True: md+="⌚️ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ : ʜɪɢʜᴛ\n\n"
                else:md+="⌚️ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ : ʟᴏᴡ\n"
                "\n*============*\n⭐✰ Ŧ€ΔΜ ŽŞ ƤŘØŦ€ĆŦƗØŇ ✰⭐\n*============*"
                cl.sendText(msg.to,md)
            elif "Time" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif "Album merit " in msg.text:
                gid = msg.text.replace("Album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç���¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "Album " in msg.text:
                gid = msg.text.replace("Album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "Album remove " in msg.text:
                gid = msg.text.replace("Album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "Album removeat’" in msg.text:
                gid = msg.text.replace("Album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Add on","Auto add:on"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Add off","Auto add:off"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#-----------------------------------------------
            elif msg.text in ["Zs:backup on"]:
              if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup has been active")
                        ki.sendText(msg.to,"Backup has been active")
                        kk.sendText(msg.to,"Backup has been active")
                        kc.sendText(msg.to,"Backup has been active")
                        ks.sendText(msg.to,"Backup has been active")
                        k1.sendText(msg.to,"Backup has been active")
                        k2.sendText(msg.to,"Backup has been active")
                        k3.sendText(msg.to,"Backup has been active")
                        k4.sendText(msg.to,"Backup has been active")
                        k5.sendText(msg.to,"Backup has been active")
                    else:
                        cl.sendText(msg.to,"Backup has been active")
                        ki.sendText(msg.to,"Backup has been active")
                        kk.sendText(msg.to,"Backup has been active")
                        kc.sendText(msg.to,"Backup has been active")
                        ks.sendText(msg.to,"Backup has been active")
                        k1.sendText(msg.to,"Backup has been active")
                        k2.sendText(msg.to,"Backup has been active")
                        k3.sendText(msg.to,"Backup has been active")
                        k4.sendText(msg.to,"Backup has been active")
                        k5.sendText(msg.to,"Backup has been active")
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Zs:backup off"]:
              if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Rejectall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All Invites has been Rejected")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
#---------------------Sc invite owner ke group------
            elif "Zs:inviteme: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("Zs:invitene: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#=======================================================================
            elif msg.text.lower() in ["!bot"]:
                    beb = "ʙᴏᴛs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ sᴜᴅᴀʜ ʟᴇɴɢᴋᴀᴘ sᴇᴍᴜᴀ ᴋᴏᴍᴀɴᴅᴀɴ 😘 " +cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ki.sendText(msg.to,beb)
                    kk.sendText(msg.to,beb)
                    kc.sendText(msg.to,beb)
                    ks.sendText(msg.to,beb)
                    k1.sendText(msg.to,beb)
                    k2.sendText(msg.to,beb)
                    k3.sendText(msg.to,beb)
                    k4.sendText(msg.to,beb)
                    k5.sendText(msg.to,beb)
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 1:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#
            elif msg.text in ["Zs:sp"]:
              if msg.from_ in admin:
                cl.sendText(msg.to, "ʀɪʟᴇx sʟᴏᴡ ʀᴇsᴘᴏɴs...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))   
                ki.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                kk.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                kc.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                ks.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                k1.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                k2.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                k3.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                k4.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                k5.sendText(msg.to, "%sseconds" % (elapsed_time)) 
                print "[Command]Speed palsu executed"
#========================================
            elif msg.text in ["Bot1 backup run"]:
                if msg.from_ in admin:
                    wek = cl.getContact(mid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(a)
                    u.close()
                    cl.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot2 backup run"]:
                if msg.from_ in admin:
                    wek = ki.getContact(Amid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myesm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfs.txt',"w")
                    u.write(a)
                    u.close()
                    ki.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot3 backup run"]:
                if msg.from_ in admin:
                    wek = kk.getContact(Bmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('msgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysfdgm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('gymyps.txt',"w")
                    u.write(a)
                    u.close()
                    kk.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot4 backup run"]:
                if msg.from_ in admin:
                    wek = kc.getContact(Cmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('jhmydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myhfsm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfhs.txt',"w")
                    u.write(a)
                    u.close()
                    kc.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot5 backup run"]:
                if msg.from_ in admin:
                    wek = ks.getContact(Dmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('madydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysgjm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myrdps.txt',"w")
                    u.write(a)
                    u.close()
                    ks.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot6 backup run"]:
                if msg.from_ in admin:
                    wek = k1.getContact(Emid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydnsgv.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('jhmysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myiyps.txt',"w")
                    u.write(a)
                    u.close()
                    k1.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
#==============================================

            elif msg.text == "Cctv":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Cek CCTV di proses......")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Toong":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Di Read Oleh||%s\n||By : ✰ ᴛᴇᴀᴍ ᴢs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ✰||\n\n>Pelaku CCTV<\n%s-=CCTV=-\n•Bintitan\n•Panuan\n•Kurapan\n•Kudisan\n\nAmiin Ya Allah\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketik Toong\nDASAR PIKUN ♪")
                        
            elif msg.text == "Cctv":
              if msg.from_ in admin:
                    cl.sendText(msg.to, "Siap di intip....")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,'%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "[Command] Reset"

            elif msg.text == "Intip":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print "[Command] Check"
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✔ ✰ ᴛᴇᴀᴍ ᴢs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ✰\nRead : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.strftime(now2,'%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "[Command] reset"
                    else:
                        cl.sendText(msg.to,"Read point tidak tersedia, Silahkan ketik Cctv untuk membuat Read point.")                        
#-----------------------------------------------
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Zs:in","!!!"]: #Panggil Semua Bot
              if msg.from_ in owner:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                satpam1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                cl.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                ki.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                kk.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))   
                kc.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                ks.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                k1.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                k2.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                k3.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                k4.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                k5.sendText(msg.to,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ sᴀʜᴀʙᴀᴛ " + str(ginfo.name))
                print "Semua Sudah Lengkap"
                        

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Zs:out","---"]: #Semua Bot Ninggalin Group Kecuali Bot Induk
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"ᴛʜᴀɴᴋᴢ ғᴏʀ ғᴏᴜɴᴅᴇʀ ɢʀᴏᴜᴘs\n"  +  str(ginfo.name)  + "\nʙʏ:ᴢs ᴘʀᴏᴛᴇᴄᴛɪᴏɴ")
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Emak"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["Abah"]:
            	 if msg.from_ in admin:              
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    mention2(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                 if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                 if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention2(msg.to, nm4)
                 if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention2(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention2(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention2(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention2(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention2(msg.to, nm5)
                 if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                 cnt = Message()
                 cnt.text = "Done : " + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)                      
                     
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                
                              
            elif "Greet" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Greet","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    ki.sendText(msg.to,"maaf kalo gak sopan")
                    kk.sendText(msg.to,"makasih semuanya..")
                    kc.sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,ks,k1,k2,k3,k4,k5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")
                                
            elif msg.text in ["Salam1"]:
                ki.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                ki.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
              if msg.from_ in owner:
                ki.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Assalamu'alaikum")
                ki.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                kk.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    ki.sendText(msg.to,"maaf kalo gak sopan")
                    k2.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    k3.sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,ks,k1,k2,k3,k4,k5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                kk.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                kc.sendText(msg.to,"Nah salamnya jawab sendiri dah")
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Zs:kick " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Zs:kick ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    random.choice(KAC).sendText(msg.to,"Maaf ya....")
                      
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                  targets.append(x["M"])
                for target in targets:
                  try:
                    cl.kickoutFromGroup(msg.to,[target])
                  except:
                    cl.sendText(msg.to,"Error")
                                    
            elif "Cium " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                  targets.append(x["M"])
                for target in targets:
                  try:
                    k1.kickoutFromGroup(msg.to,[target])
                  except:
                    k1.sendText(msg.to,"Error")
                    
            elif "Nakal " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nakal ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                satpam1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        satpam1.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        satpam1.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
                        
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Prohibited Banned Bot")
                        ki.sendText(msg.to,"Prohibited Banned Bot")
                        kk.sendText(msg.to,"Prohibited Banned Bot")
                        kc.sendText(msg.to,"Prohibited Banned Bot")
                        ks.sendText(msg.to,"Prohibited Banned Bot")
                        k1.sendText(msg.to,"Prohibited Banned Bot")
                        k2.sendText(msg.to,"Prohibited Banned Bot")
                        k3.sendText(msg.to,"Prohibited Banned Bot")
                        k4.sendText(msg.to,"Prohibited Banned Bot")
                        k5.sendText(msg.to,"Prohibited Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k1.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                k5.sendText(msg.to,"P ��􀆶squared up!􏿿")
                k5.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#
#----------------------------[Spam To Contact]----------------------------#WORK 
            elif "Spamcontact @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam") 
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       cl.sendText(g.mid,"Ini Adalah Spam")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       kk.sendText(g.mid,"Jangan Ngintip")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       k1.sendText(g.mid,"Masuk Room Woy...!!!")
                       cl.sendText(msg.to, "Target Spam, Done...!!!")
                       kk.sendText(msg.to, "Target Spam, Done...!!!")
                       k1.sendText(msg.to, "Target Spam, Done...!!!")
                       print " Spammed !"
#----------------------------[Spam To Contact]----------------------------#WORK 
       #--------------------Start-----------------------#       
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)		
                k1.sendText(msg.to,jawaban)		                
                kk.sendText(msg.to,jawaban)		                
            elif "Berapa besar cinta " in msg.text:
                tanya = msg.text.replace("Berapa besar cinta ","")
                jawab = ("0%","25%","50%","75%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)                
                kk.sendText(msg.to,jawaban)		                
                kk.sendText(msg.to,jawaban)		                
            elif "Siapakah cewek " in msg.text:
                tanya = msg.text.replace("Siapakah cewek ","")
                jawab = ("Maryati􀜁�","Ida􀜁�","Uke􀜁�","Alyn􀜁�","Ikka􀜁�","Yunikey􀜁�","Qwenie􀜁�","Gendis􀜁�","Aryani􀜁�","Nindy􀜁�","Wina􀜁�","Dewi􀜁�","Ifah􀜁�")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                ki.sendText(msg.to,jawaban)
                ki.sendText(msg.to,jawaban)
            elif "Siapakah cowok " in msg.text:
                tanya = msg.text.replace("Siapakah cowok ","")
                jawab = ("Arjun􀜁�","Ahmad khan􀜁�","Hajir􀜁�","Dd􀜁�","Indra􀜁�","Jeong􀜁�","Yogi􀜁�","Ary􀜁�","Ucil􀜁�")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                ki.sendText(msg.to,jawaban)
                k5.sendText(msg.to,jawaban)
            elif "Adakah " in msg.text:
                tanya = msg.text.replace("Adakah ","")
                jawab = ("Tidak tahu.","Ada.","Tidak ada.","Mungkin ada")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                k3.sendText(msg.to,jawaban)	                
                k3.sendText(msg.to,jawaban)	                             
            elif "Cakepkah " in msg.text:
                tanya = msg.text.replace("Cakepkah ","")
                jawab = ("Jelek.","Cakep.","Lumayan.","Kaya jembut.")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                k1.sendText(msg.to,jawaban)	         
                k1.sendText(msg.to,jawaban)	                       
       #-------------------Finish-----------------------#
        #-------------Fungsi Broadcast Start------------#
            elif "GBc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                bctxt = msg.text.replace("GBc ","")
                a = cl.getGroupIdsJoined()
                a = ki.getGroupIdsJoined()
                a = kk.getGroupIdsJoined()
                a = kc.getGroupIdsJoined()
                a = ks.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  ki.sendText(taf, (bctxt))
                  kk.sendText(taf, (bctxt))
                  kc.sendText(taf, (bctxt))
                  ks.sendText(taf, (bctxt))
        #-------------Fungsi Broadcast Start------------#
            elif msg.text in ["LG"]: #Melihat List Group
              if msg.from_ in admin:
                gids = cl.getGroupIdsJoined()
                h = ""
                for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                  cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                  h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                  cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Zs:leave all"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                gid = k1.getGroupIdsJoined()
                gid = k2.getGroupIdsJoined()
                gid = k3.getGroupIdsJoined()
                gid = k4.getGroupIdsJoined()
                gid = k5.getGroupIdsJoined()
                for i in gid:
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                  k1.leaveGroup(i)
                  k2.leaveGroup(i)
                  k3.leaveGroup(i)
                  k4.leaveGroup(i)
                  k5.leaveGroup(i)
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
  #------------------------End---------------------
#-------------------------------------------------
            elif "Pm cast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Broadcast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Broadcast ", "")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt +"\n\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName))
  #-----------------End-----------
            elif msg.text in ["hai","Hai"]:
                ki.sendText(msg.to,"Hai Every Body 􀜁􀅔Har Har􏿿")

            elif msg.text in ["nah","Nah"]:
                ki.sendText(msg.to,"Kan")
            elif msg.text in ["salam","Assalamualaikum"]:
                ki.sendText(msg.to,"Walaikumsalam wr wb.")
            elif msg.text in ["Pagi","pagi"]:
                ki.sendText(msg.to,"Hai met pagi juga kak :v")
            elif msg.text in ["typo","Typo"]:
                ki.sendText(msg.to,"Mending lu hapus akun aja :v")
#-----------------------------------------------)
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Zs:absen","Zs:respon"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                kk.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                kc.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                ks.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                cl.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                k1.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                k2.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                k3.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                k4.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                k5.sendText(msg.to,"ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴛᴇᴀᴍ ᴢs ɪs ᴘʀᴇsᴇɴᴛ ᴛᴏ ᴋᴇᴇᴘ ᴛʜᴇ ɢʀᴏᴜᴘ")
                random.choice(KAC).sendText(msg.to,"ᴛʜᴀɴᴋs ғᴏʀ ᴀʟʟᴏᴡɪɴɢ ᴜs ʜᴇʀᴇ")
      #-------------Fungsi Respon Finish---------------------#
            elif msg.text in ["Gruplist"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup══���══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)         
#==========================================
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
           
            	    ki.sendText(msg.to,text)
                    kc.sendText(msg.to,text)
                    kk.sendText(msg.to,text)
                    ks.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			kk.sendMessage(msg)
            			ki.sendMessage(msg)
			        kc.sendMessage(msg)
            			ks.sendMessage(msg)
            			
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			kk.sendMessage(msg)
            			ki.sendMessage(msg)
                                kc.sendMessage(msg)
                                ks.sendMessage(msg)         

            
#            elif msg.text in ["Target list"]:
#              if msg.from_ in admin:
#                        if mimic["target"] == {}:
#                            cl.sendText(msg.to,"nothing")
#                        else:
#                            mc = "Target mimic user\n"
#                            for mi_d in mimic["target"]:
#                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
#                            cl.sendText(msg.to,mc)

         
#            elif "Mimic:" in msg.text:
#	          if msg.from_ in admin:
#            		  cmd = msg.text.replace("Mimic:","")
#            		  if cmd == "on":
#            			  if mimic["status"] == False:
#            				  mimic["status"] = True
#            				  cl.sendText(msg.to,"turning on mimic")
#            				
#            			  else:
#            				  cl.sendText(msg.to,"mimic have been enable")
            				
#            		  elif cmd == "off":
#            			  if mimic["status"] == True:
#            				  mimic["status"] = False
#            				  cl.sendText(msg.to,"turning off mimic")
#            				
#            			  else:
#            				  cl.sendText(msg.to,"Mimic have been desable")
            				
#            		  elif "Mimic target " in cmd:
#                            if msg.from_ in admin:
#                                      target0 = msg.text.replace("Mimic target ","")
#            			      target1 = target0.lstrip()
#            			      target2 = target1.replace("@","")
#            			      target3 = target2.rstrip()
#            			      _name = target3
#            			      gInfo = cl.getGroup(msg.to)
#            			      targets = []
#            			      for a in gInfo.members:
#                               	              if _name == a.displayName:
#            				              targets.append(a.mid)
#            			      if targets == []:
#            				     cl.sendText(msg.to,"No targets")
#            				
#            			      else:
#                			      for target in targets:
#            					      try:
#            						      mimic["target"][target] = True
#            						      cl.sendText(msg.to,"Success added target")
#            						
#            						      #cl.sendMessageWithMention(msg.to,target)
#            						      break
#            					      except:
#            						      cl.sendText(msg.to,"Failed")
#            						
#            						      break
#            		  elif "Untarget " in cmd:
#                            if msg.from_ in admin:
#            			      target0 = msg.text.replace("Untarget ","")
#            			      target1 = target0.lstrip()
#            			      target2 = target1.replace("@","")
#            			      target3 = target2.rstrip()
#            			      _name = target3
#            			      gInfo = cl.getGroup(msg.to)
#            			      gInfo = ki.getGroup(msg.to)
#            			      targets = []
#            			      for a in gInfo.members:
#            				      if _name == a.displayName:
#            					      targets.append(a.mid)
#            			      if targets == []:
#            				      cl.sendText(msg.to,"No targets")
            				
#            			      else:
#            				      for target in targets:
#            					      try:
#            						      del mimic["target"][target]
#            						      cl.sendText(msg.to,"Success deleted target")
            					
            						      #cl.sendMessageWithMention(msg.to,target)
#            						      break
#            					      except:
#            						      cl.sendText(msg.to,"Failed!")            

#==========================================

            elif msg.text in ["Mimic on","mimic on","Mimic:on"]:
                if msg.from_ in admin:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic off","Mimic:off"]:
                if msg.from_ in admin:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list","Targetlist"]:
                if msg.from_ in admin:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                if msg.from_ in admin:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                if msg.from_ in admin:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                if msg.from_ in admin:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#==========================================
#=======================================
            elif msg.text in ["Backup","backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    ki.updateDisplayPicture(backup.pictureStatus)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    k1.updateDisplayPicture(backup.pictureStatus)
                    k2.updateDisplayPicture(backup.pictureStatus)
                    k3.updateDisplayPicture(backup.pictureStatus)
                    k4.updateDisplayPicture(backup.pictureStatus)
                    k5.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    ki.updateProfile(backup)
                    kk.updateProfile(backup)
                    kc.updateProfile(backup)
                    ks.updateProfile(backup)
                    k1.updateProfile(backup)
                    k2.updateProfile(backup)
                    k3.updateProfile(backup)
                    k4.updateProfile(backup)
                    k5.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                    k1.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    ki.sendText(msg.to, str(e))
                    kk.sendText(msg.to, str(e))
                    kc.sendText(msg.to, str(e))
                    ks.sendText(msg.to, str(e))
                    k1.sendText(msg.to, str(e))
                    k2.sendText(msg.to, str(e))
                    k3.sendText(msg.to, str(e))
                    k4.sendText(msg.to, str(e))
                    k5.sendText(msg.to, str(e))
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    ki.CloneContactProfile(target)
                                    kk.CloneContactProfile(target)
                                    kc.CloneContactProfile(target)
                                    ks.CloneContactProfile(target)
                                    k1.CloneContactProfile(target)
                                    k2.CloneContactProfile(target)
                                    k3.CloneContactProfile(target)
                                    k4.CloneContactProfile(target)
                                    k5.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif msg.text in ["Kembali awal"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    k1.updateDisplayPicture(backup.pictureStatus)
                    k1.updateProfile(backup)
                    k2.updateDisplayPicture(backup.pictureStatus)
                    k2.updateProfile(backup)
                    k3.updateDisplayPicture(backup.pictureStatus)
                    k3.updateProfile(backup)
                    k4.updateDisplayPicture(backup.pictureStatus)
                    k4.updateProfile(backup)
                    k5.updateDisplayPicture(backup.pictureStatus)
                    k5.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    ki.sendText(msg.to, str (e))
                    kk.sendText(msg.to, str (e))
                    kc.sendText(msg.to, str (e))
                    ks.sendText(msg.to, str (e))
                    k1.sendText(msg.to, str (e))
                    k2.sendText(msg.to, str (e))
                    k3.sendText(msg.to, str (e))
                    k4.sendText(msg.to, str (e))
                    k5.sendText(msg.to, str (e))
#--------------------------------------------------------
            elif "rejectall" in msg.text:
                    X = cl.getGroupIdsInvited()
                    for i in X:           	    
			cl.rejectGroupInvitation(i)
#--------------------------------------------------------
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#
            elif ("Vkick" in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")
							
       #-------------Fungsi Speedbot Start---------------------#
            elif "Zs:banall" in msg.text:                  
                       nk0 = msg.text.replace("Zs:banall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")
      #-------------Fungsi Speedbot Finish---------------------#
      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Zs:ban"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                kk.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                kc.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                ks.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                k1.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                k2.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                k3.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                k4.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
                k5.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʙᴀɴɴᴇᴅ")
            elif msg.text in ["Zs:unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                kk.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                kc.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                ks.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                k1.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                k2.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                k3.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                k4.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
                k5.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ᴜɴʙᴀɴɴᴇᴅ")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u15da775f99668a36b1818d0a7644f9ff'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"ɪᴛᴜ ᴄʀᴇᴀᴛᴏʀ ᴋᴀᴍɪ ʏᴀɴɢ ᴋᴀʟᴇᴍ ᴡᴋᴡᴋ")  
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Koplak Lu','Muka Lu Kaya Jembut','Ada Orang kah disini?','Ada Janda Yang Bisa Di Ajak Mojok Gak, Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Zs:kilban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    random.choice(KAC).sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
	      if msg.from_ in owner:
		cl.removeAllMessages(op.param2)
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		kc.removeAllMessages(op.param2)
		ks.removeAllMessages(op.param2)
		k1.removeAllMessages(op.param2)
		k2.removeAllMessages(op.param2)
		k3.removeAllMessages(op.param2)
		k4.removeAllMessages(op.param2)
		k5.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat Finish")
#---------------------------
#KICK_BY_TAG
        elif "Boom " in msg.text:
          if msg.from_ in Creator:
            if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', msg.text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                print mentionees
                for mention in mentionees:
                    cl.kickoutFromGroup(msg.to,[mention['M']])
                    ki.kickoutFromGroup(msg.to,[mention['M']])
                    kk.kickoutFromGroup(msg.to,[mention['M']])
                    kc.kickoutFromGroup(msg.to,[mention['M']])
                    ks.kickoutFromGroup(msg.to,[mention['M']])
#===========================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#        if op.param1 in autocancel:
#			OWN = "ua7fc5964d31f45ac75128fc2b8deb842","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","uc7f32bb28dc009916d40af87c9910ddc"
#			if op.param2 in OWN:
#				pass
#			else:
#				Inviter = op.param3.replace("",',')
#				InviterX = Inviter.split(",")
#				contact = cl.getContact(op.param2)
#				cl.cancelGroupInvitation(op.param1,InviterX)
#				ki.cancelGroupInvitation(op.param1,InviterX)
#				kk.cancelGroupInvitation(op.param1,InviterX)
#				ks.cancelGroupInvitation(op.param1,InviterX)
#				kc.cancelGroupInvitation(op.param1,InviterX)
#				ka.cancelGroupInvitation(op.param1,InviterX)
#				cl.kickoutFromGroup(op.param1,[op.param2])
#				ki.kickoutFromGroup(op.param1,[op.param2])
#				kk.kickoutFromGroup(op.param1,[op.param2])
#				ks.kickoutFromGroup(op.param1,[op.param2])
#				kc.kickoutFromGroup(op.param1,[op.param2])
#				ka.kickoutFromGroup(op.param1,[op.param2])
#				wait["blacklist"][op.param2] = True
#				f=codecs.open('st2__b.json','w','utf-8')
#				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = "u15da775f99668a36b1818d0a7644f9ff","u8d7f5f6959ab3711aeca4cf3c9682d8e","u0452d018812c8a8b3027fc58e65ceba9","ub8ce9a0e16a457aff34c9427eba3a0bb"
			if op.param2 in Bots and admin:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				k1.kickoutFromGroup(op.param1,[op.param2])
				k2.kickoutFromGroup(op.param1,[op.param2])
				k3.kickoutFromGroup(op.param1,[op.param2])
				k4.kickoutFromGroup(op.param1,[op.param2])
				k5.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#===========================================
#        if op.type == 26:
#            if "@"+cl.getProfile().displayName in msg.text:
#                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
#                jawab = ("Jgn Tag Gw woyy!!\nlagi ngocok dulu...!!!","Berisik jgn tag Gw Koplak","Gw Sibuk, Gausah di Tag!!!","Ngapain tag neh,, kangen yah...!!!")
#                jawaban = random.choice(jawab)
#                cl.sendText(msg.to,jawaban)
                
#        elif "@"+cl.getProfile().displayName in msg.text:
#            try:
#                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
#                jawab = ("Jgn Tag Si "+cl.getProfile().displayName+"Ta cipok luh..!!","Berisik jgn tag si "+cl.getProfile().displayName+" dia lagi asyik ngocok...!!!")
#                jawaban = random.choice(jawab)
#                random.choice(KAC).sendText(msg.to,jawaban)
#                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
#            except:
#                pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
#        if op.type == 17:
#          if op.param2 in Bots:
#            return
#          ginfo = cl.getGroup(op.param1)
#          random.choice(KAC).sendText(op.param1, "Welcome\nSelamat Datang Di  " + str(ginfo.name))
#          random.choice(KAC).sendText(op.param1, "Founder =>>> " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
#          random.choice(KAC).sendText(op.param1, "😊 Semoga Betah Kk 😘\nNo Baper,No nakal,No Ngeyel ya,No Bulshit")
#          print "MEMBER HAS JOIN THE GROUP"
#        if op.type == 15:
#          if op.param2 in Bots:
#             return
#          random.choice(KAC).sendText(op.param1, "Baper Tuh Orang :v\nBelum di Anu Kayanya 😊")
#          print "MEMBER HAS LEFT THE GROUP"
#--------------------------------------------------------
#        if 'MENTION' in mid or Amid or Bmid or Cmid or Dmid or Emid or Fmid or Gmid or Hmid or Imid:
#          cl.sendtext(msg.to,'[Auto Respon]\nngapain tag, pc langsung aja...!!!')
#          pass
#--------------------------------------------------------
#Restart_Program
        elif msg.text in ["Bot restart"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Bot has been restarted")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
#--------------------------------------------------------




        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          k1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          k1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          k2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          k2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          k3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          k3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,500):
        hasil = cl.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    k5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    k1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    k2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    k3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（���ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Boss"
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5)
            time.sleep(600)
        except:
            pass
         
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
