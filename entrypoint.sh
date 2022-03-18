#!/bin/bash
python create_tables.py
python load_fixtures.py
exec "$@"