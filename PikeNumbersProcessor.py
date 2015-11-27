import phonenumbers
import subprocess

# import file
PhoneNumbersFile = open('Phone Numbers', 'r')
TextMessageFile = open('Text Message', 'r')

num = 0
FormattedList = []
TextMessage = " " + TextMessageFile.read().rstrip('\n')

#perform logic
for line in PhoneNumbersFile:
    x = phonenumbers.parse(line, "US")
    FormattedList.append(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)[1:])
    num = num + 1

for var in FormattedList:
    mystr = "osascript sendMessage.applescript " + str(var) + TextMessage
    print mystr
    subprocess.call(mystr, shell=True)

print str(num) + " numbers processed..."

# osascript -e 'tell application "Messages" to send + TextMessage + to ""'
