from typing import Self
from json.decoder import JSONDecodeError
from requests.exceptions import HTTPError

from src.utils import fetch_api
from src.errors import StatusError, FetchError
from src.macrostate_info import MacrostateInfo
from src.general_info import GeneralInfo
from src.core_os import CoreOS

class OrderStatus:
    def __init__(self, raw_data: dict):
        if raw_data["status"] != "ok":
            raise StatusError(raw_data['message'])

        self.data = raw_data["data"]

        self.macrostate_info = MacrostateInfo(self.data["macroState"])
        self.general_info = GeneralInfo(self.data["generalInfo"])
        self.core_os = CoreOS(self.data["coreOs"])
    
    @classmethod
    def from_order_id(cls, order_id: int | str) -> Self:
        try:
            order = fetch_api(order_id)
        except HTTPError as e:
            raise FetchError(e)
        except JSONDecodeError as e:
            raise FetchError(e)

        return cls(order)
