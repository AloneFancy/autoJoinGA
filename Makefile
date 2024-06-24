all: mann skinsmonkey

timezone:
	python syncTZ.py
mann:	
	python mann.py
skinsmonkey:
	python skinsmonkey.py