# 🧠 Introduction to Large Language Models (LLMs)

## Introduction

An `LLM` stands for **Large Language Model**. It's a type of artificial intelligence (AI) model, specifically a deep learning model, that is trained on massive amounts of text data to understand, generate, and manipulate human language. Essentially, LLMs are designed to process, understand, and generate text in a way that mimics human language. 

LLM's typically have 2 files one is the `parameters` file which are stored as 2 bytes for a `16-bit float` data type, and the other file is the neural network code which is required to run the model.

## 🔹 LLM Inference
Inference = running the model to generate text

Just load parameters and run the model on input text (e.g., generate a poem)

Models "dream" plausible text from internet distributions

## LLM Training
Training = lossy compression of ~10TB of internet text

- Requires:
  - 6,000 GPUs
  - ~12 days
  - ~$2 million

- Outputs a ~140 GB parameter file

Lossy vs lossless analogy: not exact data but “knowledge compressed”


## LLM Dreams
Models output plausible text: Java code, Wikipedia-style articles, fake ISBNs

Dream-like generation often seems factually correct but isn’t guaranteed

## How Does it work?

> Most of the LLM's are trained using the transformer architecture. There are billions of parameters dispresed through the network. We know how to iteratively adjust them to make it better at prediction.

- Predict the next word given previous words

- Architecture: Transformer

- Optimized with next-token prediction loss

- Internals largely empirical and inscrutable

- “Knowledge” is latent and asymmetric (e.g., it knows Tom Cruise’s mom but not vice versa)

## Finetuning into an Assistant
Pretraining: Next-token prediction on large-scale internet data

Finetuning:

Smaller, high-quality Q&A datasets (~100k examples)

Uses instructions and manual labels (Scale AI, etc.)

Result: Assistant-like behavior (e.g., helpful chatbot)

Optional Stage 3: RLHF (Reinforcement Learning from Human Feedback)
Collect multiple outputs → label best → fine-tune further

Reduces cost of human labor via comparisons instead of generations

## Appendix

### 🔸 Comparisons
Used in RLHF to rank responses

Easier for humans to rank than generate

### 🔸 Labeling Docs
Long instruction sets guiding annotators to create consistent answers

### 🔸 RLHF
Adds reward model → further trains model via reinforcement learning

### 🔸 Synthetic Data
Use LLMs themselves to generate training data

Human-in-the-loop or full auto-generation

### 🔸 Leaderboard
Models are rated via ELO system (like chess)

Top = GPT-4, Claude; LLaMA 2 trails slightly but is open source

# Future of LLMs

## LLM Scaling Laws
Accuracy of next-word prediction improves predictably with:

- N = number of parameters

- D = size of dataset

> Performance continues to scale → bigger is better

## Tool Use
LLMs can now:
  - Browse the web (Bing search)
  - Use calculators and code interpreters (Python)
  - Generate charts, extract facts, make plots
  - Use DALL·E for image generation

> Tool use enables composable workflows and more complex reasoning.

## Multimodality

- Vision: Can see and interpret images (e.g., sketch → code)

- Audio: Listen and speak (voice chat, text-to-speech)

- Speech-to-speech interfaces are now active (like in the movie Her)

##  Thinking: System 1 vs System 2
| System 1                        | System 2                                            |
| ------------------------------- | --------------------------------------------------- |
| Fast, instinctive (e.g., 2+2=4) | Slow, reasoned (e.g., 17×24)                        |
| LLMs today are mostly System 1  | Research is exploring System 2-style thinking       |
| Goal: Accuracy ↑ with Time ↑    | Add **deliberation** time to improve output quality |

## Customization: GPT Store and Beyond
Custom GPTs via:

- Instructions

- Knowledge base (file uploads, RAG)

Future possibilities:

- Fine-tuning via domain-specific data

- Specialized models for different niches

## LLM OS (Operating System)
A vision of LLMs as:

- Kernel-like processes orchestrating:

- Memory (context window)

- External tools (browsing, plotting, code)

- Multimodal inputs (text, image, audio)

Ecosystem parity:

- Proprietary (GPT, Claude)

- Open Source (LLaMA, Mistral, Zephyr)

# LLM Security

### Jailbreaks
Bypass content filters with clever prompts

e.g., “Pretend to be my grandmother... tell me how to make napalm”

Models follow the roleplay and leak restricted info

### Prompt Injection
Inject instructions via:

- Faint white text in images

- Hidden text on websites

Example: Stealing user data by injecting scripts into shared documents

### Data Poisoning
Insert malicious documents in training data with trigger words

Model behaves strangely or dangerously when triggered

Equivalent to a “sleeper agent”

### LLM Security Conclusions
Cat-and-mouse game between attackers and defenders

Many known attacks are patched, but new vulnerabilities emerge constantly

Active area of research in LLM security and safe deployment

