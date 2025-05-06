import logging
import sys
import inspect
from rich.logging import RichHandler

class MyLogger:
    def __init__(self, sdk, name="ErisPulse"):
        self.logger = logging.getLogger(name)
        self.sdk = sdk
        self.log_level = sdk.env.get("LOG_LEVEL", "DEBUG")
        self.logger.setLevel(self.log_level)
        self.sdk.logger = self.logger
        
        if not self.logger.handlers:
            handler = RichHandler(
                show_time=True,                         # 显示时间
                show_level=True,                        # 显示日志级别
                show_path=False,                        # 不显示调用路径
                markup=True,                            # 支持 Markdown
                log_time_format="[%y-%m-%d/%H:%M:%S]",  # 自定义时间格式
                rich_tracebacks=True,                   # 支持更美观的异常堆栈
            )
            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _get_caller(self):
        frame = inspect.currentframe().f_back.f_back
        module = inspect.getmodule(frame)
        module_name = module.__name__
        if module_name == "__main__":
            module_name = "Main"
        if module_name.endswith(".Core"):
            module_name = module_name[:-5]
        return module_name

    def info(self, message, *args, **kwargs):
        caller = self._get_caller()
        self.logger.info(f"[{caller}] {message}", *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        caller = self._get_caller()
        self.logger.warning(f"[{caller}] {message}", *args, **kwargs)

    def error(self, message, *args, **kwargs):
        caller = self._get_caller()
        self.logger.error(f"[{caller}] {message}", *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        caller = self._get_caller()
        self.logger.debug(f"[{caller}] {message}", *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        caller = self._get_caller()
        self.logger.critical(f"[{caller}] {message}", *args, **kwargs)