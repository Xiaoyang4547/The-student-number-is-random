from easygui import *
list_1 = ['小明','张三','小红']
import random

msgbox('您当前使用的是测试版本，所以有不稳定的地方，请见谅', "广告")
pw = passwordbox(msg='请输入密码', title=' ', default='', image=None, root=None)
if pw=='qmx5883950':
    while 1:
        a = buttonbox(msg='选择随机模式', title='选择随机模式', choices=('随机一人', '随机多人','关于','退出',), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)
        if a=='随机一人':
            jg = random.randint(0,3)
            msgbox(list_1[jg], '随机结果')
        if a=='随机多人':
            list_2 = []
            b = enterbox(msg='输入随机人数', title='输入随机人数', default='', strip=True, image=None, root=None)
            b = int(b)
            if b < 50:
                for i in range(b):
                    jg = random.randint(0,3)
                    list_2.append(list_1[jg])
                    msgbox(list_2, '随机结果')
            if b==50:
                msgbox(list_1, '随机结果')
            if b > 50:
                msgbox('没有这么多人！', '随机结果')
        if a=='关于':
            msgbox('''学号随机 版本1.0.0 Bata-1  Thonny4.1.4,Python3.1.3,Easygui0.98.2,Pyinstaller6.12.0,anaconda3编写
更新内容：
1.添加限位。
已知问题：
1.随机多人时会发生重复现象。''', '关于')
        if a=='退出':
            break
else:
    msgbox('密码错误，无法验证', ok_button="退出")