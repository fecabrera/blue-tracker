from src.errors import NoActiveMacrostateError
from src.macrostate import Macrostate

class MacrostateInfo:
    _data: dict
    _status_code: int

    def __init__(self, raw_data: dict):
        self._data = raw_data["data"]
        self._status_code = int(raw_data["statusCode"])

        self.macrostates = [
            Macrostate(state) for state in self._data["traceMacrostates"]["macrostates"]
        ]
    
    def get_active_macrostate(self) -> Macrostate:
        try:
            return next(state for state in self.macrostates if state.is_active)
        except StopIteration:
            raise NoActiveMacrostateError
