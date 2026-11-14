# AI Engineering Curriculum — Topic Map (v1)

The full list of topics. **ROADMAP.md** gives the week-by-week order, and **PROGRESS.md** has the checkboxes.

## Scope for your time budget

Weekly time: 4 deep sessions × 2h plus 3 light sessions × 30m ≈ **9.5 h/week**. Over 32 weeks that's **~300 hours**, which is enough only if every hour counts. Hours per track:

| Track | Hours | Note |
|---|---|---|
| 0 Foundations (Python depth, Git, Linux, SQL) | ~35 | front-loaded in months 1–2 |
| 1 FastAPI backend | ~40 | becomes the capstone's skeleton |
| 2 Rust + PyO3 | ~30 | only the Rust needed for extension modules |
| 3 DevOps / MLOps | ~40 | Docker early, CI in month 3, K8s/cloud in months 6–7 |
| 4 AI / LLM engineering | ~85 | the largest track, on purpose |
| 5 Math + ML + DL | ~70 | math explained, then implemented in code |

**Cut or reduced to "aware" level to fit the time:** async Rust/tokio, CNN/RNN depth, DPO, Terraform beyond basics, LlamaIndex, dedicated vector DBs besides pgvector + one look at Qdrant, TensorRT, CV, and speech. Any of these can come back in the buffer weeks or after the plan ends.
**Cloud provider:** AWS by default, since it shows up most in job listings. Switching to GCP is fine; just tell me.

Legend: **[core]** must learn in depth · **[working]** be able to use it confidently · **[aware]** know what it is and when to reach for it
`(+)` = something you didn't list that I've added, with the reason why.

---

## Track 0 — Foundations nobody lists but everything depends on (+)

Without these, every other track turns into copy-pasting.

| Topic | Level | Why |
|---|---|---|
| Python depth: type hints, dataclasses/Pydantic, generators, context managers, decorators | core | FastAPI and LangGraph are built on these |
| `asyncio`: event loop, `async/await`, tasks, gather, when async *doesn't* help (CPU-bound) | core | FastAPI performance, concurrent LLM calls, batch inference |
| Packaging: `uv`, `pyproject.toml`, virtual envs, wheels | core | You can't ship Rust modules or Docker images without it |
| Testing: `pytest`, fixtures, mocking, testing async code | core | CI/CD has nothing to run without tests |
| Profiling: `cProfile`, `py-spy`, memory profiling | working | This is how you decide what to rewrite in Rust |
| Linux + shell: processes, signals, env vars, permissions, `ssh`, `tmux` | working | Docker and K8s are Linux underneath |
| Networking basics: HTTP/1.1 vs 2, TCP, DNS, TLS, WebSockets, SSE | working | Streaming LLM tokens = SSE/WebSockets |
| Git properly: branching, rebase vs merge, resolving conflicts, PR workflow | core | Also the base of Track 3 |

## Track 1 — Backend with FastAPI

| Topic | Level |
|---|---|
| HTTP & REST design: status codes, idempotency, pagination, versioning | core |
| FastAPI: routing, Pydantic v2 models, dependency injection, lifespan events, middleware | core |
| Sync vs async endpoints; threadpool; blocking calls inside async | core |
| Streaming responses (SSE) for LLM output; WebSockets | core |
| Auth: password hashing, JWT, OAuth2 flows, API keys, rate limiting | core |
| **(+) SQL + PostgreSQL**: schema design, indexes, transactions, EXPLAIN | core — this is also your vector DB later (pgvector) |
| SQLAlchemy 2.0 (async) + Alembic migrations | core |
| **(+) Redis**: caching, rate limiting, queues, semantic cache | working |
| **(+) Background work**: FastAPI BackgroundTasks → task queues (Celery / arq / Dramatiq) | core — needed for batch processing and ingestion |
| Error handling, structured logging, settings management (pydantic-settings) | core |
| Testing APIs (TestClient / httpx), load testing (locust / k6) | working |
| API security: CORS, input validation, OWASP top 10 basics | working |

## Track 2 — Rust for Python extension modules

| Topic | Level |
|---|---|
| Rust basics: ownership, borrowing, lifetimes, structs/enums, pattern matching | core |
| Error handling (`Result`, `?`, `thiserror`/`anyhow`), traits, generics | core |
| Iterators, closures, collections | core |
| Cargo, crates, modules, testing in Rust | core |
| Concurrency: threads, `rayon` for data parallelism, `Send`/`Sync` | working |
| **PyO3**: exposing functions/classes, converting types, the GIL and releasing it | core |
| **maturin**: building and publishing wheels, mixed Python/Rust projects | core |
| `numpy` crate: zero-copy arrays between Python and Rust | working |
| Benchmarking honestly: Python vs NumPy vs Rust, criterion | working |
| async Rust / tokio | aware — not needed for extension modules at first |

Realistic AI-flavored Rust modules to build: a text chunker/tokenizer, a BM25 index, a fast cosine-similarity / top-k search, a log/JSONL parser for batch jobs. (Hugging Face `tokenizers`, Pydantic v2 core, Polars, `ruff`, and `uv` are all Rust under a Python API — this is the pattern you're learning.)

## Track 3 — Deployment & maintenance (DevOps / MLOps)

| Topic | Level |
|---|---|
| Docker: images vs containers, layers, multi-stage builds, slim images for Python + Rust | core |
| docker compose: running API + Postgres + Redis + worker locally | core |
| CI/CD with GitHub Actions: lint (ruff), type-check (mypy/pyright), test, build, push image | core |
| Kubernetes: pods, deployments, services, ingress, configmaps/secrets, probes, HPA | core |
| Local K8s with `kind`/`k3d`, then Helm charts | working |
| **(+) Observability**: Prometheus metrics, Grafana, OpenTelemetry tracing, log aggregation | core — "maintenance" is mostly this |
| **(+) One cloud provider** (AWS or GCP): IAM, VMs, object storage, managed Postgres, container registry | working |
| (+) Terraform basics (infrastructure as code) | aware → working |
| (+) GPU deployment: NVIDIA container toolkit, GPU node pools | aware |
| Release practices: semantic versioning, blue/green & canary deploys, rollbacks | working |
| ML-specific: model registry & experiment tracking (MLflow / W&B), data versioning (DVC) | working |

## Track 4 — AI / LLM engineering

**4a. How LLMs actually work (+)** — needed to reason about inference, cost, and failures
- Tokenization (BPE), embeddings, transformer architecture, attention, positional encodings — core
- Sampling: temperature, top-p, top-k, logprobs — core
- Context windows, KV cache, why long prompts cost what they cost — core

**4b. Using models via API**
- Chat/messages APIs, system prompts, prompt engineering that's tested rather than guessed — core
- Structured outputs / JSON schema, tool (function) calling — core
- Streaming, retries, timeouts, rate limits, cost tracking — core
- Provider abstraction (OpenAI-compatible APIs, LiteLLM) — working

**4c. Embeddings, vectors, retrieval**
- Embedding models, cosine vs dot product, normalization — core
- Vector indexes: flat, IVF, HNSW, product quantization (what tradeoffs each makes) — core
- Vector stores: **pgvector** (core), plus one dedicated store (Qdrant / Weaviate / Milvus) — working; FAISS — working
- Hybrid search: BM25 + dense, reciprocal rank fusion — core

**4d. RAG — done properly**
- Ingestion pipeline: parsing PDFs/HTML, chunking strategies, metadata — core
- Retrieval → reranking (cross-encoders) → generation with citations — core
- Advanced: query rewriting, multi-query, parent-document, contextual retrieval, GraphRAG — working
- **(+) RAG evaluation**: retrieval metrics (recall@k, MRR, nDCG), answer faithfulness, building a golden test set — core. This separates engineers from tutorial-followers.

**4e. Frameworks & agents**
- Build a RAG app and an agent loop **without frameworks first** — core
- LangChain (LCEL, retrievers, tools) — working
- **LangGraph**: state graphs, nodes/edges, checkpoints, human-in-the-loop, multi-agent — core
- LlamaIndex — aware (know when it fits better than LangChain)
- (+) **MCP (Model Context Protocol)**: writing tool servers — working
- Agent failure modes: loops, tool errors, cost blowups, guardrails — core

**4f. Inference & batch processing**
- Self-hosting open models: Hugging Face `transformers`, Ollama/llama.cpp locally — core
- **vLLM**: continuous batching, PagedAttention, OpenAI-compatible server — core
- Quantization: int8/int4, GGUF, AWQ/GPTQ; the quality vs memory tradeoff — working
- Throughput vs latency, TTFT, tokens/sec, GPU memory math — core
- Batch processing: offline batch jobs, provider batch APIs, queue-based pipelines, backpressure — core
- Speculative decoding, prefix caching — aware
- ONNX Runtime / TensorRT — aware

**4g. Fine-tuning (+)**
- When to fine-tune vs prompt vs RAG — core
- LoRA / QLoRA with PEFT, dataset preparation — working
- Fine-tuning embedding models for your domain — working
- Preference tuning (DPO) — aware

**4h. Production LLM concerns (+)**
- LLM observability/tracing (Langfuse / LangSmith / OpenTelemetry) — core
- Evals as CI: regression tests for prompts and pipelines — core
- Security: prompt injection, data leakage, PII handling — core
- Caching (exact + semantic), cost controls — working

## Track 5 — Classic ML & deep learning (with the math)

**5a. Math** (learn each piece right before the ML that needs it, not all upfront)
- Linear algebra: vectors, matrix multiplication, dot products, norms, eigen-decomposition, SVD — core
- Calculus: derivatives, partial derivatives, chain rule, gradients, Jacobians — core
- Probability & statistics: distributions, Bayes, expectation/variance, MLE, hypothesis testing — core
- Optimization: gradient descent, SGD, momentum, Adam, convexity — core
- Information theory: entropy, cross-entropy, KL divergence — core (this *is* the LLM loss function)

**5b. Classic ML**
- NumPy fluency; pandas / **(+) Polars** for data work — core
- Linear & logistic regression **from scratch**, then scikit-learn — core
- Bias/variance, regularization (L1/L2), cross-validation, feature engineering — core
- Trees, random forests, gradient boosting (XGBoost/LightGBM) — core
- k-NN, k-means, PCA — core (PCA = SVD in action)
- Metrics: precision/recall/F1, ROC-AUC, calibration; data leakage — core

**5c. Deep learning**
- Backprop from scratch (an autograd engine like micrograd) — core
- **PyTorch**: tensors, autograd, `nn.Module`, DataLoader, training loops, GPU — core
- MLPs, initialization, normalization (BatchNorm/LayerNorm), dropout, residual connections — core
- CNNs (enough to understand them), RNNs (enough to understand why transformers replaced them) — working
- **Transformer from scratch** (a small GPT trained on text) — core; ties back to 4a
- Training at scale: mixed precision, gradient accumulation, checkpointing — working

## Track 6 — System design for AI apps (+)

Putting the tracks together: design a RAG platform, an LLM gateway, a batch inference pipeline, a recommendation system. Covers queues, caching layers, scaling stateless vs stateful services, and failure handling. This is also what interviews test.

---

## Project spine (draft)

Instead of 20 disconnected toy projects: **a few from-scratch learning builds plus one capstone that grows every month.**

**Learning builds (small, focused):**
1. Linear/logistic regression from scratch in NumPy
2. micrograd-style autograd engine → MLP
3. Mini-GPT in PyTorch trained on a text corpus
4. A Kaggle-style tabular problem with honest validation
5. Rust extension: fast top-k cosine similarity / BM25, benchmarked against NumPy

**Capstone — a self-hosted document intelligence platform** (each month adds a layer):
- FastAPI service with auth, Postgres, Alembic, tests
- Async ingestion pipeline (task queue) → chunking (your Rust module) → embeddings → pgvector
- Hybrid search + reranking + cited answers, streamed over SSE
- LangGraph agent on top (tool use, multi-step research)
- Self-hosted model via vLLM / Ollama alongside an API model; batch re-embedding jobs
- Evaluation harness running in CI
- Docker → compose → Kubernetes (kind, then cloud) with GitHub Actions, Prometheus/Grafana, tracing

---

## Ordering

See **ROADMAP.md** for the 32-week plan with an assessment at the end of every week.

## Core references (short list on purpose)

- FastAPI: official docs + tutorial; SQLAlchemy 2.0 docs
- Rust: *The Rust Programming Language* (the Book), *Rust by Example*, PyO3 user guide, maturin docs
- DevOps: Docker docs; Kubernetes docs (Concepts + Tasks); GitHub Actions docs
- AI engineering: Chip Huyen — *AI Engineering*; vLLM docs; LangGraph docs
- ML/DL: Karpathy — *Neural Networks: Zero to Hero*; *Mathematics for Machine Learning* (Deisenroth et al., free PDF); 3Blue1Brown linear algebra & neural nets series; Géron — *Hands-On Machine Learning*; *Dive into Deep Learning* (d2l.ai)
- Systems: Kleppmann — *Designing Data-Intensive Applications*; Chip Huyen — *Designing Machine Learning Systems*
