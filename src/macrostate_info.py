from src.errors import NoActiveMacrostateError
from src.macrostate import Macrostate

class MacrostateInfo:
    def __init__(self, raw_data: dict):
        self.status_code = raw_data["statusCode"]
        self.data = raw_data["data"]

        self.macrostates = [
            Macrostate(state) for state in self.data["traceMacrostates"]["macrostates"]
        ]
    
    def get_active_macrostate(self) -> Macrostate:
        try:
            return next(state for state in self.macrostates if state.is_active)
        except StopIteration:
            raise NoActiveMacrostateError
