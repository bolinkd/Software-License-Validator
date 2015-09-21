from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
import Crypto.Util.number
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

key = RSA.generate(2048)

if args.location != None:
	location = args.location
if args.day == None:
	date = datetime.datetime.now() + datetime.timedelta(days=31)
	date = date.strftime("%d/%m/%Y")
else:
	date = datetime.datetime
	date = date.strptime(args.day, "%d/%m/%Y")
	date = date.strftime("%d/%m/%Y")

if args.generate == False:

	f = open(location + "\Software License.txt", "r")

	read = f.read()
	temp = key.decrypt(read)

else:

	message = date
	input_File = open(location + "\Date.txt", "r+")
	input_File.write(message + '\n')

	hashMD5 = MD5.new()
	hashMD5.update(message)
	input_File.write(hashMD5.hexdigest())



	output_File = open(location + "\Software License.txt", "w")