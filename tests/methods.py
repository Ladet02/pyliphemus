import asyncio
from loguru import logger

from pylyphemus.api import PyLiphemAPI

smm_service = PyLiphemAPI(token="")
token = ""


async def test_service_list():
    result = await smm_service.service_list()
    logger.debug(result)


async def test_check_balance():
    result = await smm_service.check_balance(token=token)
    logger.debug(result)


async def test_order_list():
    result = await smm_service.order_list(token=token)
    logger.debug(result)


async def test_referral_list():
    result = await smm_service.referreal_list(token=token)
    logger.debug(result)


async def main():
    logger.info("PRIMARY TESTS")
    await test_service_list()
    await test_check_balance()
    await test_order_list()
    await test_referral_list()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
