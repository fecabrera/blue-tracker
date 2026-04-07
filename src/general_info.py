from src.api_section import ApiSection


class GeneralInfo(ApiSection):
    @property
    def creation_date(self) -> str:
        return self._data.get("creationDate")
    
    @property
    def last_movement_date(self) -> str:
        return self._data.get("lastDateMovement")
    
    @property
    def expected_delivery_date(self) -> str:
        return self._data.get("promiseDate")