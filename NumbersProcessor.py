#! /usr/bin/python

import phonenumbers
import subprocess

# import file
PhoneNumbersFile = open('Phone Numbers', 'r')
TextMessageFile = open('Text Message', 'r')

#variables
num = 0
FormattedList = []
TextMessage = " \"" + TextMessageFile.read().rstrip('\n') +"\""

#extract numbers
for line in PhoneNumbersFile:
    x = phonenumbers.parse(line, "US")
    FormattedList.append(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)[1:])
    num = num + 1

#send messages
for var in FormattedList:
    mystr = "osascript sendMessage.applescript " + str(var) + TextMessage
    print mystr
    subprocess.call(mystr, shell=True)

#print how many numbers were processed
print str(num) + " numbers processed..."

# osascript -e 'tell application "Messages" to send "text_message" to "number"'
