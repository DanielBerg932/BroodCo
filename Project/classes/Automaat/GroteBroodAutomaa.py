from classes.BroodAutomaat import BroodAutomaat


class GroteBroodAutomaat(BroodAutomaat):
    def startup(self):
        return super().startup()

    def __init__(self) -> None:
        super().__init__()
        self.max_brood = 105
