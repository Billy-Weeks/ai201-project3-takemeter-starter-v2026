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

*Update after labelling:* While labelling the full dataset, the boundary
between `analysis_review` and `plot_clarification` turned out to be harder,
because ending-focused posts often mix explaining the story with judging it.
The final taxonomy below names that pair as the hardest boundary and gives the
decision rule used.

---

## What This Does

TakeMeter will classify public top-level posts from the `r/movies` community.
The classifier will sort posts by their main purpose: evaluating a movie,
sharing an immediate personal response, clarifying a plot or ending, or
discussing movie-industry news and decisions. The goal is to distinguish how
people participate in movie discussions, not to decide whether a movie is good.

**Declared stretch feature:** I am using a fourth label because industry news
and decisions are a recurring kind of post that the other three do not cover.

**What the fourth label captures that the first three missed:** The first
three labels all describe how someone engages with a movie that already
exists: judging it (`analysis_review`), reacting to it (`personal_reaction`),
or working out its story (`plot_clarification`). A large share of `r/movies`
posts are about something outside the finished film instead: a new poster, a
casting or director change, a project put on hold, studio interference and
reshoots, or a funding or distribution decision. For example, "Taika
Waititi's 'Star Wars' film is now on hold" or "First Poster for
'Hurricanna'". There is no finished movie to evaluate, react to, or explain,
so without `industry_news` these posts would be forced into one of the other
three labels. That would blur those labels' definitions. In the final dataset
the label covers 28 of 200 posts (14%), which is more than
`plot_clarification` (24).

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
> **[Practical Magic 2 had the cast and the world but not the script](https://www.reddit.com/r/movies/comments/1x72tbn/practical_magic_2_had_the_cast_and_the_world_but/)**
> "Kylie is the one trying to break the curse, yet we barely see her do any
> magic and her sister Antonia is hardly part of the plot. For a film that says
> sisterhood is the strongest magic, the new sisters never get to show it."

**Example 2:**
> **["Sacrifice" is genuine absurdism](https://www.reddit.com/r/movies/comments/1x7z5ae/sacrifice_is_genuine_absurdism/)**
> "By absurdism, I am referring to Camus' philosophy..." The post then quotes
> Camus and *The Stranger* to argue that the film fits that philosophy.

### `personal_reaction`

**Definition:** A post whose main purpose is sharing an immediate feeling,
preference, or first impression without a sustained evidence-based argument.

**Example 1:**
> **[Just watched Shawshank redemption and OH MY GOD!](https://www.reddit.com/r/movies/comments/1x9a0ty/just_watched_shawshank_redemption_and_oh_my_god/)**
> "Where do I even begin?... Honestly I can't describe how incredible this
> movie was with just words... I really can't! Just so incredible... So
> beautiful... Definitely my favorite movie!"

**Example 2:**
> **[I just watched Coco for the first time ever…I haven't cried like that in a minute!](https://www.reddit.com/r/movies/comments/1x96x0q/i_just_watched_coco_for_the_first_time_everi/)**
> "Last night I watched Coco for the first time ever and wow, I did not expect
> that ending! ... I started crying and my kids asked if I was alright"

### `plot_clarification`

**Definition:** A post whose main purpose is asking about or explaining what
happened in a movie, what the ending means, or how the story should be
understood, rather than judging the movie's quality.

**Example 1:**
> **[La Bola Negra questions](https://www.reddit.com/r/movies/comments/1x96ulf/la_bola_negra_questions/)**
> "Why does the Nationalist soldier who both sees Sebastian caressing Rafael
> and catches him talking to Rafael when he's in jail, help him and bring
> Rafael to him so they can talk alone? Why doesn't he report him?"

**Example 2:**
> **[Was the ending to Thelma and Louise meant to be satirical?](https://www.reddit.com/r/movies/comments/1x89zou/was_the_ending_to_thelma_and_louise_meant_to_be/)**
> "So I wonder, were they trying to go for a bittersweet honest feeling, or are
> they trying to make you feel like the ending is much more darker as a result
> and it's meant to be satirical darkness?"

### `industry_news`

**Definition:** A post whose main purpose is discussing an external movie-
industry event or decision, such as casting, a trailer, a release plan, or a
studio choice, rather than a completed movie's content.

**Example 1:**
> **[All Dogs Go To Heaven... any chance the Bluth cut (PG) cut gets released?](https://www.reddit.com/r/movies/comments/1x8r05n/all_dogs_go_to_heaven_any_chance_the_bluth_cut_pg/)**
> "Is there ANY chance this exists? Is it long gone? A lost myth? Bluth's said
> it's gone, but isn't there an HD still?"

**Example 2:**
> **[Joe Manganiello reveals plot of Ben Affleck's scrapped Batman film](https://www.reddit.com/r/movies/comments/1x8qn8x/joe_manganiello_reveals_plot_of_ben_afflecks/)**
> "From the article: • Deathstroke would be the main villain, dismantling
> Batman's life after thinking he killed his son"

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
| **Total** | 200 | 100% |

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

**4.**
> *The post:* [An Explanation of Na Hong-Jin's HOPE](https://www.reddit.com/r/movies/comments/1x87pug/an_explanation_of_na_hongjins_hope/),
> a long breakdown of what the film is about, which the writer says is "a
> smart movie, made by someone with a track record of making smart movies, and
> worth engaging with."
>
> *Could have been:* `plot_clarification` or `analysis_review`
>
> *I chose, because:* `analysis_review`. The title says "explanation", but by
> the decision rule the post's main goal is to defend the film's quality
> against people calling it a parody or "all over the place", not to resolve
> what happened. The explanation is evidence for that judgment.

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
| Overall accuracy | 0.300 | 0.433 | +0.133 |
| Macro F1 | 0.239 | 0.151 | -0.088 |
| F1 — `analysis_review` | 0.308 | 0.000 | -0.308 |
| F1 — `industry_news` | 0.316 | 0.000 | -0.316 |
| F1 — `personal_reaction` | 0.333 | 0.605 | +0.271 |
| F1 — `plot_clarification` | 0.000 | 0.000 | +0.000 |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

Before seeing the results, I predicted that the trained model would beat the
zero-shot baseline most clearly on `personal_reaction`, but would most likely
not beat it on `analysis_review`, `plot_clarification`, or `industry_news`.

**What the gap actually means:**
I also ran the baseline without `label_definitions.txt`, using only the bare
label names. The definitions-based baseline had 0.300 accuracy and 0.239 macro
F1. The bare-label baseline had higher accuracy at 0.433 but lower macro F1 at
0.200.

| Measure | With Definitions | Bare Label Names | Bare - Definitions |
|---|---:|---:|---:|
| Overall accuracy | 0.300 | 0.433 | +0.133 |
| Macro F1 | 0.239 | 0.200 | -0.039 |
| F1 — `analysis_review` | 0.308 | 0.200 | -0.108 |
| F1 — `industry_news` | 0.316 | 0.000 | -0.316 |
| F1 — `personal_reaction` | 0.333 | 0.600 | +0.267 |
| F1 — `plot_clarification` | 0.000 | 0.000 | +0.000 |

This shows that the definitions improved balance across labels, especially
`industry_news`, even though they reduced overall accuracy on this split. The
definitions-based run remains the official baseline because it is the fair
comparison using the taxonomy written for the task. The bare-label results are
recorded in `baseline_results_bare.json` as an additional ablation.
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

### Three-seed spread

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---|---|---|---|
| Overall accuracy | 0.433 | 0.433 | 0.433 | 0.000 |
| Macro F1 | 0.151 | 0.151 | 0.151 | 0.000 |
| F1 — `analysis_review` | 0.000 | 0.000 | 0.000 | 0.000 |
| F1 — `personal_reaction` | 0.605 | 0.605 | 0.605 | 0.000 |
| F1 — `plot_clarification` | 0.000 | 0.000 | 0.000 | 0.000 |
| F1 — `industry_news` | 0.000 | 0.000 | 0.000 | 0.000 |

Accuracy moved 0.000 across seeds. The score is stable across seeds, but the
model consistently collapses into `personal_reaction`; stability does not mean
the model meets the targets.

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

**Device:** `cpu` (CPU)

| true \ predicted | analysis_review | personal_reaction | plot_clarification | industry_news |
|---|---|---|---|---|
| **analysis_review** | 0 | 9 | 0 | 0 |
| **personal_reaction** | 0 | 13 | 0 | 0 |
| **plot_clarification** | 0 | 4 | 0 | 0 |
| **industry_news** | 0 | 4 | 0 | 0 |

**My biggest off-diagonal number, and what it means:**
The biggest confusion is 9 real `analysis_review` posts classified as
`personal_reaction`, while 0 real `personal_reaction` posts were classified as
`analysis_review`. This is lopsided: the model leans toward
`personal_reaction` on this pair. The agreement report will help determine
whether this points to inconsistent labeling or a model limitation.
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
