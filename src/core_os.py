class CoreOS:
    def __init__(self, raw_data: dict):
        self.status_code = raw_data["statusCode"]
        self.data = raw_data["data"]
    
    @property
    def display_name(self) -> str:
        return self.data.get("displayName")
    
    @property
    def receivable(self) -> bool:
        return self.data.get("receivable")
    
    @property
    def time_dl(self) -> str:
        return self.data.get("timeDL")
    
    @property
    def date_dl(self) -> str:
        return self.data.get("dateDL")