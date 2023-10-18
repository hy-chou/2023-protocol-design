from random import sample, seed

CHUNK_SIZE = 8

with open("./seed") as f:
    seed(f.readline())

with open("./alice") as f:
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
    charlie += "".join([chunk[i] for i in oneline])

buffer = int(charlie, 2).to_bytes(len(charlie) // 8, byteorder="big")
with open("./charlie", "bw") as f:
    f.write(buffer)
