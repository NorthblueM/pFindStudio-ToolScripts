# -*- coding: UTF-8 -*-

# @Date    : Sep 12, 2020
# @Author  : Peng-Zhi Mao, maopengzhi@foxmail.com
"""fasta文件的一些操作"""

import pandas as pd

def read_fasta_file(path):
    """读取fasta文件

    Args:
        path: fasta文件路径
    Returns:
        字典{蛋白质名称：蛋白质序列}
    """

    map_protein_seq = {}

    with open(path, 'r') as fin:
        i_total = 0
        prtn_name = ''
        prtn_seq = ''
        prtn_seq_ls = []
        for line in fin:
            if line[0] == '>':
                i_total += 1
                if i_total != 1:
                    prtn_seq = ''.join(prtn_seq_ls)
                    map_protein_seq[prtn_name] = prtn_seq
                    prtn_name = ''
                    prtn_seq = ''
                    prtn_seq_ls = []
                prtn_name = line.strip()[1:]
            else:
                prtn_seq_ls.append(line.strip())

        prtn_seq = ''.join(prtn_seq_ls)
        map_protein_seq[prtn_name] = prtn_seq
    return map_protein_seq


def write_fasta_file(path, map_prtn_seq):
    """写出fasta文件

    Args:
        path: fasta文件路径
        map_prtn_seq: 字典{蛋白质名称：蛋白质序列}
    """

    prtn_line_len = 60 # 每行蛋白质序列最长

    with open(path, 'w') as f:
        for k, v in map_prtn_seq.items():
            f.write('>' + k + '\n')
            for i in range(int(len(v)/prtn_line_len)):
                f.write(v[i*prtn_line_len:(i+1)*prtn_line_len] + '\n')
            if len(v)%prtn_line_len != 0:
                i = int(len(v)/prtn_line_len)
                f.write(v[i*prtn_line_len:] + '\n')


def extract_ac(ac2seq, ac_ls, cmp_shortac=False):
    """根据蛋白名称提取蛋白
        cmp_shortac: 通过短文件名比较
    """
    if cmp_shortac:
        ac_ls = [x.split()[0] for x in ac_ls]

    ac_set = set(ac_ls)
    ac2seq_new = {}
    for ac, seq in ac2seq.items():
        ac_str = ac
        if cmp_shortac:
            ac_str = ac_str.split()[0]
        if ac_str in ac_set:
            ac2seq_new[ac] = seq
    print('===original protein: %d\textract protein: %d'%(len(ac2seq),len(ac2seq_new)))
    return ac2seq_new


def extract_ac_pfind_spectra(fpath):
    """从pFind的spectra鉴定文件提取蛋白质名称
        去掉反库
    """

    df = pd.read_csv(fpath, sep='\t')
    ls_ac_str = list(df['Proteins'])
    ls_ac = []
    for ac_str in ls_ac_str:
        ls_ac.extend(ac_str.strip('/').split('/'))
    
    ls_ac_target = []
    for ac in ls_ac:
        if not ac.startswith('REV_'):
            ls_ac_target.append(ac)
    
    print('===total protein: %d\t target: %d'%(len(set(ls_ac)), len(set(ls_ac_target))))

    return set(ls_ac_target)

def build_fasta_pfind_spectra(fpath_fasta, fpath_pfind, fpath_out):
    """从pFind的spectra鉴定文件提取蛋白质名称
        建新库
    """

    ac2seq = read_fasta_file(fpath_fasta)
    set_ac = extract_ac_pfind_spectra(fpath_pfind)
    ac2seq = extract_ac(ac2seq, list(set_ac), cmp_shortac=True)

    write_fasta_file(fpath_out, ac2seq)

def _main():
    pass

if __name__ == "__main__":
    _main()
