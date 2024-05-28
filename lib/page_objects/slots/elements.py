from core.page_object import PageObject


class SlotsPage(PageObject):
    def __init__(self, page):
        super().__init__(page, selector="div[id='root']", name="Slot page")
        self.categories = Categories(page, parent=self.selector)
        self.game_img = PageObject(page, selector="section > img", name="Game image")


class Categories(PageObject):
    def __init__(self, page, parent):
        super().__init__(page, selector=f"{parent} div[class='_1q1i1h0']", name="Categories block")
        self.rtp98plus = PageObject(page, selector="a[href='/en/casino/slots/rtp-98']", name="RTP 98+")
