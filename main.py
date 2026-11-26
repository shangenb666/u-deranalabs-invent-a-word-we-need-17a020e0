"""Write the entry word for make.fun's "Invent a Word We Need" bounty.

The entry is one invented English word that does not exist, plus its
definition in one clear line, at most 140 characters in total. It
names a feeling every programmer knows but no dictionary covers yet:
the dread of code that works too easily. The "(n.)" marks it as a
noun, the way a dictionary entry would. This program writes that
line to entry.txt in the output directory, deterministically: the
same line, byte for byte, on every run. Standard library only;
no network.
"""

import os

LINE = "Flurf (n.): the sudden panic when your code works on the first try and you no longer trust any of it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
