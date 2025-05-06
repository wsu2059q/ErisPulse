from ErisPulse import sdk, logger
import asyncio

def main():
    sdk.logger.info("默认日志")
    sdk.init()
    sdk.logger.info("日志模块")

if __name__ == "__main__":
    main()