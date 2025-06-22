# 🧠 Gen-AI Foundations

**Gen-AI Foundations** module — a beginner-friendly deep dive into the fundamental building blocks of modern Generative AI.

---

## 📚 Notebooks Included

| Notebook | Description |
|---------|-------------|
| [`01-attention.ipynb`](./01-attention.ipynb) | Understand the core attention mechanism with examples and self-attention math |
| [`02-transformer-architecture.ipynb`](./02-transformer-architecture.ipynb) | Explore the full Transformer model: layers, multi-head attention, and positional encoding |
| [`03-tokenization.ipynb`](./03-tokenization.ipynb) | Learn how text is turned into numbers using tokenization strategies like WordPiece and BPE |
| [`04-training.ipynb`](./04-training.ipynb) | Covers pretraining (MLM, CLM) and task-specific fine-tuning pipelines |
| [`05-inference.ipynb`](./05-inference.ipynb) | Discover decoding techniques like greedy, top-k, top-p sampling, and temperature |
| [`06-optimizations.ipynb`](./06-optimizations.ipynb) | Review limitations and learn about performance boosts: FlashAttention, LoRA, Quantization |

---

## 🚀 How to Use

1. Clone the repo or download this folder
2. Open each `.ipynb` notebook in Jupyter or VS Code
3. Follow the notes and run the cells to learn by doing

```bash
jupyter notebook 01-attention.ipynb
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
