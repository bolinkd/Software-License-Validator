from Crypto.PublicKey import RSA
import argparse
import datetime
import os

parser = argparse.ArgumentParser(description='Software License Validator')
parser.add_argument('location', metavar='S', type=str, nargs='?',
                   help='Key Location')
parser.add_argument('--generate', required=False, default=False, type=bool,
                   help='Create A License Key')
parser.add_argument('--day', required=False,
				   help='Day Key Expires')
args = parser.parse_args()

location = os.getcwd()
date = None

if args.location != None:
	location = args.location
if args.day == None:
	date = datetime.datetime.now() + datetime.timedelta(days=31)
	date = date.strftime("%d/%m/%Y")
else:
	date = datetime.datetime
	date = date.strptime(args.day, "%d/%m/%Y")
	date = date.strftime("%d/%m/%Y")

key = RSA.generate(2048)

if args.generate == False:

	f = open(location + "\Software License.txt", "r")

	read = f.read()
	temp = key.decrypt(read)
	print "VALUE: " + temp


else:

	message = str(date)

	e_message = key.encrypt(message,32)

	f = open(location + "\Software License.txt", "w")

	f.write(e_message)

	f.close()