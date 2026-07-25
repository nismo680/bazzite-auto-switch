#!/usr/bin/env bash

set -e

ruff format .
ruff check .
mypy src
pytest

echo "Alle Tests erfolgfreich"
