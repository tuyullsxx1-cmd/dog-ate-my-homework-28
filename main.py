from pathlib import Path

# Three beats for the dog: the accusation, the motive, the verdict.
SEGMENTS = (
    "I ate your homework because it looked at me like a snack",
    "and, frankly, after three chapters on fractions,",
    "it had it coming.",
)
JOKE = " ".join(SEGMENTS)

# The entry must be a single line of plain text.
assert "\n" not in JOKE
# Brief cap for this bounty: at most 200 characters.
assert 1 <= len(JOKE) <= 200
# The dog's excuse has to name the homework it ate.
assert "homework" in JOKE
# Second pass: the snack line lands harder when the fractions chapter is named.
assert JOKE.startswith("I ate")

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(JOKE + "\n", encoding="utf-8")
