# Instructions: independent check of drafted conditions

You are checking content drafted by another agent for a mock triage engine (a
demonstration, never for clinical use). Do not edit anything. Report problems.

Read the batch's condition cards, observations, entry-symptom files and advice,
and the saved source pages they cite. Use your own clinical knowledge as well.

Look for, most serious first:

1. A red flag or urgent sign for an entry symptom that has no rule.
2. A rule, default or condition with the wrong urgency or level of care.
3. A dangerous condition missing from an entry symptom it commonly presents
   with, or with a danger class that is too low.
4. A condition that cannot be told apart from its look-alikes: too few
   observations, or none that point to it more than to the others.
5. Bands that are clearly wrong: a common condition marked rare, or a typical
   symptom marked weak.
6. Question or advice wording that changes the meaning of the source, or is
   hard to understand.
7. A SNOMED CT code whose concept does not mean the same as the item.
8. Duplicated observations that should be one, or should be parent and child.

For each problem give the file and id, what is wrong, the evidence (a source
quote or clinical reasoning), and a concrete fix. Separate definite problems
from judgement calls. Keep the report under 800 words.
