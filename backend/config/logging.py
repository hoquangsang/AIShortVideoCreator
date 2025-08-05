import logging
import sys
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from uvicorn.logging import DefaultFormatter
from datetime import datetime
from config.setting import settings


class AppLogger:
    def __init__(self):
        self.logger = logging.getLogger("app")
        self.logger.setLevel(self._get_log_level())
        self.logger.propagate = False

        if not self.logger.handlers:
            self._add_handlers()

    def _get_log_level(self) -> int:
        level_map = {
            "critical": logging.CRITICAL,
            "error": logging.ERROR,
            "warning": logging.WARNING,
            "info": logging.INFO,
            "debug": logging.DEBUG,
        }
        return level_map.get(settings.LOG_LEVEL.lower(), logging.INFO)

    def _add_handlers(self):
        self.logger.addHandler(self._create_file_handler())
        self.logger.addHandler(self._create_console_handler())

    def _create_file_handler(self):
        log_dir = Path(settings.LOG_DIR)
        if not log_dir.is_absolute():
            project_root = Path(__file__).resolve().parent.parent
            log_dir = project_root / log_dir
        log_dir.mkdir(parents=True, exist_ok=True)

        # Tạo file log theo ngày hiện tại
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = log_dir / f"{today}.log"

        handler = TimedRotatingFileHandler(
            filename=log_file,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8"
        )
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))
        return handler

    def _create_console_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG if settings.APP_ENV.lower() == "development" else self._get_log_level())
        handler.setFormatter(DefaultFormatter(fmt="%(levelprefix)s %(message)s", use_colors=True))
        return handler

    def __getattr__(self, name):
        return getattr(self.logger, name)


logger = AppLogger()
