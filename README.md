# Compact RAG

(Work in progress)

## Background

In the past six months, I've built many LLM applications. In conclusion, I want a compact RAG rather than a compact LLM.

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

## Reference documents and chunk generation for RAG

=> [Reference Documents](./ref/README.md)

## RAG as an API server based on Flask

...

## Unit test

- [rag](./unittest/rag)
- [api](./unittest/api)

## References

- [HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction](https://arxiv.org/html/2408.04948v1)
- [Bach Network](https://github.com/araobp/bach-network)
