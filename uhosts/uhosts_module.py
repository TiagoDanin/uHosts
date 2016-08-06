#!/usr/bin/python3
# -*- coding:utf-8 -*-

import re
import io

def regex(pattern, string):
	capt = re.match(pattern, string)
	if bool(capt):
		return capt.group(1)
	return False

def check(input):
	try:
		f = open(input, 'r')
	except FileNotFoundError:
		return False
	return True

def dir(self):
	if self.system_os == 'linux': #Linux <3
		self.dir_hosts = '/etc/hosts'
	elif self.system_os == 'linux2':
		self.dir_hosts = '/etc/hosts'
	elif self.system_os == 'linux3':
		self.dir_hosts = '/etc/hosts'
	elif self.system_os == 'darwin': #MacOS or OSx
		self.dir_hosts = '/etc/hosts'
	elif self.system_os == 'win32': #BadWindows
		self.dir_hosts = 'C:\Windows\System32\Drivers\etc\hosts'
	elif self.system_os == 'win64':
		self.dir_hosts = 'C:\Windows\System32\Drivers\etc\hosts'
	elif self.system_os == 'cygwin': #BadWindows
		self.dir_hosts = 'C:\Windows\System32\Drivers\etc\hosts'
	elif self.system_os == 'test':
		self.dir_hosts = 'hosts'
	else:
		return False
	return

def read_file(file):
	try:
		f = open(file, 'r')
	except:
		return False
	return f.read()

def read(self):
	f = open(self.dir_hosts, 'r')
	return f

def search(self, host):
	f = read(self)
	i = 0
	for h in f.readlines():
		i += 1
		if regex('^(' + host + ')', h):
			return h, i
	return False, False

def write(file, input, mode=None):
	_m = 'w'
	if mode != None:
		_m = mode

	f = open(file, _m)
	f.write(input)
	f.close
	return

def add(self, host):
	f = open(self.dir_hosts, 'a')
	f.write(host + '\n')
	f.close()
	return

def add_file(self, host_file):
	f = open(self.dir_hosts, 'a')
	f.write(host_file)
	f.close()
	return

def rem(self, host):
	f = read(self)
	text = ''
	found = 0
	for h in f.readlines():
		if regex('((' + host + ')[\n])', h):
			found += 1
		else:
			text = text + h

	write(self.dir_hosts, text)
	return found

def rem_file(self, host_file):
	found = 0
	file = io.StringIO(host_file)
	for host in file.readlines():
		found += rem(self, host.replace('\n', ''))
	return found
