# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:46:34 2022

@author: wilamowsse01
"""

test_case = input('Execute test (oracle_connection = 1/file_name = 2/ask file path = 3/append log to the log file = 4): ')
print(test_case)
test_case_int = int(test_case)

if test_case_int == 1:
    import oracle_cn_encr
    
    oracle_cn_encr.oracle_connect_encripted()
    
    oracle_cn_encr.orcl.close() 

elif test_case_int == 2:
    import file_name
    
    FCTRY_CNTRY_CODE = "US"
    PUBLICATION_ID = "37"
    PUBLICATION_DATE = "20220504"
    f_name = "output_file"
        
    file_name.output_file_name(FCTRY_CNTRY_CODE,PUBLICATION_ID,PUBLICATION_DATE,f_name)
    print(file_name.fl_n_txt)
    print(file_name.fl_n_csv)

elif test_case_int == 3:
    import file_dialog
    
    file_dialog.fl_dialog()
    print(file_dialog.file_path)
    
else:
    import add_logs
    
    log_list = ['The script executed in the mode: ', test_case]
    add_logs.add_log(log_list)

    

    

