class Macrostate:
    def __init__(self, raw_data: dict):
        self.data = raw_data
    
    @property
    def is_active(self) -> bool:
        return self.data.get("isActive", False)
    
    @property
    def title(self) -> str:
        return self.data.get("title")
    
    @property
    def message(self) -> str:
        return self.data.get("message")
