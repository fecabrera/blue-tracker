class BlueTrackerError(Exception):
    pass

class NoActiveMacrostateError(BlueTrackerError):
    pass
    
class StatusError(BlueTrackerError):
    pass

class FetchError(BlueTrackerError):
    pass
