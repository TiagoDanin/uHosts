from uhosts_module import *
import datetime
import requests
import io

def get_hosts(url):
	text = '\n\n #{}    URL:{}'.format(str(datetime.time), url)
	try:
		data = requests.get(url)
	except:
		return False
	if data.status_code != 200:
		return False

	file = io.StringIO(data.text)
	for host in file.readlines():
		if regex('^[\@]*[\|]*(([\w]*\.)([\w]*)([\.[\w]*))\^$', host):
			text = text + regex('^[\@]*[\|]*(([\w]*\.)([\w]*)([\.[\w]*))\^$', host) + '\n'
		elif regex('^127\.0\.0\.1[\s]*(([\w]*\.)([\w]*)([\.[\w]*))', host):
			text = text + regex('^127\.0\.0\.1[\s]*(([\w]*\.)([\w]*)([\.[\w]*))', host) + '\n'
	return text

filter = {} #List
filter['EasyList_Adult']        = 'https://easylist-downloads.adblockplus.org/easylist_noadult.txt'
filter['EasyList_Privacy']      = 'https://easylist-downloads.adblockplus.org/easyprivacy.txt'
filter['Fanboy_Cookies']        = 'https://www.fanboy.co.nz/fanboy-cookiemonster.txt'
filter['uBlockOrigin_Privacy']  = 'https://raw.githubusercontent.com/gorhill/uBlock/master/assets/ublock/privacy.txt'
filter['hpHosts_Exploits']      = 'http://hosts-file.net/exp.txt'
filter['hpHosts_Hijacking']     = 'http://hosts-file.net/hjk.txt'
filter['hpHosts_Malware']       = 'http://hosts-file.net/emd.txt'
filter['hpHosts_Phishing']      = 'http://hosts-file.net/psh.txt'
filter['hpHosts_Fraud']         = 'http://hosts-file.net/fsa.txt'
filter['hpHosts_Pharmacy']      = 'http://hosts-file.net/pha.txt'
filter['hpHosts_Piracy']        = 'http://hosts-file.net/wrz.txt'
filter['hpHosts_Spam']          = 'http://hosts-file.net/grm.txt'
