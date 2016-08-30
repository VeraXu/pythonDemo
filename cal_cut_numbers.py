# -*- coding: utf-8 -*-
__author__ = 'xuziyue'
#引入sys模块
import sys

class CutNumber: 
    
    #定义获取剪法的, 规律 0，1，2，4，7，12，20
    def getCutNum(self,n):
        if n<=1:
            return 0;
        elif  n==2:
            return 1;
        else:
            return self.getCutNum(n-1)+self.getCutNum(n-2)+1;
    #验证参数有效性
    def check(self,n):
        length=str(n)
        #只有输入正整数才执行方法,isdigit方法判断输入的是数字
        if  length.isdigit():
            length=int(length)
            if length<=0:
                print("绳子长度设置错误,请输入大于0的正整数,您输入的是:%s" % length)
                return -1 
            else:
                temp=self.getCutNum(length);
                print("%s " % temp)
                return temp
        else:
            print("绳子长度设置错误,请输入正整数,您输入的是:%s" % n)
            return -1
#main函数
if __name__ == '__main__':
    #判断用户是否输入参数
    if len(sys.argv) < 2 :
        print ("执行%s 请设置绳子长度" % sys.argv[0])
        sys.exit()
    else:
        cutNumber=CutNumber();
        cutNumber.check(sys.argv[1])
