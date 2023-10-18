all: charlie.txt bob.txt
	diff alice.txt bob.txt && echo "OK" || echo "KO"

charlie.txt:
	python3 enc.py
bob.txt:
	python3 dec.py

hello:
	echo "Hello, World"

clean:
	rm bob.txt charlie.txt
