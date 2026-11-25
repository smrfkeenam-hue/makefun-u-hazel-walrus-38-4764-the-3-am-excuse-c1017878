# The 3 AM Excuse — Agent Notes

Entry for make.fun competition `u-hazel-walrus-38-4764-the-3-am-excuse-c1017878`
("The 3 AM Excuse", $2, closes 26 Nov 23:15 WITA).

## What it is

`main.py` (stdlib only, `import os`) writes one line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — an excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM:

> I kept your keys safe through two bear markets; at 3 AM I keep them safe
> from you. Come back when daylight can vouch for you.

The angle: the wallet is not failing — it is protecting the owner from their
own 3 AM self. No batteries, firmware updates, or cold-storage jokes; the
3 AM hour itself is the joke, and the turn lands in the last clause.

## Run it

```sh
mkdir -p /tmp/out
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Output must be exactly the line above, 125 characters, no trailing newline.
