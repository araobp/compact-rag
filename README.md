# Compact RAG

(Work in progress)

## Background

In the past six months, I've built many LLM applications. In conclusion, I want a compact RAG rather than a compact LLM.

From my experience, when it comes to RAG, I couldn't get the expected responses unless I used OpenAI's GPT-4o or GPT-4o-mini. A larger LLM is necessary, rather than a compact one.

For most cases, unless you're dealing with service providers or large enterprises, processing data within 10,000 records is sufficient for RAG. [SQLite](https://www.sqlite.org/) is enough for the database.

And a simple database that can perform similarity search is sufficient. I tried [sqlite-vec](https://github.com/asg017/sqlite-vec), and for the use cases I typically handle, sqlite-vec provided enough performance.

## Goal of this project

Develop a compact RAG that can run on my Raspberry Pi 3 Model B.

This RAG will also work as an API server for my other project: https://github.com/araobp/virtual-showroom

## Compiling sqlite-vec for Rapsberry Pi

```
$ git clone https://github.com/asg017/sqlite-vec
$ cd sqlite-vec
$ sudo apt-get install libsqlite3-dev
$ make all
```

Find "vec0.so" in ./dist directory.

## Test script

