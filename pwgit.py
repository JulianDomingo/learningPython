#! python3
# Manages all passwords for user.

import sys, pyperclip

passwords = {'facebook':'*****',
			 'utemail':'*****',
			 'personalemail':'*****',
			 'overwatch':'*****',
			 'league':'*****',
			 'slack':'*****',
			 'git':'*****'}

account = sys.argv[1]
account = account.lower()

if account in passwords:
	pyperclip.copy(passwords[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('No password for ' + account + '.')