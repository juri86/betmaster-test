from core.validate import Validate


class BaseTest:
    validate = Validate()
    step_txt = None

    def description(self, text: str):
        self.step_txt = text
