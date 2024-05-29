from playwright.async_api import TimeoutError as PlaywrightTimeoutError, Page

from core.settings import settings


class PageObject:
    def __init__(self, page: Page, selector="", name=None, parent="", strategy="css-selector", discover=True, **kwargs):
        """
        :param page: Page, Playwright Page object
        :param selector: Playwright selector
        :param locator: Playwright Locator
        :param name: PageObject name
        :param parent: PageObject parent
        :param strategy: str, default 'css-selector'
        :param discover: PageObject discover, boolean, Use 'False' for page objects if object do not exist after load
        """
        spacer = " " if strategy == "css-selector" else ""
        self.page = page
        self.selector = str(parent) + spacer + selector  # Parent + selector path, based on strategy
        self.name = name
        self.locator = self.get_locator()
        self.parent = parent
        self.discover = discover
        self.strategy = strategy

    def get_locator(self, has_text=None):
        """
        returns element Locator
        :param has_text: str, default: None, filter by text,
        :return: Locator
        """
        match has_text:
            case str():
                # https://playwright.dev/python/docs/release-notes#locator-improvements
                return self.page.locator(self.selector, has_text=has_text)
            case _:
                return self.page.locator(self.selector)

    def get_locator_name(self, info=False):
        """
        returns page object name
        :param info: boolean, default: False, will return additional info about selector
        :return: str
        """
        match info:
            case True:
                if self.name:
                    return f"{self.name} ({self.selector.strip()})"
                return self.selector
            case _:
                if self.name:
                    return self.name
                return self.selector

    async def blink_element(self):
        """
        wrapper for Playwright locator.highlight()
        https://playwright.dev/python/docs/api/class-locator#locator-highlight
        :return: None
        """
        await self.locator.highlight()
        await self.page.wait_for_timeout(500)

    async def click(self, wait_before: int = 0, wait_after: int = 0, force=False):
        """
        click element action
        :param wait_before: int, default 0, will wait ms before click
        :param wait_after: int, default 0, will wait ms after click
        :param force: bool, default False, force click
        :return: None
        """
        try:
            await self.page.wait_for_timeout(wait_before)
            if settings().BLINK_ELEMENT is True:
                await self.blink_element()
            await self.locator.click(timeout=settings().ELEMENT_TIMEOUT, force=force)
            await self.page.wait_for_timeout(wait_after)
        except PlaywrightTimeoutError:
            msg = f"Element '{self.get_locator_name(info=True)}' can't use 'click' action"
            raise Exception(msg)

    async def text(self):
        """
        get text content inside the tag
        :return: str
        """
        return await self.locator.text_content(timeout=settings().ELEMENT_TIMEOUT)
