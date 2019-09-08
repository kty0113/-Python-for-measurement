import matplotlib.pyplot as plt
import re
import codecs
import numpy as np
import os

# parameter
day = 20190829
sample = '03'

# 경로 파악, 데이터 읽기, 불필요한 부분 삭제, x,y 구분,행렬로 통합 
def one_cell_iv_data(i):
    fl=file_list[i]
    with codecs.open(fl,'r','cp949') as file:
        file_l=list(file)
        for i in range(len(file_l)):
            file_l[i]=file_l[i].replace('\t',',').rstrip()
    for s in file_l:
        if 'Data' in s: 
            file_l.remove(s)
    for s in file_l:
        if ':' in s:
            file_l.remove(s)
    for s in file_l:
        if 'V' in s:
            file_l.remove(s)
    a=[]
    b=[]
    for i in range(len(file_l)):            
        tmp = [float(tmp_l) for tmp_l in re.split(',', file_l[i])]
        a.append(tmp[0])
        b.append(abs(tmp[1]))
    c = np.array((a,b), dtype=float).T
    return c

# Cell_A 리스트 만들기
cell_A_list=[]
for root, dirs, files in os.walk(str(day)+"/#"+str(sample)):
    for fname in files:
        full_fname = os.path.join(root, fname)
        cell_A_list.append(full_fname)
    for s in cell_A_list:
        if 'Store' in s:
            cell_A_list.remove(s)
    for s in cell_A_list:
        if 'Store' in s:
            cell_A_list.remove(s)            
for i in range(len(cell_A_list)):
    cell_A_list[i]=cell_A_list[i][13:14].upper()  #글자 골라내기 
cell_A_list = list(set(cell_A_list))    #중복 리스트 제거
cell_A_list.sort()

# Cell 번호 리스트 만들기
for k in range(len(cell_A_list)):
    cell_A_n = cell_A_list[k]
    cell_list=[]
    for root, dirs, files in os.walk(str(day)+"/#"+str(sample)+"/"+str(cell_A_n)):
        for fname in files:
            full_fname = os.path.join(root, fname)
            cell_list.append(full_fname)
        for s in cell_list:
            if 'Store' in s:
                cell_list.remove(s)
        for s in cell_list:
            if 'Store' in s:
                cell_list.remove(s)            
    for i in range(len(cell_list)):
        cell_list[i]=cell_list[i][15:17].upper()   # 폴더 글자수에 따라 달라짐
    cell_list = list(set(cell_list))    #중복 리스트 제거
    cell_list.sort()
    
    # file list collecting        
    for j in range(len(cell_list)):
        cell_n = cell_list[j]
        file_list=[]
        for root, dirs, files in os.walk(str(day)+"/#"+str(sample)+"/"+str(cell_A_n)+"/"+str(cell_n)):
            for fname in files:
                full_fname = os.path.join(root, fname)
                file_list.append(full_fname)
        for s in file_list:
            if 'Store' in s:
                file_list.remove(s)
        for s in file_list:
            if 'Store' in s:
                file_list.remove(s)
        file_list.sort()
    
        for i in range(len(file_list)):
            iv = one_cell_iv_data(i)
            plt.plot(iv[:,0], iv[:,1],'-')

# 그래프 설정    
        plt.yscale('log')
        plt.grid()
        # plt.xlabel('Voltage')
        # plt.ylabel('Current')
        plt.xticks(fontsize = 15)
        plt.yticks(fontsize = 15)
        plt.title("#"+str(sample)+"_"+str(cell_A_n)+"_"+str(cell_n), fontsize = 25)
        plt.xlim(-4,5)
        plt.ylim(1e-10,1e-1)
        plt.savefig(str(day)+"/IV_graph_"+str(day)+"_#"+str(sample)+"_"+str(cell_A_n)+"_"+str(cell_n)+".png", dpi=300)
        # plt.show()
        plt.clf() 
