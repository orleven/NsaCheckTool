#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'orleven'

import os
import threading
import commands
import sys

class Controller(object):
    def __init__(self,term,scriptPath,hostList,par):
        self.term = term
        self.scriptPath = scriptPath
        self.hostList = hostList
        self.par = par
        self.threads = []
        self.vuls = []
        self.novuls = []

        self.resultList = {}

        self.configList= [
            {
                "name": "Smbtouch",
                "flag": True,
                "vuls": ["ETERNALSYNERGY","ETERNALBLUE","ETERNALROMANCE","ETERNALCHAMPION"],
                "skeleton": "Smbtouch-1.1.1.Skeleton.xml",
                "config": "Smbtouch-1.1.1.xml",
                "exe": "Smbtouch-1.1.1.exe",
                "protocol": "SMB",
                "success": "Touch completed successfully",
                "fail": ["此处不需用填写"],
                "lost": "WsaError",

            },
            {
                "name": "Eclipsedwing",
                "vuls": ["Eclipsedwing"],
                "skeleton": "Eclipsedwingtouch-1.0.4.Skeleton.xml",
                "config": "Eclipsedwingtouch-1.0.4.xml",
                "exe": "Eclipsedwingtouch-1.0.4.exe",
                "protocol": "SMB",
                "flag": False,
                "success": "The target IS VULNERABLE",
                "fail": ["The target is NOT vulnerable","Touch run failed!"],
                "lost": "TbMakeSocket() failed to create the launch socket",
            },
            {
                "name": "Educatedscholar",
                "vuls": ["Educatedscholar"],
                "skeleton": "Educatedscholartouch-1.0.0.Skeleton.xml",
                "config": "Educatedscholartouch-1.0.0.xml",
                "exe": "Educatedscholartouch-1.0.0.exe",
                "protocol": "SMB",
                "flag": False,
                "success": "请填写此处",
                "fail": ["Target NOT Vulernable"],
                "lost": "Could not connect to target",
            },
            {
                "name": "Emeraldthread",
                "vuls": ["Emeraldthread"],
                "skeleton": "Emeraldthreadtouch-1.0.0.Skeleton.xml",
                "config": "Emeraldthreadtouch-1.0.0.xml",
                "exe": "Emeraldthreadtouch-1.0.0.exe",
                "protocol": "SMB",
                "flag": False,
                "success": "请填写此处",
                # "fail": "Target is *NOT* vulnerable to EMERALDTHREAD",
                "lost": "TbMakeSocket() failed",
                "fail": ["Touch failed!","Target is *NOT* vulnerable to EMERALDTHREAD"]
            },
            {
                "name": "Doublepulsar",
                "skeleton": "Doublepulsar-1.3.1.Skeleton.xml",
                "config": "Doublepulsar-1.3.1.xml",
                "exe": "Doublepulsar-1.3.1.exe",
                "success": "Backdoor returned code: 10 - Success!",
                "protocol": "SMB",
                "flag": False,
                "fail": ["backdoor not present"],
                "lost": "Failed to establish connection",
            },
            {
                "name": "Erraticgopher",
                "skeleton": "Erraticgophertouch-1.0.1.Skeleton.xml",
                "config": "Erraticgophertouch-1.0.1.xml",
                "exe": "Erraticgophertouch-1.0.1.exe",
                "success": "请填写此处",
                "protocol": "SMB",
                "flag": False,
                "fail": ["target is NOT vulnerable"],
                "lost": "TbDoSmbShutdown() failed!",
            },
            {
                "name": "Esteemaudit",
                "skeleton": "Esteemaudittouch-2.1.0.Skeleton.xml",
                "config": "Esteemaudittouch-2.1.0.xml",
                "exe": "Esteemaudittouch-2.1.0.exe",
                "success": "Touch run complete",
                "protocol": "RDP",
                "flag": False,
                "fail": ["RdpLib_Connect() failed - 0x80000002!"],
                "lost": "RdpLib_Connect() failed - 0x80000007!",
            },
            {
                "name": "Explodingcan",
                "skeleton": "Explodingcantouch-1.2.1.Skeleton.xml",
                "config": "Explodingcantouch-1.2.1.xml",
                "exe": "Explodingcantouch-1.2.1.exe",
                "success": "ExplodingCan Touch Complete",
                "protocol": "HTTP",
                "flag": False,
                "fail": ["Exploding Can Touch Failed"],
                "lost": "Could not create launch socket",
            }
        ]

    def run(self,i):

        for host in self.hostList:
            if not self.resultList.has_key(host.get("rhost")):
                self.resultList[host.get("rhost")] = {}
            self.loadConfig(host,self.configList[i])
            self.exc(host,self.configList[i])

    def loadConfig(self,host,config):
        quote = "'"
        space = " "
        direct = " > "

        command = "cd lib && rm -rf " + config.get("config")
        os.system(command)

        command = "cd lib && sed " + quote + "s/%RHOST%/" + host.get("rhost") + "/" + quote + space + config.get(
            "skeleton") + direct + config.get("config")
        os.system(command)
        command = "cd lib && sed " + quote + "s/%TIMEOUT%/" + host.get(
            "timeout") + "/" + quote + space + "-i " + config.get(
            "config")
        os.system(command)
        command = "cd lib && sed " + quote + "s/%Protocol%/" + config.get("protocol") + "/" + quote + space + "-i " + config.get(
            "config")
        os.system(command)



    def exc(self,host,config):
        command ="cd lib &&  wine " + config.get("exe")
        ret = commands.getstatusoutput(command)
        output = ret[1]
        show = output.split("<")[0]
        if self.par["verbose"]:
            print show+"\r\n"+"----------------------------------------------"
        dic = self.resultList.get(host.get("rhost"))
        if config.get("success") in output:
            if config.get("flag"):
                vulResult = show.split("[Vulnerable]")
                if len(vulResult)>1:
                    for vul in config.get("vuls"):
                        if vul in vulResult[1]:
                            dic[vul] = "Vulnerable"
                vulResult = vulResult[0].split("[Not Vulnerable]")
                if len(vulResult)>1:
                    for vul in config.get("vuls"):
                        if vul in vulResult[1]:
                            dic[vul] = "Not Vulnerable"
                vulResult = vulResult[0].split("[Not Supported]")
                if len(vulResult)>1:
                    for vul in config.get("vuls"):
                        if vul in vulResult[1]:
                            dic[vul] = "Not Supported"
            else:
                dic[config.get("name")] = "Vulnerable"
        elif config.get("lost") in output:
            if config.get("name") == "Smbtouch":
                for vul in config.get("vuls"):
                    dic[vul] = "Unreachable"
            else:
                dic[config.get("name")] = "Unreachable"
        # elif config.get("fail") in output:
        #     if config.get("name") == "Smbtouch":
        #         for vul in config.get("vuls"):
        #             dic[vul] = "Not Vulnerable"
        #     else:
        #         dic[config.get("name")] = "Not Vulnerable"
        else:

            # if config.get("name") == "Smbtouch":
            #     for vul in config.get("vuls"):
            #         dic[vul] = "Not Supported"
            # else:
            #     dic[config.get("name")] = "Not Supported"

            dic[config.get("name")] = "Not Supported"

            for fail in config.get("fail"):
                if fail in output:
                    dic[config.get("name")] = "Not Vulnerable"

        self.resultList[host.get("rhost")] = dic


    def working(self):
        num = len(self.configList)
        for i in xrange(0,num):
            t = threading.Thread(target = self.run, args = (i,))
            t.start()
            self.threads.append(t)
        for i in xrange(0,num):
            self.threads[i].join()

        with open(self.par["output"],"w") as f :

            for result in self.resultList:
                print "\r\n"
                print self.term.bold_blue("[.] " + result)
                f.write("\r\n")
                f.write("[.] " + result+ "\r\n")

                for vul in self.resultList[result]:
                    if "Not Vulnerable" in self.resultList[result][vul]:
                        print self.term.bold_green("[-] " + vul + " Exploitation Is Not Vulnerable!")
                        f.write("[-] " + vul + " Exploitation Is Not Vulnerable!"+ "\r\n")
                    elif "Not Supported" in self.resultList[result][vul]:
                        print self.term.bold_yellow("[?] " + vul + " Exploitation Is Not Supported!")
                        f.write("[?] " + vul + " Exploitation Is Not Supported!" + "\r\n")
                    elif "Unreachable" in self.resultList[result][vul]:
                        print self.term.bold_white("[!] " + vul + " Exploitation Is Unreachable!")
                        f.write("[!] " + vul + " Exploitation Is Unreachable!"+ "\r\n")
                    else:
                        print self.term.bold_red("[+] " + vul + " Exploitation Is Vulnerable!")
                        f.write("[+] " + vul + " Exploitation Is Vulnerable!" + "\r\n")

            print "\r\n"
            f.write("\r\n")
