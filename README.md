# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## Milestone 1: Finding the Community's Distinctions

**Community:** `r/movies`

**Source:** https://www.reddit.com/r/movies/

These are candidate distinctions observed while reading public top-level
posts. They are observations for designing the taxonomy, not final labels yet.
The main purpose of the post is the deciding factor when two patterns overlap.

1. **Evidence-based movie analysis or review:** The writer evaluates a movie
   and supports the evaluation with specific scenes, acting, dialogue,
   comparisons, or other details.
2. **Personal reaction or first impression:** The writer mainly shares a
   feeling, preference, or immediate response without building a sustained
   evidence-based argument.
3. **Plot or ending clarification:** The post's main purpose is to ask about or
   explain what happened, what the ending means, or how the story should be
   understood. It is about resolving the story, not primarily judging the
   movie's quality.
4. **Movie-industry news or decisions:** The post focuses on an external event
   or decision such as casting, a trailer, a release plan, or a studio choice,
   rather than interpreting a completed movie.

The hardest likely boundary is evidence-based analysis versus personal
reaction. A post belongs in the first group when specific movie details do
argumentative work; it belongs in the second when the details are absent or
merely decorative and the post is mainly a feeling or broad opinion.

---

## What This Does

TakeMeter will classify public top-level posts from the `r/movies` community.
The classifier will sort posts by their main purpose: evaluating a movie,
sharing an immediate personal response, clarifying a plot or ending, or
discussing movie-industry news and decisions. The goal is to distinguish how
people participate in movie discussions, not to decide whether a movie is good.

**Declared stretch feature:** I am using a fourth label because industry news
and decisions are a recurring kind of post that the other three do not cover.

---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `analysis_review`

**Definition:** A post whose main purpose is to evaluate or interpret a movie
and support that evaluation with specific scenes, acting, dialogue,
comparisons, or other details.

**Example 1:**
> [Gone Girl (2014): The Last Great Hollywood Thriller](https://www.reddit.com/r/movies/comments/1x65h59/gone_girl_2014_the_last_great_hollywood_thriller/)

**Example 2:**
> [The Ending of 'The Menu' [SPOILERS]](https://www.reddit.com/r/movies/comments/10qzsy2/the_ending_of_the_menu_spoilers/)

### `personal_reaction`

**Definition:** A post whose main purpose is sharing an immediate feeling,
preference, or first impression without a sustained evidence-based argument.

**Example 1:**
> [Unofficial Discussion: Atonement (2026)](https://www.reddit.com/r/movies/comments/1x67zgs/unofficial_discussion_atonement_2026/)

**Example 2:**
> [Rush Hour is Brilliant](https://www.reddit.com/r/movies/comments/qn3odu/rush_hour_is_brilliant/)

### `plot_clarification`

**Definition:** A post whose main purpose is asking about or explaining what
happened in a movie, what the ending means, or how the story should be
understood, rather than judging the movie's quality.

**Example 1:**
> [Mr. K [SPOILERS]](https://www.reddit.com/r/movies/comments/1x66vv5/mr_k_spoilers/)

**Example 2:**
> [What are some movies where the ending makes it that nothing really mattered?](https://www.reddit.com/r/movies/comments/1ubzw8z/what_are_some_movies_where_the_end_makes_it_that/)

### `industry_news`

**Definition:** A post whose main purpose is discussing an external movie-
industry event or decision, such as casting, a trailer, a release plan, or a
studio choice, rather than a completed movie's content.

**Example 1:**
> [Has a casting announcement ever made you lose interest in an otherwise promising movie?](https://www.reddit.com/r/movies/comments/1tizkn3/has_a_casting_announcement_ever_made_you_lose/)

**Example 2:**
> [Joe Manganiello reveals plot of Ben Affleck's scrapped Batman film](https://www.reddit.com/r/movies/comments/1x8qn8x/joe_manganiello_reveals_plot_of_ben_afflecks/)

### The hardest boundary

**Which two labels:** `analysis_review` vs. `plot_clarification`

**The decision rule I used every time:** If the post's main goal is to judge or
interpret the movie's quality, craft, or themes, label it `analysis_review`,
even if it discusses the ending. If its main goal is to resolve what happened
or what the ending means, label it `plot_clarification`, even if it includes an
opinion about whether the explanation is satisfying.



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

I collected 200 public posts from [r/movies](https://www.reddit.com/r/movies/).
The posts include reviews, reactions, questions about movie details, and
movie-industry discussions.

**How I labelled them:**

I labelled the first 22 posts cold, without AI assistance, and marked them
`cold` in the `note` column. I used AI assistance to propose labels for the
remaining 178 posts, then checked the assignments against the taxonomy and
accepted or corrected them. Each row keeps its Reddit source URL in `note`.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `analysis_review` | 60 | 30% |
| `personal_reaction` | 88 | 44% |
| `plot_clarification` | 24 | 12% |
| `industry_news` | 28 | 14% |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* A post about the theory that *The Wizard of Oz* was intentionally
> synchronized with Pink Floyd's *Dark Side of the Moon*.
>
> *Could have been:* `personal_reaction` or `analysis_review`
>
> *I chose, because:* `analysis_review`. The writer expresses personal
> excitement, but supports the interpretation with specific timing, lyric, and
> scene comparisons.

**2.**
> *The post:* A question about whether a restored or uncensored “Bluth cut” of
> *All Dogs Go to Heaven* might ever be released.
>
> *Could have been:* `industry_news` or `analysis_review`
>
> *I chose, because:* `industry_news`. Although the writer explains why the
> movie matters to them, the main question concerns an unavailable edit and
> the release decision surrounding it.

**3.**
> *The post:* An article-style post describing the plot of Ben Affleck's
> scrapped Batman movie and its planned villain and ending.
>
> *Could have been:* `industry_news` or `plot_clarification`
>
> *I chose, because:* `industry_news`. It discusses production information
> about an unreleased project rather than asking what happened in a completed
> movie.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

`distilbert-base-uncased`

**Settings:** <!-- epochs, learning rate, batch size, seed -->

The run used 3 epochs, learning rate `2e-5`, batch size `16`, maximum length
`128`, and seed `42`. It ran on the CPU with PyTorch `2.14.1+cpu`.

**Anything I changed from the defaults, and why:**

Nothing. I kept the supplied defaults so the first run would provide a clear
baseline for later comparisons.

**Split sizes:**

The stratified split produced 139 training posts, 31 validation posts, and 30
test posts. The test set contained 9 `analysis_review`, 13
`personal_reaction`, 4 `plot_clarification`, and 4 `industry_news` posts. The
two four-example test groups are small, so their metrics may vary substantially
in later seed comparisons.

**First-run results:**

The held-out test accuracy was `0.433` and macro F1 was `0.151`. Per-label F1
was `0.000` for `analysis_review`, `0.605` for `personal_reaction`, `0.000`
for `plot_clarification`, and `0.000` for `industry_news`. The most-confident
third had `0.600` accuracy, while the least-confident third had `0.100`.



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Help comparing possible distinctions in r/movies and
  testing whether the proposed labels were meaningfully separate.
- *What came back:* The discussion identified analysis/review, personal
  reaction, plot clarification, and industry news as useful patterns, with the
  main boundary between evaluating a movie and explaining its plot.
- *What I changed:* I changed the broad discussion category into
  `personal_reaction` and kept `industry_news` as a fourth label because it
  captured production and release posts the other labels missed.

**Moment 2**

- *What I asked for:* Help classify the collected posts consistently under the
  written taxonomy and check the CSV formatting.
- *What came back:* The AI proposed labels for the non-cold posts and helped
  identify quoting, URL, duplicate, and row-count problems in the CSV.
- *What I changed:* I reviewed the proposed labels against the taxonomy,
  accepted or corrected them, and fixed the CSV structure while preserving the
  source URLs.

**Pre-labelling disclosure:**

I labelled the first 22 posts cold without AI assistance. The remaining 178
posts were initially labelled with AI assistance, then read and checked against
the taxonomy before being accepted or corrected. The `note` column marks these
rows as `AI-assisted` and retains their source URL.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
