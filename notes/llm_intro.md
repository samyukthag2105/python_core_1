# Intro to Large Language Models (LLMs)

## What is an LLM?

A Large Language Model (LLM) is an AI model trained on enormous amounts of text to predict the next token in a sequence. By repeatedly predicting the next token, it can answer questions, summarize text, translate languages, write code, and perform many other language tasks.

---

## Model vs Program

### Traditional Program

A traditional program follows instructions written by a programmer.

Example:

If user enters 5
    print("Hello")

The programmer writes every rule.

---

### Large Language Model

An LLM does not contain hard-coded rules for every question.

Instead, it learns patterns from billions of words during training and uses those learned patterns to generate responses.

---

## Training vs Inference

### Training

Training is when the model learns from huge datasets.

This process takes:

- Massive datasets
- Powerful GPUs
- Weeks or months
- Millions of dollars for the largest models

Training happens only occasionally.

---

### Inference

Inference is what happens when you use ChatGPT.

You ask:

"Explain RAG."

The already-trained model generates an answer.

Training teaches the model.

Inference uses the model.

---

## Tokens

LLMs do not read words.

They read tokens.

Examples:

"ChatGPT is amazing."

might become

["Chat", "G", "PT", " is", " amazing", "."]

Everything becomes tokens.

---

## Parameters

Parameters are the numbers the model learns during training.

Think of them as the model's memory.

More parameters generally allow the model to learn more complex patterns.

Examples:

- 1 Billion parameters
- 7 Billion parameters
- 70 Billion parameters
- Hundreds of billions of parameters

---

## Why Scale Matters

More data

+

More parameters

+

More compute

↓

Better language understanding

Better reasoning

Better coding ability

Better general performance

This is why modern AI models have become so capable.

---

## Three-Sentence Summary

A Large Language Model is an AI system trained to predict the next token in a sequence of text.

Unlike a traditional computer program that follows explicitly written rules, an LLM learns statistical patterns from enormous datasets during training.

When we chat with an LLM, we are performing inference—the model uses what it learned during training to generate a response.