class Macrostate:
    def __init__(self, data: dict):
        self.data = data
    
    @property
    def is_active(self) -> bool:
        return self.data["isActive"]
    
    @property
    def title(self) -> str:
        return self.data["title"]
    
    @property
    def message(self) -> str:
        return self.data["message"]
