# 🧠 MULTIMODAL: Vision + Language AI

This module explores **Multimodal AI**, where models process and reason over multiple data types — primarily **images and text**.

---

## 📚 Contents

| File/Notebook | Description |
|---------------|-------------|
| `01-intro-to-multimodal.ipynb` | Overview of multimodal learning, use cases, and popular models (e.g., CLIP, BLIP) |
| `02-multimodal-embeddings.ipynb` | Extract and visualize joint embeddings for text and images |
| `03-multimodal-rag.ipynb` | Perform Retrieval-Augmented Generation using image + text embeddings |
| `04-fine-tuning-multimodal-embeddings.md` | Guide to fine-tuning or adapting vision-language models for specific tasks |
| `functions.py` | Utility functions used across notebooks (e.g., embedding, visualization) |
| `requirements.txt` | Python dependencies for this module |

---

## 📂 Folders

- `images/`: Sample images for inference or training
- `data/`: Any auxiliary datasets or `.json`/`.csv` files
- `assets/`: Markdown images

---

## 🚀 Setup

Install required packages:

```bash
pip install -r requirements.txt
```

---

## ✅ Goals

- Understand how text and images can be represented in a shared space
- Perform image-text retrieval using sentence-transformers, CLIP, etc.
- Build and evaluate a Multimodal RAG pipeline
- Learn how to adapt/fine-tune multimodal models for domain-specific tasks

---

## 📦 Example Libraries Used

- `transformers`, `sentence-transformers`, `torchvision`, `CLIP`, `gradio`

> **Reference**:  
>
> Talebi, S. *YouTube-Blog*. GitHub, 2025. [https://github.com/ShawhinT/YouTube-Blog](https://github.com/ShawhinT/YouTube-Blog)
