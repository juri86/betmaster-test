from core.page_object import PageObject


class SlotsPage(PageObject):
    def __init__(self, page):
        super().__init__(page, selector="div[id='root']", name="Slot page")
        self.categories = Categories(page, parent=self.selector)


class Categories(PageObject):
    def __init__(self, page, parent):
        super().__init__(page, selector=f"{parent} aside > div", name="Categories block")
        self.rtp98plus = PageObject(page, selector="a[href='/en/casino/slots/rtp-98']", name="RTP 98+")
        self.rtp98count = PageObject(page, selector=f"{self.rtp98plus.selector} span[role='status']", name="RTP 98+ count")
