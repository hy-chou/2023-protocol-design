from random import choices, getstate, randint, seed, setstate
from secrets import randbits

CHUNK_SIZE = 8 * 3
NUM_CHANNEL = 3

with open("./seed") as f:
    seed(f.readline())  # seed for channel picking
state_i_picking = getstate()

seed(randbits(128))  # seed for noise generation
state_noise = getstate()


with open("./alice", "br") as f:
    buffer = f.read()

alice = ""
for byte in buffer:
    alice += "".join(f"{byte:08b}")

chunks = [
    alice[i * CHUNK_SIZE : (i + 1) * CHUNK_SIZE]
    for i in range(len(alice) // CHUNK_SIZE)
]

channels = ["" for _ in range(NUM_CHANNEL)]
for chunk in chunks:
    setstate(state_i_picking)
    i_picked = randint(0, NUM_CHANNEL - 1)
    state_i_picking = getstate()
    for i in range(NUM_CHANNEL):
        if i == i_picked:
            channels[i] += chunk
        else:
            noise = "".join(choices(["0", "1"], k=CHUNK_SIZE))
            channels[i] += noise

for i in range(NUM_CHANNEL):
    buffer = int(channels[i], 2).to_bytes(len(channels[i]) // 8, byteorder="big")
    with open(f"./channel_{i}", "bw") as f:
        f.write(buffer)
