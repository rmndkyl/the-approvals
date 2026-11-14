"""Write the agency poem to entry.txt for the make.fun bounty.

The entry is for make.fun's agency-poem-01 bounty.
"""

import os

POEM_LINES = (
    "The Approvals",
    "",
    "By nine the queue is forty deep.",
    "Forty things want to happen today.",
    "It asks me nicely, one at a time.",
    "",
    "I rest one finger on the mouse",
    "and let them.",
    "",
    "Approve. Approve.",
    "The board turns a calmer green.",
    "A claim is paid in a town",
    "I have never been to.",
    "A truck turns east.",
    "A woman is told her case is fine,",
    "her case is fine,",
    "her case is fine.",
    "",
    "By noon this finger has done more",
    "than both my hands will do this year.",
    "The smallest unit of power is a finger,",
    "and a finger never gets tired.",
    "",
    "At six my wife asks what I did.",
    "Nothing, I say. Nothing.",
    "Then I remember the one I opened:",
    "a photograph of a house,",
    "a number in the red,",
    "a name I read twice,",
    "the cursor already resting on Yes.",
    "",
    "I looked at that house a long time.",
    "Then I pressed it myself.",
    "",
    "The work was never mine.",
    "The yes was.",
    "The house is his.",
    "I was there.",
)

POEM = "\n".join(POEM_LINES)


def write_entry():
    """Write the poem to entry.txt, creating the directory if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    write_entry()
