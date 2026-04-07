class GeneralInfo:
    _data: dict
    _status_code: int

    def __init__(self, raw_data: dict):
        self._data = raw_data["data"]
        self._status_code = int(raw_data["statusCode"])
    
    @property
    def creation_date(self) -> str:
        return self._data.get("creationDate")
    
    @property
    def last_movement_date(self) -> str:
        return self._data.get("lastDateMovement")
    
    @property
    def expected_delivery_date(self) -> str:
        return self._data.get("promiseDate")