import pytest

from core.testcase import BaseTest
from lib.page_objects.slots.elements import SlotsPage
from lib.api import RestApi


class TestBetmasterCategories(BaseTest):
    @pytest.mark.asyncio
    @pytest.mark.parametrize("category", ["rtp98", "rtp98wrong"])
    async def test_betmaster_category_rpt98(self, page, category):
        self.step_description("Open RTP98 category")
        slot_page = SlotsPage(page)
        # await slot_page.categories.rtp98plus.click()
        frontend_games_count = 2

        self.step_description("MOCK: Send request to backend to understand count of games in the RTP98 category")
        _, resp_body = RestApi().get_games_in_category(category)
        backend_games_count = len(resp_body["games"])

        self.step_description("Assert count of games between frontend and backend response")
        self.validate.assert_that_entity_is_equal_to_expect(frontend_games_count, backend_games_count)

    @pytest.mark.asyncio
    async def test_betmaster_category_all_slots(self):
        pass
