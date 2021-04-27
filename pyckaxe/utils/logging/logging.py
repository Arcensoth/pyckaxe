import logging
from logging import Logger
from typing import Dict, Optional, Union

# Use colorlog/colorama as an optional dependency for prettier logs.
# NOTE Colours may not work on Git Bash: https://github.com/tartley/colorama/pull/226
try:
    import colorlog
except:
    pass


__all__ = (
    "Logger",
    "LOG_LEVELS",
    "setup_logging",
    "get_logger",
)


LOG_LEVELS = (
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
)

LOG_FORMAT_BASIC = "%(log_color)s%(message)s"
LOG_FORMAT_DETAILED = "%(log_color)s%(asctime)s %(levelname)-8s [%(name)s] %(message)s"

LOG_COLORS = {
    LOG_LEVELS[0]: "cyan",
    LOG_LEVELS[1]: "green",
    LOG_LEVELS[2]: "yellow",
    LOG_LEVELS[3]: "red",
    LOG_LEVELS[4]: "red,bg_white",
}


def setup_logging(
    level: Union[int, str] = logging.WARNING,
    detailed: bool = False,
    log_format: Optional[str] = None,
    log_colors: Dict[str, str] = LOG_COLORS,
):
    log_format = log_format or (LOG_FORMAT_DETAILED if detailed else LOG_FORMAT_BASIC)
    log_handler = logging.StreamHandler()

    try:
        formatter = colorlog.ColoredFormatter(fmt=log_format, log_colors=log_colors)
        log_handler.setFormatter(formatter)
    except:
        print(
            "Terminal colors (via colorama and/or colorlog) are unavailable; using basic logging instead."
        )

    logging.basicConfig(level=level, handlers=[log_handler])


def get_logger(name: str) -> Logger:
    return logging.getLogger(name)
