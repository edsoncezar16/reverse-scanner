# Reverse Scanner

A program that scans physical files with tables and generates an excel file with the data.

## Motivation

At the time of this writing, I had a girlfriend that worked as the focal of a reverse logistics operation.

Sometimes she would spend many hours at home doing some tasks, such as manually inserting data from physical files with tables into excel files.

This situation originated the idea of developing a program that automates such tasks so that she could spend more time with her children and me.

## How to run the application

### Setup

- Have a working instance of docker compose.

- Clone the repo.

- Put the images you want to scan into the `input images` folder.

- At the repo root, execute the command

```sh
   docker compose up -d [--build]
```

*Note: use the --build flag if you want to rebuild the scanner docker image.*

- After the containers are up and running, execute:

```sh
   docker compose exec -it scanner bash
```

This shoud open an interactive bash session where you can use the scanner according to the following instructions.

*Note: the scanner.sh script sets up environment variables before running the pipeline. You might want take a look at the default values or change them at your will.*

### Usage

```lua
   ./scanner.sh 
```

### Shutting down the containers

After you are done playing with the scanner, run

```sh
   docker compose down
```

to remove the containers.

## Perspectives

- Improve app efficiency with more generic images, not only cropped ones.

- Provide an API for a richer user experience and more customizable operating options.
