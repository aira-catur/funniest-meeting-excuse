"""Entry for The Funniest Excuse for Skipping a Meeting (make.fun).

Judge brief from RULES.txt (published in full):
- One funny single-line excuse, at most 200 characters, for skipping a
  pointless work meeting or Zoom call. Judge compares two at a time and
  picks the one that would draw the biggest knowing laugh from office workers.
- Criteria, most important first:
  1. Is a funny one-line excuse for skipping a pointless work meeting or
     Zoom call, and loses to any excuse that is on the subject.
  2. Lands a sharp, surprising turn that earns the laugh, not just a mild smile.
  3. Feels true to office life, so the laugh arrives with a nod of recognition.
  4. Says it in one tight line, with no wasted words or throat-clearing.
  5. Finds a fresh angle rather than a stock excuse about bad wifi, a cat
     or a dentist.
- Gate from RULES.txt: /output/entry.txt is UTF-8 text of 1 to 200
  characters, not only whitespace. Entry filename: entry.txt
"""
import os

MIN_CHARS = 1
MAX_CHARS = 200

# Each candidate scored per judge criteria (1-5 above), 0-10 each.
CANDIDATES = [
    {
        "text": "Can't make it — I'm still in the pre-meeting about whether we needed this meeting.",
        "scores": {"on_subject": 9, "surprise": 6, "office_truth": 9, "tightness": 8, "freshness": 6},
    },
    {
        "text": "Sorry, my calendar double-booked me with the work this meeting was going to assign me anyway.",
        "scores": {"on_subject": 9, "surprise": 7, "office_truth": 9, "tightness": 6, "freshness": 7},
    },
    {
        "text": "I can't attend — I already read the agenda and emotionally attended in advance.",
        "scores": {"on_subject": 8, "surprise": 6, "office_truth": 7, "tightness": 8, "freshness": 7},
    },
    {
        "text": "Skipping today — my out-of-office is on, but only for meetings that could've been an email.",
        "scores": {"on_subject": 9, "surprise": 6, "office_truth": 9, "tightness": 6, "freshness": 5},
    },
    {
        "text": "Can't join — I'm on mute in real life until someone sends an agenda with a decision in it.",
        "scores": {"on_subject": 8, "surprise": 7, "office_truth": 8, "tightness": 7, "freshness": 7},
    },
    {
        "text": "Sorry, I tested positive for having seen this exact meeting three times this week.",
        "scores": {"on_subject": 9, "surprise": 8, "office_truth": 9, "tightness": 8, "freshness": 7},
    },
    {
        "text": "I won't be there — my focus block and this meeting got into a fight and the focus block won.",
        "scores": {"on_subject": 8, "surprise": 6, "office_truth": 8, "tightness": 7, "freshness": 7},
    },
    {
        "text": "Declining — last time I joined a meeting with no agenda I aged out of my own action items.",
        "scores": {"on_subject": 9, "surprise": 7, "office_truth": 8, "tightness": 7, "freshness": 8},
    },
    {
        "text": "Can't join — my manager told me to prioritise, so I'm prioritising the deadline this meeting keeps talking about.",
        "scores": {"on_subject": 10, "surprise": 7, "office_truth": 10, "tightness": 7, "freshness": 8},
    },
    {
        "text": "Sorry, HR flagged my 'this could have been an email' face as a workplace hazard, so I'm quarantined from meetings.",
        "scores": {"on_subject": 10, "surprise": 8, "office_truth": 9, "tightness": 6, "freshness": 9},
    },
    {
        "text": "Can't attend — I opened the invite, saw 'quick sync, 60 minutes' and my soul filed for annual leave.",
        "scores": {"on_subject": 10, "surprise": 8, "office_truth": 10, "tightness": 7, "freshness": 8},
    },
    {
        "text": "Sorry, I'm on parental leave — the action item from our last meeting just gave birth to three more meetings.",
        "scores": {"on_subject": 10, "surprise": 10, "office_truth": 10, "tightness": 9, "freshness": 10},
    },
    {
        "text": "Declining with regret — I reached my legal limit of nodding at slides I read faster than the presenter.",
        "scores": {"on_subject": 9, "surprise": 8, "office_truth": 10, "tightness": 7, "freshness": 9},
    },
]

WEIGHTS = {"on_subject": 5, "surprise": 4, "office_truth": 3, "tightness": 2, "freshness": 2}


def total(candidate):
    return sum(candidate["scores"][k] * WEIGHTS[k] for k in WEIGHTS)


def main():
    winner = max(CANDIDATES, key=total)["text"]
    assert MIN_CHARS <= len(winner) <= MAX_CHARS, f"char count {len(winner)} outside gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(winner)


if __name__ == "__main__":
    main()
