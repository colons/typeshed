from typing import Any

rootlogger: Any

def class_logger(cls): ...

class Identified:
    logging_name: Any

class InstanceLogger:
    echo: Any
    logger: Any
    def __init__(self, echo, name) -> None: ...
    def debug(self, msg, *args, **kwargs) -> None: ...
    def info(self, msg, *args, **kwargs) -> None: ...
    def warning(self, msg, *args, **kwargs) -> None: ...
    warn: Any
    def error(self, msg, *args, **kwargs) -> None: ...
    def exception(self, msg, *args, **kwargs) -> None: ...
    def critical(self, msg, *args, **kwargs) -> None: ...
    def log(self, level, msg, *args, **kwargs) -> None: ...
    def isEnabledFor(self, level): ...
    def getEffectiveLevel(self): ...

def instance_logger(instance, echoflag: Any | None = ...) -> None: ...

class echo_property:
    __doc__: str
    def __get__(self, instance, owner): ...
    def __set__(self, instance, value) -> None: ...
