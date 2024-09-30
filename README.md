# Compact RAG

(Work in progress)

## Background

In the past six months, I've built many LLM applications. In conclusion, I want a compact RAG rather than a compact LLM.

From my experience, when it comes to RAG, I couldn't get the expected responses unless I used OpenAI's GPT-4o or GPT-4o-mini. A larger LLM is necessary, rather than a compact one.

For most cases, unless you're dealing with service providers or large enterprises, processing data within 10,000 records is sufficient for RAG. SQLite is enough for the database.

Even in RAG, complex academic processing isn't needed. What's important is the data model and the prompts you input into the RAG.

There's no need for LangChain. It's smoother to directly work with APIs like those provided by OpenAI. Development, debugging, and code maintenance are easier this way.

A vector DB with complex dependencies like ChromaDB isn't necessary. A simple database that can perform similarity search is sufficient. I tried [sqlite-vec](https://github.com/asg017/sqlite-vec), and for the use cases I typically handle, sqlite-vec provided enough performance.

## Goal of this project

Develop a compact RAG that can run on my Raspberry Pi 3.

This RAG will also work as an API server for my other project: https://github.com/araobp/virtual-showroom
