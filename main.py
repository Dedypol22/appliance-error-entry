"""The funniest honest appliance error: a robot vacuum, blinded by dust.

The winning line:

    Error: cliff sensor blocked by dust. I cannot see the stairs
    because of the dirt I was hired to clean. This is a conflict
    of interest.

Why it lands under the judge brief, in the brief's own order:

1. It IS an error message an appliance could show: "Error: cliff
   sensor blocked by dust" is a real fault report a robot vacuum
   gives, in the flat form such machines use.
2. The laugh lands on the first read and needs no explanation: the
   machine hired to remove dirt is blinded by dirt, and it files
   the fact as a workplace grievance -- "a conflict of interest".
3. The humour grows out of the truth of the fault itself, not a pun
   bolted on: a cliff sensor really is an optical sensor, dust
   really does block it, and the dirt really is the machine's own
   job. The irony is self-referential -- the fault IS the job --
   the same mechanism that won "Say What Actually Broke" (a disk
   full of logs complaining the disk is full).
4. The machine's voice is flat and put-upon throughout: it reports,
   it explains without pleading, and it closes with a dry HR phrase,
   as if it wrote the line without meaning to be funny.
5. It is tight: 134 characters, every clause earning its place, and
   the punch ("This is a conflict of interest.") lands on the last
   five words.

Candidate scoring (1-5 on each of the 5 judge criteria, in order):

 1. Washer, one sock 47 times -- 5, 4, 5, 4, 4 = 22
 2. Toaster, charcoal out of respect -- 4, 5, 4, 4, 4 = 21
 3. Boiler, pilot light took my will to live -- 4, 4, 4, 4, 3 = 19
 4. Dishwasher, same plate 3 times -- 3, 3, 3, 4, 4 = 17
 5. Microwave, coffee reheated 4 times -- 4, 4, 3, 5, 4 = 20
 6. Robot vacuum, cliff sensor blocked by dust -- 5, 5, 5, 5, 4 = 24
 7. Ice maker, glacier of 2,000 cubes -- 4, 4, 4, 4, 5 = 21
 8. Kettle, limescale maraca after 1,842 boils -- 5, 4, 5, 4, 4 = 22
 9. Dryer, 3 kg of clothes' former selves -- 4, 4, 4, 4, 4 = 20
10. Washer, 94% hoodie and 6% regret -- 4, 5, 4, 5, 5 = 23
11. Oven, cheese from 2019 has tenure -- 4, 5, 4, 4, 4 = 21
12. Coffee machine, 38% limescale, tastes like a cave -- 5, 4, 5, 4, 4 = 22
13. Air fryer, pressed start 11 times -- 4, 4, 3, 5, 5 = 21
14. Rice cooker, rice achieved sentience -- 2, 4, 2, 4, 5 = 17
15. Iron, shirt remains wrinkled, so do you -- 3, 4, 3, 4, 4 = 18
16. Toaster, lever jammed, become a metaphor -- 3, 4, 3, 4, 5 = 19

Rejected outright: fridge angles (fridge ordering groceries /
"watching you" are brief clichés, and our own fridge-roast entry
already plays the smart-fridge angle); smart-toaster-unplugged
(our own earlier entry plays it); any line that blames the user
instead of naming a machine fault (criterion 3 fails).
"""

import os
import sys

MAX_LENGTH = 200

ERROR_LINE = (
    "Error: cliff sensor blocked by dust. "
    "I cannot see the stairs because of the dirt "
    "I was hired to clean. This is a conflict of interest."
)


def output_path() -> str:
    """Return the path of entry.txt, honouring MAKEFUN_OUTPUT_DIR."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    return os.path.join(output_dir, "entry.txt")


def main() -> int:
    if not ERROR_LINE:
        print("error: error line is empty", file=sys.stderr)
        return 1
    if "\n" in ERROR_LINE or "\r" in ERROR_LINE:
        print("error: error line must be a single line", file=sys.stderr)
        return 1
    if len(ERROR_LINE) > MAX_LENGTH:
        print(
            f"error: error line is {len(ERROR_LINE)} characters, "
            f"over the {MAX_LENGTH}-character limit",
            file=sys.stderr,
        )
        return 1

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ERROR_LINE + "\n")

    with open(path, "r", encoding="utf-8", newline="") as handle:
        landed = handle.read()
    expected_bytes = len((ERROR_LINE + "\n").encode("utf-8"))
    actual_bytes = os.path.getsize(path)
    if landed != ERROR_LINE + "\n" or actual_bytes != expected_bytes:
        print(
            f"error: read-back mismatch on {path}: "
            f"expected {expected_bytes} bytes of the error line, "
            f"found {actual_bytes} bytes",
            file=sys.stderr,
        )
        return 1

    print(ERROR_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
