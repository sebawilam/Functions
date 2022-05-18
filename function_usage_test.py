# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:46:34 2022

@author: wilamowsse01
"""

test_case = input('Execute test (oracle_connection = 1/file_name = 2/ask file path = 3/query_maker = 4/append log to the log file = 5): ')
# print(test_case)
test_case_int = int(test_case)

if test_case_int == 1:
    import oracle_cn_encr
    
    oracle_cn_encr.oracle_connect_encripted()
    
    oracle_cn_encr.orcl.close() 

elif test_case_int == 2:
    import file_name2
    
    N_part1 = input('Name part1: ')
    N_part2 = input('Name part2: ')
    N_part3 = input('Name part3: ')
    N_part4 = input('Name part4: ')
    sep = input('Separator: ')
        
    file_name2.output_file_name(N_part1,N_part2,N_part3,N_part4,sep)
    print(file_name2.fl_n_txt)
    print(file_name2.fl_n_csv)

elif test_case_int == 3:
    import file_dialog
    
    file_dialog.fl_dialog()
    print(file_dialog.file_path)
    
elif test_case_int == 4:
    import query_maker
    
    country = input('Country: ')
    table = input('Table name: ')
    a = input('If selected column type 1/ If all columns type 0: ')
    c = input('If where conditon type 1/ If no where condition type 0: ')
    if int(a) == 1:
        columns = input('Type column names, separated by comma: ')
    else:
        columns = ""
    if int(c) == 1:
        condition = input('Type where condition: ')
    else:
        condition = ""

    query_maker.qry(country,table,a,c,columns,condition)
    print(query_maker.q_table)
    
else:
    import add_logs2
    
    log_list = ['The script executed in the mode ', test_case,'2nd line description', test_case]
    add_logs2.add_log(log_list)

    

    

