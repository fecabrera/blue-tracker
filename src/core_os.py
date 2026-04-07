from src.api_section import ApiSection


class CoreOS(ApiSection):
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