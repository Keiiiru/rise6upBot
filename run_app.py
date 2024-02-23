import logging

from aiohttp.web import run_app

from loader import app


def main():
    run_app(app, host="0.0.0.0", port=8081)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()

