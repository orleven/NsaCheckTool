#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'orleven'

import os
from blessings import Terminal
from core import controller
from core import arghandle


"""
NSA Check Tool (v.beta 1.1)  

脚本运行环境： 
    Linux系统
    wine
    python2.7
    python 模块包 argparse、blessings

NSA 工具所涉及到的漏洞，例如：永恒之蓝等等,检测的内容包含如下（主要针对445、3389）,如果需要保存到文件，使用重定向即可：
    ETERNALSYNERGY
    ETERNALBLUE
    ETERNALROMANCE
    ETERNALCHAMPION
    Eclipsedwing
    Educatedscholar
    Emeraldthread
    Doublepulsar
    Erraticgopher
    Esteemaudit
    Explodingcan

因为时间紧迫且缺少实验环境，以下的漏洞不能完全支持，只能判断漏洞不存在，如果您知道并成功测试，请完善controller.py 里配置对应的 "success" 的值。
    Educatedscholar
    Emeraldthread
    Erraticgopher

支持批量扫描，字典例子为： ip，例如：
    192.168.111.129
    192.168.111.165
    192.168.111.155
    192.168.111.154

PS: 
    1.Explodingcan（爆炸罐头）主要是针对IIS 6.0 漏洞，由于检测耗费时间有一点长，如果资产不涉及此应用，建议注释掉controller.py里关于Explodingcan的配置。
    2.如果需要保存到文件，使用重定向即可
"""

class Program(object):
    def __init__(self):
        self.term = Terminal()
        self.scriptPath = os.path.dirname(os.path.realpath(__file__))
        self.banner()
        self.arguments = arghandle.ArgHandle()
        hostList = self.arguments.getHostList()
        par = self.arguments.getParDic()

        if hostList!= None and  len(hostList) > 0:
            contro = controller.Controller(self.term,self.scriptPath,hostList,par)
            contro.working()
        else:
            print "Parameter format is not correct !\nPlease look for help e.g. -h"

    def banner(self):
        from pyfiglet import Figlet
        f = Figlet(font="slant")
        print self.term.bold_yellow(f.renderText("NSA Check Tool"))
        print self.term.bold_yellow("[version]: beta 1.1")

if __name__ == '__main__':
    Program()
