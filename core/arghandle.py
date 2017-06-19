#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'orleven'

import argparse
import re
import os

class ArgHandle:
    def __init__(self):
        self.hostList = []
        self.par = {}
        self.parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        self.argSet()
        self.handle()


    def argSet(self):
        self.parser.add_argument("-H", "--host", type=str, help="Target host ip address", default=None)
        self.parser.add_argument("-T", "--timeout", type=str, help="Timeout", default="10")
        self.parser.add_argument("-V", "--verbose", help="Verbosity", action="store_true", default=False)
        self.parser.add_argument("-L", "--load",type=str, help="Load ip dictionary", default=None)
        self.parser.add_argument("-O", "--output", type=str, help="output to txt", default="result.txt")

    def handle(self):
        args = self.parser.parse_args()
        file = args.load
        rhost = args.host
        timeout = args.timeout
        verbose = args.verbose
        output = args.output
        p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
        if file != None :
            if os.path.isfile(file):
                with open(file,'r') as f :
                    for line in f.readlines():
                        myline = line.strip('\r').strip('\n')
                        values = myline.split(":")
                        hostDic = {}
                        if p.match(values[0]):
                            hostDic["timeout"] = timeout
                            hostDic["rhost"] = values[0]
                            self.hostList.append(hostDic)
            else:
                print "The path is not exist!"

        elif rhost != None and p.match(rhost):
            hostDic = {
                "rhost": rhost,
                "timeout": timeout,
            }
            self.hostList.append(hostDic)

        self.par["output"] = output
        self.par["verbose"] = verbose


    def getHostList(self):
        return self.hostList

    def getParDic(self):
        return self.par