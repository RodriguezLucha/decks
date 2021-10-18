#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

PGPASSWORD=password psql -h localhost -U postgres --port 5432 --dbname=deck --file=$SCRIPT_DIR/../deck.sql
