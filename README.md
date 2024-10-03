# Compact RAG

(Work in progress)

## Background

In the past six months, I've built many LLM applications. In conclusion, I want a compact RAG rather than a compact LLM.

From my experience, when it comes to RAG, I couldn't get the expected responses unless I used OpenAI's GPT-4o or GPT-4o-mini. A larger LLM is necessary, rather than a compact one.

For most cases, unless you're dealing with service providers or large enterprises, processing data within 10,000 records is sufficient for RAG. [SQLite](https://www.sqlite.org/) is enough for the database.

And a simple database that can perform similarity search is sufficient. I tried [sqlite-vec](https://github.com/asg017/sqlite-vec), and for the use cases I typically handle, sqlite-vec provided enough performance.

## Goal of this project

- Develop a compact RAG that can run on my Raspberry Pi 3 Model B.
- Work with various devices via RaspberryPi (and possibly, via a MCU).
- The RAG will support Hybrid RAG: SQL DB, Vector DB and Graph DB.
- The RAG will also work as an API server for my other project: https://github.com/araobp/virtual-showroom

## Architecture

```
           Brain
    [OpenAI API service]
             |
             |
        Compact RAG
       [RaspberryPi]---+---USB---[Camera]
             |         |
         SQLite DB     +---USB---[Speaker]
                       |
                       +---USB---[Mic]
                       |
                       +---USB---[Keyboard/Mouse]
                       |
                       +---USB Serial---[Other sensors/actuators]

```

## Compiling sqlite-vec on Rapsberry Pi

```
$ git clone https://github.com/asg017/sqlite-vec
$ cd sqlite-vec
$ sudo apt-get install libsqlite3-dev
$ make all
```

Find "vec0.so" in ./dist directory.

## Test script

### [test_vector_db.py](./test/test_vector_db.py)

```
xxxx@raspberrypi:~/compact-rag/test $ python test.py 
how are you?
[(1, 0.0), (0, 0.9725450277328491), (2, 1.0223934650421143)]
```

### [test_chat.py](./test/test_chat.py)

```
xxxx@raspberrypi:~/compact-rag/test $ python test_chat.py 
Einstein's theory of relativity comprises two parts: special relativity and general relativity. Special relativity posits that the laws of physics are the same for all observers, leading to the famous equation E=mc², linking mass and energy. General relativity describes gravity as the curvature of spacetime caused by mass.
--- Streaming ---
Einstein's theory of relativity consists of two parts: special relativity and general relativity. Special relativity, introduced in 1905, focuses on the physics of objects moving at constant speeds, particularly those close to the speed of light. It introduces the concepts of time dilation (time passes slower for fast-moving objects) and length contraction (objects appear shorter in the direction of motion). The famous equation \(E=mc^2\) illustrates the equivalence of mass and energy.

General relativity, published in 1915, expands this framework to include gravity, describing it as the curvature of spacetime caused by mass. Massive objects like planets and stars warp the spacetime around them, causing other objects to follow curved paths, which we perceive as gravitational attraction. Together, these theories revolutionized our understanding of space, time, and gravity.
```

## References

- [HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction](https://arxiv.org/html/2408.04948v1)
- [Bach Network](https://github.com/araobp/bach-network)
