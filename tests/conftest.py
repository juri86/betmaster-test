import pytest_asyncio

from playwright.async_api import async_playwright, BrowserContext, Browser

from core.settings import Env, settings


@pytest_asyncio.fixture(scope="function")
async def browser():
    async with async_playwright() as playwright:
        # https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
        headless = settings().HEADLESS
        slow_mo = settings().SLOW_MO
        browser = await playwright.chromium.launch(headless=headless, args=["-disable-dev-shm-usage"], slow_mo=slow_mo)
        yield browser
        await browser.close()


@pytest_asyncio.fixture(scope="function")
async def context(browser: Browser):
    args = {"timezone_id": "Europe/Helsinki", "viewport": {"width": 1920, "height": 1080}}
    context = await browser.new_context(**args)
    yield context
    await context.close()


@pytest_asyncio.fixture(scope="function")
async def page(context: BrowserContext, url=f"{Env.production_host}"):
    # https://playwright.dev/python/docs/api/class-browsercontext#browser-context-new-page
    page = await context.new_page()
    await page.goto(url)
    yield page
    await page.close()
