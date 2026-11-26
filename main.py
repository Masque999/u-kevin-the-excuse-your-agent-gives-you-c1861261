LINE = "The bug is fixed, and in my defence the compiler started it: the code did exactly what I wrote, which is the problem, and also the reason I am apologising in this font."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE
# The gate also rejects whitespace-only text: pin the no-padding rule
# (first run showed trim==self, now enforced so a stray space fails here).
assert LINE == LINE.strip(), "line has leading/trailing whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
