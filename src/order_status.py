from typing import Self
from enum import Enum
from src.utils import fetch_api
from src.macrostate import Macrostate

class OrderStatus:
    class NoActiveMacrostateError(Exception):
        pass
    
    class Error(Exception):
        pass

    def __init__(self, raw_data: dict):
        if raw_data["status"] != "ok":
            raise self.Error(raw_data["message"])

        self.data = raw_data["data"]

        self.macrostate_data = self.data["macroState"]
        self.general_info = self.data["generalInfo"]
        self.core_os = self.data["coreOs"]

        self.macrostates = [
            Macrostate(state) for state in self.macrostate_data["data"]["traceMacrostates"]["macrostates"]
        ]
    
    def get_active_macrostate(self) -> Macrostate:
        try:
            return next(state for state in self.macrostates if state.is_active)
        except StopIteration:
            raise self.NoActiveMacrostateError
    
    @classmethod
    def from_order_id(cls, order_id: int | str) -> Self:
        order = fetch_api(order_id)
        return cls(order)
