### Tests and linter status:

[![Maintainability](https://api.codeclimate.com/v1/badges/8dbf515e6079dcb5e358/maintainability)](https://codeclimate.com/github/emp7yhead/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8dbf515e6079dcb5e358/test_coverage)](https://codeclimate.com/github/emp7yhead/python-project-lvl3/test_coverage)
[![CI](https://github.com/emp7yhead/python-project-lvl3/actions/workflows/CI.yml/badge.svg)](https://github.com/emp7yhead/python-project-lvl3/actions/workflows/CI.yml)

# page-loader

## Description

Cli utility for asynchronous downloading of web-pages to a local directory.

## Dependencies

- python = "^3.9"
- httpx = "^0.24.0"
- beautifulsoup4 = "^4.10.0"
- progress = "^1.6"

## Usage

```bash
usage: page-loader [options] <url>

Downloading web-page to local directory

positional arguments:
  url                   url to download

optional arguments:
  -o, --output          output dir (default: current working directory)

  -v, --version         show program's version number and exit
  -h, --help            dispaly help for command
```

## Installation

Use the package manager pip:

```bash
pip install --user git+https://github.com/emp7yhead/python-project-lvl3
```

### Or

Clone repository and use poetry:

```bash
git clone https://github.com/emp7yhead/python-project-lvl3
cd python-project-lvl3
make build
make package-install
```

### Work process

[![asciicast](https://asciinema.org/a/kbl4O04t9yU4w7iO0jWlvHYGs.svg)](https://asciinema.org/a/kbl4O04t9yU4w7iO0jWlvHYGs)
