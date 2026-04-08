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

    @property
    def has_exception(self) -> bool:
        return self.data.get("isException", False)
    
    @property
    def exception_type(self) -> str:
        return self.data.get("exceptionType")
