
# How to
## PokeAPI
To use this app you need the PokeAPI https://github.com/PokeAPI/pokeapi
We recommend you to clone the PokeAPI repo and follow the instructions to start a local instance of the API instead of using the public one at https://pokeapi.co/:

1) https://github.com/PokeAPI/pokeapi#setup-
2) https://github.com/PokeAPI/pokeapi#v2-database-setup

-- OR (if you use Docker) --

https://github.com/PokeAPI/pokeapi#docker

If you wish to use the public one nonetheless, you need to specify the API URL at the beginning of constants.py:

```python
API_PATH = "https://pokeapi.co/api/v2/" # Or any other URL serving the PokeAPI
```

After doing that you can start using the Pokestats CLI project:

## Pokestats CLI

After cloning this repo wherever you want on your computer:

First, you'll need the newest version of Python 3: https://www.python.org/downloads/

*N.B.: All the following commands are to be ran from the root directory of the project: pokestats/ if you cloned the repo without specifying a custom target directory.*

You might want to create a virtual env before installing required packages: https://virtualenv.pypa.io/en/stable/

```bash
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
```

Install the required packages with pip: https://pip.pypa.io/en/stable/installing/

```bash
$ pip install -r requirements.txt
```

Run tests:

```bash
$ python -m unittest discover tests *_test.py
```

Finally, you can use the tool.
Example:

```bash
$ python pokestats.py Pikachu
```
