import os
from glob import glob

files = glob('ava/*.png')
valid = open("valid.txt", "a")

if not os.path.exists('rp'):
    os.mkdir('rp')

for img in files:
    valid.write('rp/' + img.split('/')[-1] + '\n')
    os.system('cp ' + img + ' rp/')
    ann_file = img.split('/')[-1].split('.')[0] + '.txt'
    ann_file = open('rp/' + ann_file, "a")
    ann_file.write("0 0" + '\n')
    ann_file.write("001.00 002.000 003.000 004.00" + '\n')
    ann_file.write("005.00 006.00 007.00 008.00")
    ann_file.close()
