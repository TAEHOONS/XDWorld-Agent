import logging
import sys

from app.core.config import get_settings


def setup_logging() -> logging.Logger:
    settings = get_settings()
    level = getattr(logging, settings.log_level.upper(), logging.INFO)

    # gunicorn 멀티워커 환경에서 어느 워커가 찍은 로그인지 식별 가능하도록 PID 포함
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | pid=%(process)d | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root = logging.getLogger("xdworld")
    root.setLevel(level)
    root.addHandler(handler)

    return root


logger = setup_logging()
