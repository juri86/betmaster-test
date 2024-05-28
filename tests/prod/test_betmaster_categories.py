import pytest

from core.testcase import BaseTest
from lib.page_objects.slots.elements import SlotsPage
from lib.api import RestApi


class TestBetmasterCategories(BaseTest):
    @pytest.mark.asyncio
    @pytest.mark.parametrize("category", ["rtp98", "rtp98wrong"])
    async def test_betmaster_category_rpt98(self, page, category):
        self.description("Open category RTP98+ and get game images in the category")
        slot_page = SlotsPage(page)
        await slot_page.categories.rtp98plus.click()
        frontend_games_count = await slot_page.game_img.elements_count(wait_before=500)

        self.description("MOCK: Send request to backend to understand count of games in the category RTP98+")
        _, resp_body = RestApi().get_games_in_category(category)
        backend_games_count = len(resp_body["games"])

        self.description("Assert count of games between frontend and backend response")
        self.validate.assert_that_entity_is_equal_to_expect(frontend_games_count, backend_games_count)
