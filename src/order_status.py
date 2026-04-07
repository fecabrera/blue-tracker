from typing import Self
from json.decoder import JSONDecodeError
from requests.exceptions import HTTPError

from src.fetch_api import fetch_api
from src.errors import StatusError, FetchError
from src.macrostate_info import MacrostateInfo
from src.general_info import GeneralInfo
from src.core_os import CoreOS

class OrderStatus:
    _data: dict
    _status: str
    _message: str

    macrostate_info: MacrostateInfo
    general_info: GeneralInfo
    core_os: CoreOS

    def __init__(self, raw_data: dict):
        self._data = raw_data["data"]
        self._status = raw_data["status"]
        self._message = raw_data["message"]
        
        if self._status != "ok":
            raise StatusError(self._message)

        self.macrostate_info = MacrostateInfo(self._data["macroState"])
        self.general_info = GeneralInfo(self._data["generalInfo"])
        self.core_os = CoreOS(self._data["coreOs"])
    
    @classmethod
    def from_order_id(cls, order_id: int | str) -> Self:
        try:
            order = fetch_api(order_id)
        except HTTPError as e:
            raise FetchError(e)
        except JSONDecodeError as e:
            raise FetchError(e)

        return cls(order)
