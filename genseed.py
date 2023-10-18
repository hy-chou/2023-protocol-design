from secrets import randbits

seed = randbits(128)
with open("./seed.txt", "w") as f:
    f.write(f"{seed}")
