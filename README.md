# Simple Flask Web Server

The simplest possible Flask web server: it serves a static site (e.g. a Webpack build's output) from a `static/` folder, with routes for the index page, a favicon, and an `iframe.html` page.

## Tech Stack

- Python
- [Flask](https://flask.palletsprojects.com/) 1.1.2

## Prerequisites

- Python 3 (a version compatible with Flask 1.1.2, e.g. Python 3.6–3.8)
- pip

## Installation

```bash
git clone https://github.com/er-shrey/simple-flask-web-server.git
cd simple-flask-web-server

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Running the server

```bash
python server.py -p <port number>
```

If `-p`/`--port` is omitted, the server defaults to port `9999` and binds to `0.0.0.0`. Once running, visit `http://localhost:<port>/` in your browser.

## Project structure

- `server.py` — Flask app; serves `static/index.html` at `/`, `favicon.ico`, and `static/iframe.html` at `/iframe.html`
- `static/` — static site content (e.g. a Webpack build output) served by the app
