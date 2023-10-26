from random import randint, seed

CHUNK_SIZE = 8 * 3
NUM_CHANNEL = 3

with open("./seed") as f:
    seed(f.readline())


channels = ["" for _ in range(NUM_CHANNEL)]
for i in range(NUM_CHANNEL):
    with open(f"./channel_{i}", "br") as f:
        buffer = f.read()
    for byte in buffer:
        channels[i] += "".join(f"{byte:08b}")

chunks = []
for i in range(len(channels[0]) // CHUNK_SIZE):
    i_picked = randint(0, NUM_CHANNEL - 1)
    chunk = channels[i_picked][i * CHUNK_SIZE : (i + 1) * CHUNK_SIZE]
    chunks.append(chunk)

bob = ""
for chunk in chunks:
    bob += "".join(chunk)

line = int(bob, 2).to_bytes(len(bob) // 8, byteorder="big")
with open("./bob", "bw") as f:
    f.write(line)
