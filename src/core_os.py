class CoreOS:
    _data: dict
    _status_code: int

    def __init__(self, raw_data: dict):
        self._data = raw_data["data"]
        self._status_code = int(raw_data["statusCode"])
    
    @property
    def display_name(self) -> str:
        return self._data.get("displayName")
    
    @property
    def receivable(self) -> bool:
        return self._data.get("receivable")
    
    @property
    def delivery_time(self) -> str:
        return self._data.get("timeDL")
    
    @property
    def delivery_date(self) -> str:
        return self._data.get("dateDL")