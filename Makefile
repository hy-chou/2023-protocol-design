all: charlie bob
	diff alice bob && echo "OK" || echo "KO"

charlie:
	python3 enc.py
bob:
	python3 dec.py

hello:
	echo "Hello, World"

clean:
	rm bob charlie
