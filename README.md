# NSA Check Tool (v.beta 1.1)  

## 脚本运行环境： 
    Linux系统
    wine
    python2.7
    python 模块包 argparse、blessings
    

## 检查内容
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
    

## 其他 

1. 支持批量扫描，字典例子为： ip，例如：
    192.168.111.129
    192.168.111.165
    192.168.111.155
    192.168.111.154

2. 因为时间紧迫且缺少实验环境，以下的漏洞不能完全支持，只能判断漏洞不存在，如果您知道并成功测试，请完善controller.py 里配置对应的 "success" 的值。
    Educatedscholar
    Emeraldthread
    Erraticgopher

3. Explodingcan（爆炸罐头）主要是针对IIS 6.0 漏洞，由于检测耗费时间有一点长，如果资产不涉及此应用，建议注释掉controller.py里关于Explodingcan的配置。

