import os

from src.application.app import create_app

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
