# -*- coding: utf-8 -*-
__author__ = 'xuziyue'
#引入Python自带的unittest模块
import unittest
import time

from cal_cut_numbers import CutNumber

#定义单元测试类
class TestCutNumber(unittest.TestCase):
    
    #测试参数有效性
    def test_init(self):
        cutNumber=CutNumber();
        self.assertEqual(cutNumber.check(0),-1)
        self.assertEqual(cutNumber.check("字符串"),-1)
        self.assertEqual(cutNumber.check("null"),-1)
        self.assertEqual(cutNumber.check(2),1)
        
        
    #程序执行时间
    def test_exeTime(self):
        cutNumber=CutNumber();
        start = time.clock()
        #执行30米
        cutNumber=cutNumber.check(40)
        end = time.clock()
        self.assertLess(end - start, 120)
        #print ("read: %f s" % (end - start))
        
#main方法
if __name__ == '__main__':
    unittest.main()          
    
    