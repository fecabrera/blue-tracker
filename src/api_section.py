class ApiSection:
    """Blue API envelope: top-level ``statusCode`` and nested ``data``."""

    _data: dict
    _status_code: int

    def __init__(self, raw_data: dict) -> None:
        self._data = raw_data["data"]
        self._status_code = int(raw_data["statusCode"])
