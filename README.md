# Trabajo Práctico Parseo y Generación de Código

- [Enunciado TP1](./docs/tp1.pdf)

- [Enunciado TP2](./docs/tp2.pdf)

Los tests se encuentran en la carpeta "./src/test":

- Tests TP1 en la carpeta "tests_parser_json".

- Tests TP2 en la carpeta "tests_interpreter".

## Pre-requirements

- python v3.11
- [PLY v3.11](https://github.com/dabeaz/ply)
- [Pytest v7.4.2](https://pypi.org/project/pytest/)
- [argparse](https://docs.python.org/3/library/argparse.html)

Note: If "py" not works use "python3" / "python".

## Docker

1) Go to repository root folder
2) Build image from Dockerfile with:

    ```bash
    docker build -t flecha .
    ```

3) Execute image as container with:

    ```bash
    docker run -it --entrypoint bash --name flecha flecha
    ```

4) Use commands in [Tests](#tests) or [Execute](#execute) sections (you might need to replace command "py" with "python3")


## Set up 


### From requirement.txt file

```bash
pip install -r requirements.txt
```

# Tests

```bash
py -m pytest -v
```

## Execute

### Help command
```bash
py ./src/main.py -h
```


### Enable REPL

Enables Read Evaluate Print Loop. _Note: disable all other flags_

```bash
py ./src/main.py -r
```

### Example with flag "-s" or "--stringProgram"
```bash
py ./src/main.py -s 12+234
```

### Example with flag "-i" or "--inputFile"
```bash
py ./src/main.py -i test/tests_parser_json/test18.input
```

### Show tokens with flags "-t" or "--tokenize"
```bash
py ./src/main.py -t -i test/tests_parser_json/test18.input
```

### Enable parser AST with flags "-p" or "--parse" 
```bash
py ./src/main.py -p -i test/tests_parser_json/test18.input
```

### Enable debug info (such as: Program Input) with flags "-d" or "--debug" 
```bash
py ./src/main.py -d -p -t -i test/tests_parser_json/test18.input
```
