#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

PGPASSWORD=password pg_dump -s deck \
    -h localhost \
    -U postgres \
    --port 5433 \
    -c \
    --clean \
    -s \
    -O \
    --if-exists \
    --file=$SCRIPT_DIR/../deck_export.sql
