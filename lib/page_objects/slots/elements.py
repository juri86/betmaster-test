from core.page_object import PageObject


class SlotsPage(PageObject):
    def __init__(self, page):
        super().__init__(page, selector="div[id='root']", name="Slot page")
        self.categories = Categories(page, parent=self.selector)


class Categories(PageObject):
    def __init__(self, page, parent):
        super().__init__(page, selector=f"{parent} ", name="Categories block")
        self.rtp98plus = PageObject(page, selector="", name="RTP 98+")
