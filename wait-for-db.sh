#!/bin/sh
set -e

host="$1"
shift
cmd="$@"

echo "⏳ Waiting for database at $host..."

until pg_isready -h "$host" -U "postgres"; do
  sleep 1
done

sleep 2  # give DB a couple extra seconds

echo "✅ Database ready, starting app..."
exec $cmd
