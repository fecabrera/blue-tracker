class GeneralInfo:
    def __init__(self, raw_data: dict):
        self.status_code = raw_data["statusCode"]
        self.data = raw_data["data"]
    
    @property
    def creation_date(self) -> str:
        return self.data.get("creationDate")
    
    @property
    def last_date_movement(self) -> str:
        return self.data.get("lastDateMovement")
    
    @property
    def promise_date(self) -> str:
        return self.data.get("promiseDate")