import os
from flask import Flask
from flask import Response, render_template, send_from_directory
import argparse

curr_dir_path = os.path.dirname(os.path.realpath(__file__))
curr_dir_path = curr_dir_path.split(os.sep)

curr_dir_path.append("static")
static_dir_path = os.sep.join(curr_dir_path)

app = Flask(__name__, template_folder=static_dir_path, static_folder=static_dir_path)

def parse_args() -> argparse.Namespace:
    """
    Parse the command line argument.

    Returns:
        argparse.Namespace: Contains the named argument parsed.
    """
    parser = argparse.ArgumentParser(description="SWBServer")
    parser.add_argument("-p", "--port", required=False, default=r"9999", type=int,
                        help="Port to run the service on.")
    return parser.parse_args()

# Parse the commandline arguments
args = parse_args()
port = args.port
localhost = "0.0.0.0"


@app.route('/', methods=["GET"])
def index() -> Response:
    """
    Serve Index.html

    Returns:
        Render build html file.
    """
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    """
    serving favicon
    """
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/iframe.html')
def iframe():
    """
    serving favicon
    """
    return render_template("iframe.html")

if __name__ == '__main__':
   app.run(host=localhost, port=port)