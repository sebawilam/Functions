# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:10:04 2022

@author: wilamowsse01
"""
from datetime import datetime

def add_log(log_list):
    now = datetime.now()
    print(now)
    file1 = open("log.log", "a")  # append mode
    file1.write('\n')
    file1.write(str(now))
    file1.write('\n')
    file1.writelines(log_list)
    file1.close()
    print("Log updated \n")
    for x in log_list:
        print(x)