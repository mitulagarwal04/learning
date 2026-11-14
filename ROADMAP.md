# Roadmap — 32 weeks

Each week ≈ 9.5h: **D** = deep 2h sessions (4 a week), **L** = light 30m sessions (3 a week).
Each week has a **main** line (most of the deep sessions) and a **side** line (one deep session plus the light sessions, usually math/ML).
Learning paths with links are in `weeks/week-NN.md`, written one week ahead. When you finish a week, Claude assesses you on the last column (plus anything else from that week) and updates PROGRESS.md.

---

## Phase 1 — Foundations (W1–W4) · 12 Nov → 9 Dec

| Wk | Dates | Main | Side | Assessed on |
|---|---|---|---|---|
| 1 | Nov 12–18 | Git (core workflow, branching, PRs), `uv`, ruff, pytest, type hints, mypy | Vectors and dot product (3B1B LA 1–2, 9); NumPy vectorization | Typed `Vector` lib with ≥10 tests, mypy strict clean; ≥2 merged PRs; Python-vs-NumPy benchmark numbers |
| 2 | Nov 19–25 | Python depth: generators, decorators, context managers, dataclasses vs Pydantic; intro to `asyncio` | Matrices and matmul as transformations (3B1B 3–4, 7) | Your own `@retry(backoff)` decorator + `timer` context manager, tested; explain event loop vs threads |
| 3 | Nov 26–Dec 2 | `asyncio` deeper (tasks, gather, semaphores, timeouts), HTTP/TCP/DNS/TLS basics, `httpx` | Linear regression from scratch: normal equation + gradient descent | Async concurrent fetcher with rate limiting and retries; linear regression matches sklearn to 1e-4 |
| 4 | Dec 3–9 | SQL in Postgres: joins, GROUP BY, indexes, transactions, EXPLAIN; Docker basics: images, Dockerfile, volumes, `docker run` Postgres | Logistic regression from scratch; cross-entropy loss | 10 SQL query exercises on a real dataset, plus one index speedup measured with EXPLAIN ANALYZE; your own Dockerfile for a Python script |

## Phase 2 — Backend + classic ML (W5–W10) · 10 Dec → 20 Jan

| Wk | Dates | Main | Side | Assessed on |
|---|---|---|---|---|
| 5 | Dec 10–16 | FastAPI: routing, Pydantic v2, dependency injection, errors, TestClient. **Start the `docmind` repo** | Derivatives, partial derivatives, chain rule (3B1B Calculus 1–4) | `docmind` v0.0: CRUD for documents (in-memory), 100% of endpoints tested |
| 6 | Dec 17–23 | SQLAlchemy 2.0 async, Alembic migrations, Postgres-backed CRUD, pagination | sklearn: bias/variance, L1/L2, cross-validation | Migrations run up and down cleanly; explain N+1 queries and fix one |
| 7 | Dec 24–30 | Auth: password hashing, JWT, API keys, pydantic-settings, structured logging | Trees, random forest, gradient boosting (XGBoost/LightGBM) | Users can register/login; protected routes; tests cover expired and tampered tokens |
| 8 | Dec 31–Jan 6 | Redis, task queue (arq), file upload → background processing; docker compose (api+db+redis+worker) | Metrics (P/R/F1, ROC-AUC), data leakage; **start the Kaggle tabular project** | `docker compose up` runs the whole stack; uploading a file triggers a worker job |
| 9 | Jan 7–13 | GitHub Actions CI: ruff, mypy, pytest with a Postgres service, build + push the image | Finish the Kaggle project; probability and stats basics (distributions, Bayes, MLE) | CI green on every PR; Kaggle project with an honest CV score and a written leakage check |
| 10 | Jan 14–20 | **Buffer / catch-up**, then Rust Book ch. 1–4 (ownership, borrowing) | Review weak math | Phase-2 review: demo `docmind` v0.1 end to end; Rustlings: variables → move_semantics |

## Phase 3 — Rust, DL foundations, LLM basics (W11–W16) · 21 Jan → 3 Mar

| Wk | Dates | Main | Side | Assessed on |
|---|---|---|---|---|
| 11 | Jan 21–27 | Rust ch. 5–10: structs, enums, match, modules, collections, errors, traits, generics | Gradients; Karpathy *micrograd* part 1 | Rustlings through traits; a CLI word-frequency counter in Rust |
| 12 | Jan 28–Feb 3 | Rust ch. 13 (iterators/closures) + tests; `rayon` | Finish micrograd → MLP trained on a toy dataset | Your micrograd's gradients match PyTorch on 3 test expressions |
| 13 | Feb 4–10 | **PyO3 + maturin**: first module, then a Rust text chunker used inside `docmind` | PyTorch: tensors, autograd, nn.Module, training loop | Rust chunker installed as a wheel in `docmind`, built in CI, benchmarked against the Python version |
| 14 | Feb 11–17 | LLM APIs: messages, streaming, structured outputs, tool calling, retries, cost tracking | LLM internals: build a BPE tokenizer; embeddings; attention (Karpathy "Let's build the GPT tokenizer") | Your BPE tokenizer round-trips text; a script that calls a tool and returns a validated Pydantic object |
| 15 | Feb 18–24 | `docmind` chat endpoint with SSE streaming | **Mini-GPT from scratch** (Karpathy "Let's build GPT"), trained on Colab | Mini-GPT generates text from your own training run; explain the KV cache and why attention is O(n²) |
| 16 | Feb 25–Mar 3 | Vector search: brute force → Rust top-k cosine (numpy zero-copy, rayon); pgvector, IVF vs HNSW | Information theory: entropy, cross-entropy, KL | Benchmark table (Python / NumPy / Rust / pgvector-HNSW); explain the recall-vs-speed tradeoff of HNSW |

## Phase 4 — RAG and agents (W17–W22) · 4 Mar → 14 Apr

| Wk | Dates | Main | Side | Assessed on |
|---|---|---|---|---|
| 17 | Mar 4–10 | **RAG v1, no framework**: parse → chunk → embed → pgvector → answer with citations | Read Chip Huyen *AI Engineering* ch. on RAG | Ask a question over uploaded PDFs and get a cited answer, streamed |
| 18 | Mar 11–17 | **Evals**: golden set (≥50 Qs), recall@k, MRR, faithfulness; BM25 + hybrid (RRF); reranker | — | Eval report: baseline vs hybrid vs +rerank, with numbers |
| 19 | Mar 18–24 | Advanced retrieval: query rewriting, contextual retrieval; Langfuse/OTel tracing | Buffer for math/ML review | Every request traced; at least one retrieval change shown to improve the eval |
| 20 | Mar 25–31 | Agent loop from scratch (tool calling, max steps, error handling); LangChain basics | — | Your own agent loop solves 5 multi-step tasks; the same agent rebuilt in LangChain, with notes on the differences |
| 21 | Apr 1–7 | **LangGraph**: state, conditional edges, checkpoints, human-in-the-loop; write an MCP server | — | `docmind` research agent (search → read → answer) with resumable state; MCP server exposing docmind search |
| 22 | Apr 8–14 | Prompt injection and defenses, semantic cache, cost limits; **evals run in CI** | **Buffer** | `docmind` v0.5 demo; CI fails if eval scores regress |

## Phase 5 — Inference, fine-tuning, deployment (W23–W29) · 15 Apr → 2 Jun

| Wk | Dates | Main | Side | Assessed on |
|---|---|---|---|---|
| 23 | Apr 15–21 | Self-hosting: HF transformers, Ollama; GPU memory math; quantization (GGUF/AWQ) | — | Predict VRAM for a 7B model at fp16/int4 before loading it, then verify |
| 24 | Apr 22–28 | **vLLM** on vast.ai (or the work 4090s): continuous batching, OpenAI-compatible server; load test | — | Throughput/TTFT benchmark at concurrency 1/8/32; `docmind` switches between an API model and vLLM via config |
| 25 | Apr 29–May 5 | **Batch processing**: provider batch APIs, queue pipelines, backpressure, idempotent jobs | — | Re-embed the whole corpus as a resumable batch job (kill it halfway; it resumes) |
| 26 | May 6–12 | Fine-tuning: LoRA/QLoRA (PEFT) on Colab; fine-tune an embedding model on your domain | — | Fine-tuned embedder improves recall@k on your golden set (or a written analysis of why it didn't) |
| 27 | May 13–19 | Kubernetes with `kind`: pods, deployments, services, configmaps, secrets, probes | — | `docmind` running on kind; kill a pod and it recovers |
| 28 | May 20–26 | Ingress, HPA, Helm chart; Prometheus + Grafana, OpenTelemetry | — | Helm install of the whole stack; a Grafana dashboard with latency, error rate and tokens/sec |
| 29 | May 27–Jun 2 | AWS basics (IAM, ECR, managed Postgres, a small K8s or ECS deploy), Terraform intro, CD pipeline | — | A push to main deploys to the cloud; you can tear it all down with one command |

## Phase 6 — System design and wrap-up (W30–W32) · 3 Jun → 23 Jun

| Wk | Dates | Main | Assessed on |
|---|---|---|---|
| 30 | Jun 3–9 | System design: RAG platform, LLM gateway, batch inference pipeline, recommender | Whiteboard 2 designs in 45 min each, with tradeoffs |
| 31 | Jun 10–16 | `docmind` hardening: README, architecture doc, demo video, load test | A stranger can run it from the README |
| 32 | Jun 17–23 | Final review across all gates; gap list | Self-assessment against CURRICULUM.md; plan for what comes next |

Weeks 33–35 (to the 8-month mark) are reserved buffer: redo failed assessments, go deeper on weak areas, or add CV/speech.
