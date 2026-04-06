# 🎥 Video RAG System

An end-to-end **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about lecture videos and get **precise answers with timestamps and video references**.

---

## 🚀 Overview

This project processes video content and builds a semantic search system over transcriptions.  
Given a user query, it retrieves the most relevant video segments and uses an LLM to generate a grounded, context-aware answer.

👉 Example:
> *“Transformers are explained in Video 2 between 120s–300s, covering attention mechanisms and architecture.”*

---

## ✨ Features

- 🎬 **Video → Audio Pipeline** using `ffmpeg`
- 🗣️ **Speech-to-Text** using OpenAI Whisper
- 🧠 **Dense Vector Embeddings** via BGE-M3 (local embedding API)
- 🔍 **Similarity Search** using cosine similarity
- 🤖 **LLM Generation** (LLaMA3 via local API)
- ⏱️ **Timestamp Grounding** for precise navigation
- ⚡ **Auto Embedding Build** if not already created

---

## ⚡ Quick Start

```bash
# 1. Add videos
data/videos/

# 2. Convert videos to audio
python src/ingestion/video_to_audio.py

# 3. Transcribe audio
python src/processing/transcribe.py

# 4. Run RAG system
python main.py

video-rag-system/
├── data/
│   ├── videos/
│   ├── audios/
│   ├── transcripts/
│   └── embeddings.joblib
│
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── embeddings/
│   ├── retrieval/
│   ├── generation/
│   └── utils/
│
├── main.py
├── requirements.txt
└── README.md