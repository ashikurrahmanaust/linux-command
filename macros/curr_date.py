# python tool for returning a formated date string

import os, sys

def process(ar):
    ar = ar.strip('\n')
    ar = ar.strip('\t')
    ar = ar.strip(' ')
    return ar

def get_date(formatter = '.'):
    cmd='date +%d' + formatter + '%m' + formatter + '%Y > tmp'
    x = os.system(cmd)
    assert(x == 0)
    f_temp = open('tmp', 'r')
    buffer = f_temp.read()
    f_temp.close()
    buffer = process(buffer)
    print(buffer, end = '', flush = True)

if (__name__ == '__main__'):
    get_date()