# Week 1 · Nov 12–18 · Git, Python tooling, typing · vectors and NumPy

**Why this week matters:** every later week assumes you can branch, commit, open PRs, and run typed, tested Python. The `Vector` library you write here is the slow baseline that your NumPy code (this week) and your Rust code (week 16) will be measured against.

**How to use this file:** work top to bottom. Each block lists links **in the order to use them**: 📺 = watch, 📖 = read, 🛠 = do. Time estimates assume ~9.5h for the week. When you've finished, tell me "week 1 done" (or which blocks you finished) and I'll assess you.

---

## Block 1 · Git: the mental model + core commands (~2h)

1. 📺 **Missing Semester — Version Control (Git)** (MIT, ~1h20). Watch the whole thing: it teaches the *data model* (blobs, trees, commits, refs) first, which is what makes Git stop feeling like magic.
   https://missing.csail.mit.edu/2020/version-control/
2. 📖 **Pro Git ch. 2 — Git Basics**, sections 2.1–2.5. Type every command yourself in a scratch repo.
   - 2.1 Getting a repo: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository
   - 2.2 Recording changes: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
   - 2.3 Viewing history: https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History
   - 2.4 Undoing things: https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things
   - 2.5 Remotes: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
3. 🛠 Set up GitHub SSH keys:
   https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
   https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
4. 🛠 Create the GitHub repo **`ai-eng-lab`** with a README and `.gitignore` (Python template), and push ≥3 commits with meaningful messages.

**Done when:** you can predict what `git status` will show *before* you run it, after any `add` / `commit` / `restore`.

## Block 2 · Branching, merging, rebasing, PRs (~2h)

1. 📖 **Pro Git ch. 3**:
   - 3.1 Branches in a nutshell: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
   - 3.2 Basic branching and merging: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
   - 3.6 Rebasing (read "The Perils of Rebasing" carefully): https://git-scm.com/book/en/v2/Git-Branching-Rebasing
2. 🛠 **Learn Git Branching** (interactive). Do *Main → Introduction Sequence* and *Main → Ramping Up*, plus *Remote → Push & Pull*.
   https://learngitbranching.js.org/
3. 🛠 In `ai-eng-lab`: make the same line diverge on `main` and on a branch, then **merge and resolve the conflict by hand**. Repeat the same scenario with `rebase`.
4. 🛠 Open a PR from a branch, review your own diff on GitHub, and merge it.
   https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

**Done when:** you've resolved one conflict via merge and one via rebase, and have ≥2 merged PRs.

## Block 3 · Vectors and the dot product (~1h, light-day material)

1. 📺 3Blue1Brown, *Essence of Linear Algebra* ch. 1 — Vectors: https://www.3blue1brown.com/lessons/vectors
2. 📺 Ch. 2 — Linear combinations, span, and basis vectors: https://www.3blue1brown.com/lessons/span
3. 📺 Ch. 9 — Dot products and duality: https://www.3blue1brown.com/lessons/dot-products
   (The full playlist is on YouTube if you prefer: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
4. 🛠 On paper: derive why cos θ = a·b / (|a||b|), and compute it for a couple of 2D vectors you can draw.

**Done when:** you can explain why cosine similarity ignores vector *length*, and why that matters for comparing text embeddings.

## Block 4 · Python tooling: uv, ruff, pytest, mypy (~2h)

1. 📖 **uv**: install it, then work through the projects guide.
   - Install: https://docs.astral.sh/uv/getting-started/installation/
   - Working on projects: https://docs.astral.sh/uv/guides/projects/
   - Dev dependencies (`uv add --dev`): https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies
2. 📖 **ruff** tutorial and configuration:
   https://docs.astral.sh/ruff/tutorial/
   https://docs.astral.sh/ruff/configuration/
3. 📖 **pytest**: getting started, then parametrize, and assertions about exceptions.
   https://docs.pytest.org/en/stable/getting-started.html
   https://docs.pytest.org/en/stable/how-to/parametrize.html
   https://docs.pytest.org/en/stable/how-to/assert.html
   `pytest.approx` (floats!): https://docs.pytest.org/en/stable/reference/reference.html#pytest-approx
4. 📖 **Type hints + mypy**:
   - mypy getting started: https://mypy.readthedocs.io/en/stable/getting_started.html
   - Type hints cheat sheet (keep this open): https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
   - Config file (`strict = true` in pyproject): https://mypy.readthedocs.io/en/stable/config_file.html
5. 🛠 In `ai-eng-lab/week01/`: `uv init`, add `pytest`, `ruff` and `mypy` as dev dependencies, configure ruff + mypy strict in `pyproject.toml`.

## Block 5 · Build: a typed `Vector` library (~1.5h)

1. 📖 Python data model, the dunder methods for numeric types (`__add__`, `__mul__`, `__rmul__`, `__eq__`...):
   https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
2. 🛠 Write `vecmath.py`, a **pure Python** (no NumPy) `Vector` class:
   - `__init__` from a sequence of floats, `__len__`, `__repr__`, `__eq__`, `__add__`, `__sub__`, `__mul__` (scalar), `__rmul__`
   - `dot`, `norm`, `normalize`, `cosine_similarity`
   - a clear `ValueError` on a dimension mismatch or a zero-norm normalize
   - full type hints, with no `Any`
3. 🛠 Write **≥10 tests** (parametrize them; use `pytest.approx`; test that errors are raised).
4. 📖 dataclasses: https://docs.python.org/3/library/dataclasses.html, then Pydantic models: https://docs.pydantic.dev/latest/concepts/models/
5. 🛠 Refactor `Vector` to `@dataclass(frozen=True, slots=True)` holding a `tuple[float, ...]`, and keep the tests green.
6. 🛠 `ruff check`, `ruff format --check`, `mypy --strict` and `pytest` must all pass. Merge it via a PR.

**Done when:** all four tools pass, and you can say when you'd reach for Pydantic instead of a dataclass.

## Block 6 · NumPy + your first honest benchmark (~2h)

1. 📖 NumPy: the absolute basics for beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
2. 📖 Broadcasting (read this one slowly): https://numpy.org/doc/stable/user/basics.broadcasting.html
3. 📖 `np.argpartition`, for top-k without a full sort: https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html
4. 📖 `timeit`: https://docs.python.org/3/library/timeit.html
5. 🛠 `week01/vec_np.py`: `cosine_similarity(a, b)` and `top_k(query, matrix, k)` (one query vs N stored vectors → indices of the k most similar), with **no Python loops**.
6. 🛠 `week01/bench.py`, reporting the median of ≥5 repeats:
   - dot product of two 1,000,000-dim vectors: your `Vector` vs NumPy
   - top-5 search: one 384-dim query vs 10,000 random 384-dim vectors: pure Python vs NumPy
   Commit the results table into `week01/README.md`.

384 dims is the size of a common small embedding model. You'll do this exact search for real in week 16, and again in Rust.

---

## What you'll be assessed on

When you say you're done, expect a mix of:
- **MCQs and short answers:** Git internals (working tree / index / commits / refs), merge vs rebase and when *not* to rebase, `restore` vs `reset`, broadcasting rules, dataclass vs Pydantic.
- **Code tasks:** a live coding problem (e.g. a vectorized NumPy function, or adding a typed method plus tests), a broadcasting shape puzzle, and a broken `git log --graph` scenario to fix.
- **Math:** cosine similarity by hand, and reasoning questions about vector geometry.
- **Review of your repo:** `ai-eng-lab/week01` must pass ruff, mypy strict and pytest, and the benchmark table must be in it.

Passing ≈ 75% overall **and** the code tasks working. Anything below that gets a short targeted re-do before week 2.
