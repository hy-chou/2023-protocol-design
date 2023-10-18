from random import sample, seed

from perm import perm

CHUNK_SIZE = 8

with open("./seed.txt") as f:
    seed(f.readline())

with open("./alice.txt") as f:
    buffer = f.readline()

alice = ""
for char in buffer:
    for byte in char.encode("utf-8"):
        alice += "".join(f"{byte:08b}")

chunks = [
    alice[i * CHUNK_SIZE : (i + 1) * CHUNK_SIZE]
    for i in range(len(alice) // CHUNK_SIZE)
]

charlie = ""
for chunk in chunks:
    oneline = sample(range(CHUNK_SIZE), k=CHUNK_SIZE)
    charlie += "".join(perm(chunk, oneline))

buffer = int(charlie, 2).to_bytes(len(charlie) // 8, byteorder="big")
with open("./charlie.txt", "bw") as f:
    f.write(buffer)