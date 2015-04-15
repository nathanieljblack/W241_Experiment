__author__ = 'tamao'

import sys
import imaplib
import getpass
import email
import datetime

from email.header import decode_header
import argparse

from difflib import SequenceMatcher

import csv

from datetime import datetime
from dateutil import parser as dtparser

#start = dtparser.parse("2015-04-11 00:00:00-07:00")

import base64

#My buggy SSH account needs this to write unicode output, you hopefully won't
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

prefix = '=?UTF-8?B?'
suffix = '?='

def reademail(emailaddress, emailpassword, csvinput, csvoutput, start_time, end_time):

    start_dt = dtparser.parse(start_time)
    end_dt = dtparser.parse(end_time)

    M = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        M.login(emailaddress, emailpassword)
    except imaplib.IMAP4.error:
        print "LOGIN FAILED!!! "
        return

    rv, mailboxes = M.list()
    if rv == 'OK':
        print "Mailboxes:"
        print mailboxes

    rv, data = M.select("INBOX")
    rv, data = M.search(None, "ALL")

    if rv != 'OK':
        print "No messages found!"
        return

    replies = []

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return

        msg = email.message_from_string(data[0][1])
        print 'Message %s: %s' % (num, msg['Subject'])
        print 'Raw Date:', msg['Date']

        dt = dtparser.parse(msg['Date'])

        if dt > start_dt and dt < end_dt:
            raw = msg['Subject']

            if "=?UTF-8?" in raw:
                # index = raw.find("==?=")
                # if index == -1:
                #     raw = raw
                # else:
                #     raw = raw[:index]

                re = unicode(decode_header(raw)[0][0], 'utf-8')
            else:
                re = unicode(raw, 'utf-8')

            print re

            replies.append(re)



    print replies

    M.close()
    M.logout()

    csvin = open(csvinput, 'r')
    csvout = open(csvoutput, 'w')

    rd = csv.reader(csvin)
    row = rd.next()
    row.append('outcome')
    print row
    all = [row]
    for row in rd:
        title = unicode(row[1], 'utf-8')
        print title
        replied = False
        for re in replies:
            if similar(title, re) > 0.7:
                replied = True
                break

        if replied:
            row.append('1')
        else:
            row.append('0')

        all.append(row)

    print all

    wr = csv.writer(csvout)
    wr.writerows(all)

    csvin.close()
    csvout.close()

def _parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--email_address', help='Email Address')
    parser.add_argument('--email_password', help='Email Password')

    parser.add_argument('--csv_input', help='CSV Input File')
    parser.add_argument('--csv_output', help='CSV Output File')

    parser.add_argument('--start_time', help='Start Date&Time')
    parser.add_argument('--end_time', help='End Date&Time')

    args = parser.parse_args()
    return args

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == '__main__':
    args = _parse_arguments()
    pilot = reademail(args.email_address, args.email_password, args.csv_input, args.csv_output, args.start_time, args.end_time)