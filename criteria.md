# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1.

The classifier will achieve at least **0.60 overall accuracy** on the held-out
test set in each of three evaluation runs using seeds `42`, `7`, and `2024`.

**Why this target:** With four labels, a roughly even random guess would be
about 0.25 accuracy. A 0.60 target means the classifier is getting a useful
majority of posts right while leaving room for the small, hand-labelled
dataset and the difficult boundary between movie analysis and plot
clarification.

---

## 2.

Every label will achieve at least **0.45 F1** on the held-out test set in each
of three evaluation runs using seeds `42`, `7`, and `2024`.


**Why this target:** The four labels describe different purposes, so overall
accuracy could hide a label that the model almost never recognizes. I am using
a lower target than the overall accuracy target because `plot_clarification`
and `industry_news` may be thinner and their test-set F1 scores will be more
volatile.

---

## 3.

No single label will account for more than **40% of the final dataset**.

**Why this target:** The assignment's hard ceiling is 70%, but a four-label
classifier should be more balanced than merely passing that ceiling. Keeping
the largest label at or below 40% should reduce the chance that the model can
look accurate by mostly guessing the most common kind of `r/movies` post.

---

## 4.

The spread between the highest and lowest **macro F1 scores across the three
evaluation runs using seeds `42`, `7`, and `2024` will be no more than 0.10**.

**Why this target:** The test set will be small, especially for the thinner
`plot_clarification` and `industry_news` labels. A spread of 0.10 or less
would mean the overall measure is reasonably stable instead of depending on
which few examples happened to land in each test split.

---

## 5.

In each of the three evaluation runs using seeds `42`, `7`, and `2024`, the
most-confident third of predictions will have at least **0.65 accuracy** and
will be at least **0.10 more accurate than the least-confident third**.

**Why this target:** If the model is going to help sort a busy movie forum,
its strongest predictions should be safer to trust than its least-certain
ones. The 0.10 gap requires confidence to carry useful information without
expecting perfect calibration from a small dataset.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
