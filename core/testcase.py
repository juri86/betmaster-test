from core.validate import Validate


class BaseTest:
    validate = Validate()

    current_step: int = 0
    step_txt = None

    def step_description(self, text: str):
        self.current_step = self.current_step + 1
        self.step_txt = text
