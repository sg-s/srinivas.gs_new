if ! poetry check --lock; then
    poetry lock
fi
poetry install