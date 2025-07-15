PORT ?= 8000

install:
    uv venv -p 3.13
    source .venv/bin/activate && uv sync

dev:
    source .venv/bin/activate && uv run flask --debug --app page_analyzer:app run

start:
    source .venv/bin/activate && uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build:
    ./build.sh

render-start:
    gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

