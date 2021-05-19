import asyncio
import random

from pyckaxe.utils.logging import get_logger


def preview_logging():
    log = get_logger("preview_logging")
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
    try:
        raise ValueError("don't worry this is a fake error")
    except:
        log.exception("exception")


async def preview_async_logging():
    async def do_debug():
        await asyncio.sleep(random.randint(500, 2000) / 1000)
        log.debug(f"debug")

    async def do_info():
        await asyncio.sleep(random.randint(500, 2000) / 1000)
        log.info(f"info")

    async def do_warning():
        await asyncio.sleep(random.randint(500, 2000) / 1000)
        log.warning(f"warning")

    async def do_error():
        await asyncio.sleep(random.randint(500, 2000) / 1000)
        log.error(f"error")

    async def do_critical():
        await asyncio.sleep(random.randint(500, 2000) / 1000)
        log.critical(f"critical")

    log = get_logger("preview_async_logging")
    awaitables = [
        do_debug(),
        do_info(),
        do_warning(),
        do_error(),
        do_critical(),
    ]
    await asyncio.gather(*awaitables)
