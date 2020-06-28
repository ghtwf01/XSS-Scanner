# XSS-Scanner功能
多线程反射型XSS扫描(可同时扫描多个url，也可指定一个扫描)
# 使用教程
--u1 指定第一个url
--u2 指定第二个url
--u3 指定第三个url
example:
python XSS-Scanner.py --u1 http://127.0.0.1/xss.php?a= --u2 http://192.168.1.2/xxss.php?b= --u3 http://172.16.1.10/xxxs.php?c=
