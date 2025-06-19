# 🧠 Gen-AI Foundations

**Gen-AI Foundations** module — a beginner-friendly deep dive into the fundamental building blocks of modern Generative AI.

---

## 📚 Notebooks Included

| Notebook | Description |
|---------|-------------|
| `01_attention.ipynb` | Understand the core attention mechanism with examples and self-attention math |
| `02_transformer_architecture.ipynb` | Explore the full Transformer model: layers, multi-head attention, and positional encoding |
| `03_tokenization.ipynb` | Learn how text is turned into numbers using tokenization strategies like WordPiece and BPE |
| `04_training.ipynb` | Covers pretraining (MLM, CLM) and task-specific fine-tuning pipelines |
| `05_inference.ipynb` | Discover decoding techniques like greedy, top-k, top-p sampling, and temperature |
| `06_optimizations.ipynb` | Review limitations and learn about performance boosts: FlashAttention, LoRA, Quantization |

---

## 🚀 How to Use

1. Clone the repo or download this folder
2. Open each `.ipynb` notebook in Jupyter or VS Code
3. Follow the notes and run the cells to learn by doing

```bash
jupyter notebook 01_attention.ipynb
```

---

## 🔧 Requirements

Install the main dependencies:

```bash
pip install torch transformers
```

For optimizations:
```bash
pip install peft bitsandbytes optimum
```

---

## 🎯 Goal

- Explain how transformers work from scratch
- Tokenize and preprocess text
- Train and infer using prebuilt models
- Optimize model inference for deployment
