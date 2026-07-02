# Transformer Notes

## What is a Transformer?

A Transformer is a neural network architecture introduced in 2017 that processes text using self-attention instead of reading words one by one.

It is the architecture behind modern LLMs such as ChatGPT, Gemini, Claude, and Llama.

---

## Why was it revolutionary?

Before Transformers:

- RNNs processed words one at a time.
- Long sentences were difficult to remember.
- Training was slow.

Transformers:

- Process all tokens in parallel.
- Understand long-range relationships.
- Train much faster on GPUs.

---

## What is Self-Attention?

Self-attention allows every word (or token) to look at every other word in the sentence and decide which ones are important for understanding its meaning.

Example:

"The animal didn't cross the street because it was tired."

The word **"it"** attends to **"animal"**, not **"street"**.

---

## Why is Self-Attention Useful?

It helps the model understand:

- Context
- Relationships
- Pronouns
- Long sentences
- Meaning

instead of treating every word independently.

---

## Encoder

The encoder reads the input and creates meaningful representations.

---

## Decoder

The decoder generates the output one token at a time.

ChatGPT mainly uses the decoder part of the Transformer architecture.

---

## Multi-Head Attention

Instead of looking at only one relationship, the model uses multiple attention heads.

Different heads can learn different kinds of relationships.

For example:

- Grammar
- Meaning
- Subject-verb agreement
- Names
- Locations

---

## Why Transformers Changed AI

Transformers made it possible to train much larger language models efficiently.

This led to:

- BERT
- GPT
- T5
- Llama
- Gemini
- Claude

and many other modern AI systems.

---

## One-Sentence Explanation of Self-Attention

Self-attention lets every word look at every other word in a sentence so the model can understand which words are most important for the current word.
