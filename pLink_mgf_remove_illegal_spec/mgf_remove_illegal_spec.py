# -*- coding: UTF-8 -*-
# @Date     : 15th Jul, 2022
# @Author   : Pengzhi Mao, maopengzhi@ict.ac.cn

"""Remove the spectra without TITLE/PEPMASS/CHARGE information in the head in the mgf file
"""
import sys

def mgf_remove_miss_info(fpath):
    """
    """
    print("load mgf...", fpath)

    fpath_out = fpath[:-4]+'_legal.mgf'
    n_total = 0
    n_legal = 0
    spec_ls = []
    with open(fpath, 'r') as fi:
        with open(fpath_out, 'w') as fo:
            for line in fi:
                # print(line)
                if 'BEGIN IONS' in line:
                    n_total += 1
                    spec_ls = []
                    b_title = False
                    b_pepmass = False
                    b_charge = False
                if 'END IONS' in line:
                    spec_ls.append(line)
                    if b_title and b_pepmass and b_charge:
                        n_legal += 1
                        for l in spec_ls:
                            fo.write(l)
                if 'TITLE=' in line:
                    b_title = True
                if 'CHARGE=' in line:
                    b_charge = True
                if 'PEPMASS=' in line: # m/z
                    b_pepmass = True
                spec_ls.append(line)
    
    print('spec total:\t', n_total)
    print('spec legal:\t', n_legal)

def _main():
    fpath = sys.argv[1]
    mgf_remove_miss_info(fpath)

if __name__ in '__main__':
    _main()
