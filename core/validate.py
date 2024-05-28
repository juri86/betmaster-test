from assertpy import assert_that
from typing import Any


class Validate:
    def __init__(self):
        self.assert_that = assert_that

    def assert_that_entity_is_equal_to_expect(self, actual_val: Any, expected_val: Any):
        try:
            self.assert_that(actual_val).is_equal_to(expected_val)
        except AssertionError as err:
            raise Exception(f"{err}")

    def assert_that_b(self):
        pass

    def assert_that_c(self):
        pass
