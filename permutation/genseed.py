from secrets import randbits

seed = randbits(128)
with open("./seed", "w") as f:
    f.write(f"{seed}")
