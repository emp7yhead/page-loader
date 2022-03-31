### Hexlet tests and linter status:
[![Actions Status](https://github.com/emp7yhead/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/emp7yhead/python-project-lvl3/actions) 
[![Maintainability](https://api.codeclimate.com/v1/badges/8dbf515e6079dcb5e358/maintainability)](https://codeclimate.com/github/emp7yhead/python-project-lvl3/maintainability) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/8dbf515e6079dcb5e358/test_coverage)](https://codeclimate.com/github/emp7yhead/python-project-lvl3/test_coverage) 
[![CI](https://github.com/emp7yhead/python-project-lvl3/actions/workflows/CI.yml/badge.svg)](https://github.com/emp7yhead/python-project-lvl3/actions/workflows/CI.yml) 
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# page-loader
## Description:
CLI utilite for downloading web-pages to existing local directory.
## Dependencies:
- python = "^3.9"
- requests = "^2.27.1"
- beautifulsoup4 = "^4.10.0"
- progress = "^1.6"

## Usage:
```
usage: page-loader [options] <url>

Downloading web-page to local directory

positional arguments:
  url                   url to download

optional arguments:
  -o, --output          output dir (default: current working directory)

  -v, --version         show program's version number and exit
  -h, --help            dispaly help for command
```
## Installation:
Use the package manager pip:
```
pip install --user git+https://github.com/emp7yhead/python-project-lvl3
```
### Or
Clone repository and use poetry:
```
git clone https://github.com/emp7yhead/python-project-lvl3
cd python-project-lvl3
make build
make package-install
```

### Work process:
[![asciicast](https://asciinema.org/a/kbl4O04t9yU4w7iO0jWlvHYGs.svg)](https://asciinema.org/a/kbl4O04t9yU4w7iO0jWlvHYGs)