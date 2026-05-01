# AskAnything 🤖 — Mini AI Answer Engine with Retrieval & Summarization

> **Ask a question. Get a cited, summarized answer in seconds — powered by Wikipedia retrieval and transformer-based summarization.**
>
> [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org) [![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)](https://streamlit.io) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
>
> ---
>
> ## 🚀 Product Overview
>
> **The Problem:** AI-powered search is reshaping how people find information — but understanding how it works under the hood is difficult without a real implementation. Most demos are either black-box API wrappers or overly complex RAG pipelines. There's no simple, inspectable prototype showing the core Retrieve → Summarize → Cite loop that powers AI answer engines.
>
> **The Solution:** AskAnything is a minimal but complete AI answer engine. It retrieves the top 3 Wikipedia articles for any query, summarizes them using Facebook's BART transformer model, and returns a cited, concise answer — all in one Streamlit interface.
>
> **The Impact:**
> - 🔍 Demonstrates a **working RAG (Retrieval-Augmented Generation) pattern** end-to-end
> - - 📝 Produces **cited answers** — not hallucinated responses — by grounding in retrieved content
>   - - ⚡ Shows how AI search works under the hood in **under 100 lines of code**
>     - - 🎓 Serves as a **learning tool** for PMs and engineers exploring AI search architecture
>      
>       - ---
>
> ## 🎯 Why This Matters (Product Perspective)
>
> AI answer engines (Perplexity, Google AI Overviews, Bing Copilot) are reshaping search — and every AI PM needs to understand how they work. This prototype demonstrates the core architecture: **retrieve relevant context → summarize with an LLM → cite your sources**. As a PM building AI search features, this project shows I can go from concept to working prototype — and understand the tradeoffs in retrieval quality, summarization accuracy, and latency.
>
> ---
>
> ## 🧠 AI/ML Explanation
>
> | Component | Technique | Why It Was Chosen |
> |---|---|---|
> | **Information Retrieval** | Wikipedia API (keyword search) | No API key required; demonstrates retrieval-first architecture |
> | **Summarization Model** | Facebook BART (bart-large-cnn) | State-of-the-art extractive-abstractive summarizer; runs locally |
> | **Grounding** | Retrieved article text passed to summarizer | Prevents hallucination — model can only summarize what was retrieved |
> | **Citation** | Source article titles + URLs displayed | Transparency and auditability — users see where answers came from |
>
> **Why RAG over direct LLM generation?**
> A pure LLM would hallucinate on factual questions. By retrieving real Wikipedia articles first and then summarizing them, we ground the AI's response in verified content. This is the same principle behind enterprise RAG systems used in production AI products.
>
> **Architecture:** Query → Wikipedia Search API → Top 3 Articles → BART Summarizer → Cited Answer
>
> ---
>
> ## 🛠 Tech Stack
>
> | Layer | Technology |
> |---|---|
> | UI | Streamlit |
> | Information Retrieval | Wikipedia-API (Python wrapper) |
> | Summarization | HuggingFace Transformers (facebook/bart-large-cnn) |
> | Language | Python 3.8+ |
>
> ---
>
> ## 📊 Sample Results
>
> Query: *"What is reinforcement learning from human feedback?"*
>
> | Step | Output |
> |---|---|
> | Retrieved Articles | "Reinforcement learning", "OpenAI", "ChatGPT" |
> | Summarized Answer | "Reinforcement learning from human feedback (RLHF) is a technique used to align AI model outputs with human preferences by training a reward model from human feedback and optimizing the language model against it..." |
> | Sources Cited | Wikipedia: Reinforcement learning, Wikipedia: ChatGPT |
> | Latency | ~3.2 seconds (local BART model) |
>
> **Quality Observation:** The retrieval step is the biggest quality bottleneck — keyword-based Wikipedia search misses semantic matches. This is why production systems use embedding-based retrieval (next roadmap item).
>
> ---
>
> ## 📸 Demo Instructions
>
> ```bash
> # 1. Clone the repo
> git clone https://github.com/Poojaahegde/AskAnything-Mini-AI-Answer-Engine.git
> cd AskAnything-Mini-AI-Answer-Engine
>
> # 2. Install dependencies (note: first run will download BART model ~1.6GB)
> pip install -r requirements.txt
>
> # 3. Launch the app
> streamlit run main.py
> ```
>
> Open **http://localhost:8501** in your browser. Type any question and press Enter.
>
> **Note:** First run downloads the BART model (~1.6GB). Subsequent runs are fast.
>
> ---
>
> ## 🎯 Product Thinking Layer
>
> ### 👥 Target Users
> - **AI Product Managers** learning RAG architecture to make better product decisions about AI search features
> - - **Developers** building a first AI search prototype for a product
>   - - **Students** understanding how LLM-based answer engines work under the hood
>    
>     - ### 😣 Pain Points Solved
>     - 1. **"How does AI search actually work?"** — Most PMs and engineers can't answer this concretely; this project makes the architecture tangible and inspectable
>       2. 2. **LLM hallucination** — Direct LLM answers fabricate facts; retrieval-first architecture fixes this
>          3. 3. **No source attribution** — Most AI prototypes don't show their sources; citations are a core trust feature for users
>            
>             4. ### 🧩 Key Product Decisions Made
>             5. - **Wikipedia over web search:** No API key required, high-quality content, perfect for demonstrating retrieval without infrastructure complexity
>                - - **BART over GPT API:** Runs 100% locally — no cost, no latency from API calls, demonstrates the pattern without dependency on OpenAI uptime
>                  - - **Show retrieved articles alongside answer:** Transparency is a product value — users should see where their answer came from
>                    - - **Streamlit for speed-to-demo:** Demonstrates the full user flow (ask → answer → cite) in minutes, not weeks
>                     
>                      - ### 🗺 Future Roadmap
>                      - | Priority | Feature | Expected Impact |
>                      - |---|---|---|
>                      - | P0 | Semantic retrieval using embeddings (FAISS + sentence-transformers) | Major quality improvement over keyword search |
>                      - | P0 | Support custom knowledge bases (upload PDF/docs) | Transforms from demo to enterprise-ready RAG |
>                      - | P1 | OpenAI/Claude API option for summarization | Higher quality answers with GPT-4/Claude 3 |
>                      - | P1 | Relevance scoring for retrieved articles | Show confidence in sources |
>                      - | P2 | Multi-hop reasoning: ask follow-up questions | Conversational AI search experience |
>                      - | P2 | Response caching for repeated queries | Latency optimization for production |
>                      - | P3 | Answer quality evaluation (ROUGE score vs. source) | Automated quality measurement |
>                     
>                      - ---
>
> ## 📁 Project Structure
>
> ```
> AskAnything/
> ├── main.py              # Streamlit app — retrieval, summarization, citation pipeline
> ├── requirements.txt     # Python dependencies
> └── README.md            # This file
> ```
>
> ---
>
> ## 🔗 Related Projects in This Portfolio
> - [**FeedbackSense**](https://github.com/Poojaahegde/FeedbackSense-AI-Product-Feedback-Analyzer) — AI-powered user feedback clustering and sentiment analyzer
> - - [**PriorityLens**](https://github.com/Poojaahegde/prioritylens) — AI feature prioritization engine with bias detection
>  
>   - ---
>
> *Built as part of an AI PM portfolio — demonstrating understanding of RAG architecture, the foundation of modern AI search products.*
