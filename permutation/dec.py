from random import sample, seed

CHUNK_SIZE = 8

with open("./seed") as f:
    seed(f.readline())

with open("./charlie", "br") as f:
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
    tmp = [-1 for _ in range(len(oneline))]
    for i, p in enumerate(oneline):
        tmp[p] = chunk[i]  # reverse permutation
    bob += "".join(tmp)

line = int(bob, 2).to_bytes(len(bob) // 8, byteorder="big")
with open("./bob", "bw") as f:
    f.write(line)
