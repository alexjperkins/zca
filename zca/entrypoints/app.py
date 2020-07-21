import os
from pathlib import Path
from typing import Optional

from flask import Flask, jsonify


_VERSION = "0.0.1"
_API_ROOT = "api/v1"
_PROJECT_ROOT = Path(__file__).parent


def create_app(*, environment: Optional[str] = None):
    app = Flask(__name__)
    environment = environment or os.environ.get("ZCA_ENVIRONMENT", "local")

    @app.route("/version", methods=["GET"])
    def version():
        return jsonify({
            "version": _VERSION,
        }), 200

    return app
