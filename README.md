# Compact RAG

<img src="./docs/my_raspberry_pi.jpg" width=400>

## Background

I develop a compact RAG (Retrieval-Augmented Generation) that runs on Raspberry Pi. As the database for RAG, I adopt SQLite and implement a vector DB using [sqlite-vec](https://github.com/asg017/sqlite-vec).

## Goal of this project

- Develop a compact RAG that runs on Raspberry Pi, supporting Hybrid RAG: SQL DB and Vector DB.
- The RAG also works as an API server for my other projects: [virtual-showroom](https://github.com/araobp/virtual-showroom).

## Requrements

- OpenAI API key
- LLM model: gpt-4o-mini
- Embeddings model: text-embedding-3-small
- Raspberry Pi

## Architecture

```
                                   Brain
                           [OpenAI API service]
Unity app                            |
[VirtualShowroom]-----+              |
                      |              |
Web apps              |        Compact RAG (app.py)
[Web Browser]---------+------- [Raspberry Pi]---+---USB---[Camera with mic]
                      |              |          |
GenAI                 |          SQLite DB      +---USB---[Speaker]
[Node-RED]------------+
```

## Compiling sqlite-vec on Rapsberry Pi

```
$ git clone https://github.com/asg017/sqlite-vec
$ cd sqlite-vec
$ sudo apt-get install libsqlite3-dev
$ make loadable 
```

Find "vec0.so" in ./dist directory.

## Reference documents, chunking and embeddings for RAG

### Document sources

- [Travel guidebooks](./ref/virtual_showroom) for [virtual-showroom](https://github.com/araobp/virtual-showroom).

### Chunking and Embeddings

- [Step 1. Generating Chunks](./ref/Chunks.ipynb): I run this notebook on my Mac.
- [Step 2. Calculating embeddings](./ref/calc_embeddings.py): I run this script on my Raspberry Pi 3.

## Implementations

- [cx package](./cx) ... Python package
- [API server](./app) ... API Server

<img src="docs/api_server.jpg" width=700>

## Partition keys and auxiliary columns supported by sqlite-vec

I use partition keys and auxiliary columns for filtering records on the database in this project:

```
CREATE VIRTUAL TABLE virtual_showroom
USING vec0(
context text partition key,
embedding float[1536],
+chunk text
)
```

Reference: https://alexgarcia.xyz/sqlite-vec/features/vec0.html

### Unit tests

- [Unit tests for "cx" package](./unittest/cx)
- [Unit test for the API server](./unittest/api)

### Running the API server

```
$ cd app
$ python app.py
```

The API server provides simple web apps. Access "http://\<IP address of the API server\>:5050" with a web browser.

[virtual-showroom](https://github.com/araobp/virtual-showroom) uses this API server to access the OpenAI API service.

#### Starting the API server automatically

Refer to [this article](https://ponnala.medium.com/never-let-your-python-http-server-die-step-by-step-guide-to-auto-start-on-boot-and-crash-recovery-1f7b0f94401e) to start the server automatically.

A sample service file is like this:

```
[Unit]
Description=Python Generative AI API server
After=network.target

[Service]
ExecStart=/usr/bin/python3 -m app --directory <Path to "app" folder>
WorkingDirectory=<Path to "app" folder>
Restart=always
RestartSec=10
User=<Your user name>
Group=users
Environment=PYTHONPATH=<Path to this repo on Raspberry Pi>:$PYTHONPATH OPENAI_API_KEY=<OpenAI API key>

[Install]
WantedBy=multi-user.target
```

After having created the service file, do this:

```
$ sudo systemctl daemon-reload
$ sudo systemctl start gen_ai.service
```

Confirm the daemon process running:

```
$ sudo systemctl start gen_ai.service
```

If something wrong happened, check the syslog:
```
$ tail /var/log/syslog
```

## Extra: Some experiments with gpt-4o-mini

- [Character Profiling](./CHARACTER_PROFILING.md)
- [Hand Gesture Recognition](./HAND_GESTURE_RECOGNITION.md)

