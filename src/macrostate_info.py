from src.api_section import ApiSection
from src.errors import NoActiveMacrostateError
from src.macrostate import Macrostate


class MacrostateInfo(ApiSection):
    def __init__(self, raw_data: dict) -> None:
        super().__init__(raw_data)
        self.macrostates = [
            Macrostate(state) for state in self._data["traceMacrostates"]["macrostates"]
        ]
    
    def get_active_macrostate(self) -> Macrostate:
        try:
            return next(state for state in self.macrostates if state.is_active)
        except StopIteration:
            raise NoActiveMacrostateError
