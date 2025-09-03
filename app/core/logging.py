import logging
import sys

def configure_logging(level=logging.INFO):
    """Configure logging for the application."""

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        )
    )

    logging.basicConfig(
        level=level,
        handlers=[handler],
        force=True,
    )

    logging.getLogger().info("Logging is configured.")