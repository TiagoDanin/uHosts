#!/usr/bin/python3
# -*- coding:utf-8 -*-

import io

text = io.StringIO('''0
1
2''')

def list2():
	text2 = io.StringIO('''0
1
2''')
	for v in text2.readlines():
		print('[2]  ' + v.replace('\n', ''))
	return

for s in text.readlines():
	print('\n[1]  ' + s.replace('\n', ''))
	list2()
