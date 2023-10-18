from random import sample, seed

from perm import inve

CHUNK_SIZE = 8

with open("./seed.txt") as f:
    seed(f.readline())

with open("./charlie.txt", "br") as f:
    buffer = f.read()

charlie = ""
for byte in buffer:
    charlie += "".join(f"{byte:08b}")

chunks = [
    charlie[i * CHUNK_SIZE : (i + 1) * CHUNK_SIZE]
    for i in range(len(charlie) // CHUNK_SIZE)
]

bob = ""
for chunk in chunks:
    oneline = sample(range(CHUNK_SIZE), k=CHUNK_SIZE)
    bob += "".join(inve(chunk, oneline))

line = int(bob, 2).to_bytes(len(bob) // 8, byteorder="big").decode("utf-8")
with open("./bob.txt", "w") as f:
    f.write(line)