# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:08:33 2022

@author: Seba
"""

def output_file_name (FCTRY_CNTRY_CODE,PUBLICATION_ID,PUBLICATION_DATE,f_name):
    fl_n_1 = FCTRY_CNTRY_CODE + '_' + str(PUBLICATION_ID) + '_GSRS_'
    global fl_n_txt, fl_n_csv
    fl_n_txt =  fl_n_1 + f_name + PUBLICATION_DATE + '.txt'
    fl_n_csv =  fl_n_1 + f_name + PUBLICATION_DATE + '.csv'
    return fl_n_txt, fl_n_csv