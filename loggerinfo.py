import logging

loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]

for logger in loggers:
    print(f"[{logging.getLevelName(logger.level)}]{logger.name}")
