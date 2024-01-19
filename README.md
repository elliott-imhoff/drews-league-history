# drews-league-history

``drews_league``: Codebase for compiling fantasy football historical data for Drew's League.

## Installation 

1) [Set up SSH](https://github.com/SenteraLLC/install-instructions/blob/master/ssh_setup.md)
2) Install [pyenv](https://github.com/SenteraLLC/install-instructions/blob/master/pyenv.md) and [poetry](https://python-poetry.org/docs/#installation)
3) Install package

        git clone git@github.com:SenteraLLC/drews-league-history.git
        cd drews-league-history
        pyenv install $(cat .python-version)
        poetry install
        
4) Set up ``pre-commit`` to ensure all commits to adhere to **black** and **PEP8** style conventions.

        poetry run pre-commit install
        
## Usage

Within the correct poetry/conda shell, run ``drews_league --help`` to view available CLI commands.
