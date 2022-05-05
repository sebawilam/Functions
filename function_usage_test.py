# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:46:34 2022

@author: wilamowsse01
"""

test_case = input('Execute test (oracle_connection = 1/file_name = 2,ask file path = 3:)')

if test_case == 1:
    import oracle_cn_encr
    
    oracle_cn_encr.oracle_connect_encripted()
    
    oracle_cn_encr.orcl.close() 
elif test_case == 2:
    FCTRY_CNTRY_CODE = "US"
    PUBLICATION_ID = "37"
    PUBLICATION_DATE = "20220504"
    f_name = "output_file"
    
    def output_file_name (FCTRY_CNTRY_CODE,PUBLICATION_ID,PUBLICATION_DATE,f_name):
        fl_n_1 = FCTRY_CNTRY_CODE + '_' + str(PUBLICATION_ID) + '_GSRS_'
        global fl_n_txt, fl_n_csv
        fl_n_txt =  fl_n_1 + f_name + PUBLICATION_DATE + '.txt'
        fl_n_csv =  fl_n_1 + f_name + PUBLICATION_DATE + '.csv'
        return fl_n_txt, fl_n_csv
    
    
    output_file_name(FCTRY_CNTRY_CODE,PUBLICATION_ID,PUBLICATION_DATE,f_name)
    print(fl_n_txt)
    print(fl_n_csv)
else:
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print(file_path)