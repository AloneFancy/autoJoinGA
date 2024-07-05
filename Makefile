all: mann skinsmonkey
install:
	pip3 install -r requirements.txt
timezone:
	python syncTZ.py
mann:	
	python mann.py
skinsmonkey:
	python skinsmonkey.py

clean:
	rm logs/*

web:
	flask run