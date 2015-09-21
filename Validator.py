from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
import Crypto.Util.number
import cPickle
import argparse
import datetime
import os
import sys

parser = argparse.ArgumentParser(description='Software License Validator')
parser.add_argument('--key', required=False, default=False, dest='key', action='store_true',
                   help='Generate A Key')
parser.add_argument('--generate', default=False, dest='generate', action='store_true',
                   help='Create A License')
parser.add_argument('--test', required=False, default=False, dest='test', action='store_true',
                   help='Test a current License Key')
args = parser.parse_args()

location = os.getcwd()
date = None

if args.key == True:
	print "Creating Key..."
	rand = Random.new().read
	key = RSA.generate(1024,rand)
	with open("PrivateKey.PEM", 'wb') as s:
		s.write(key.exportKey('PEM'))

	with open("PublicKey.PEM", "wb") as s:
		s.write(key.publickey().exportKey('PEM'))


if args.generate == True:
	print "Generating . . ."

	date = datetime.datetime.now() + datetime.timedelta(days=31)
	date = date.strftime("%d/%m/%Y")

	key = RSA.importKey(open('PrivateKey.PEM').read())
	h = SHA256.new(date)
	signer = PKCS1_v1_5.new(key)
	signature = signer.sign(h)

	SoftwareLicense = open(location + "\Software License.txt", "w")
	SoftwareLicense.write(date)

	DigitalSignature = open(location + "\DigitalSignature.pkl", "wb")
	cPickle.dump(signature, DigitalSignature, protocol=cPickle.HIGHEST_PROTOCOL)

if args.test == True:
	print "Testing . . ."

	SoftwareLicense = open(location + "\Software License.txt", "r")
	DigitalSignature = open(location + "\DigitalSignature.pkl", "rb")

	SL = SoftwareLicense.read()
	dateNow = datetime.datetime.now()
	date = datetime.datetime.now()
	date = date.strptime(SL, "%d/%m/%Y")

	if date.year >= dateNow.year and  date.month >= dateNow.month and date.year >= dateNow.year:
		print "Key Is Valid!"
	else:
		sys.exit("Key is Invalid")
	

	signature = cPickle.load(DigitalSignature)

	key = RSA.importKey(open('PublicKey.PEM').read())
	h = SHA256.new(SL)
	verifier = PKCS1_v1_5.new(key)
	if verifier.verify(h, signature):
	   print "Accessing Private Network"
	   print "Download Complete!"
	else:
	    print "The Files Have Been Corrupted"

