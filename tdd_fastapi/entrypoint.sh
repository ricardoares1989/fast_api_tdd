#!/bin/sh

echo "Waiting for postgres..."

# nc -z nos permite evaluar
# si existe una red que responda,
# -z observa si hay daemons abiertos en TCP/UDP
while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostgresSQL started"

exec "$@"