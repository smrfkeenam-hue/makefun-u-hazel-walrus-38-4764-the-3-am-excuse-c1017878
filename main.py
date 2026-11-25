import os

ENTRY = "I kept your keys safe through two bear markets; at 3 AM I keep them safe from you. Come back when daylight can vouch for you."

# The wallet's excuse: at 3 AM the danger is not the network, it is the owner.
# The line is written exactly once, with no trailing newline, so the gate
# reads it as one tight line of 125 characters.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(OUTPUT_DIR + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
