from enum import Enum

class EventCode(Enum):
    DELIVERED = "DL"
    OUT_FOR_DELIVERY = "LD"
    ADMITTED_TO_WAREHOUSE = "FW"
    FZP = "FZP"
    FTR = "FTR"  # could mean "Forward to Return" or "Failed Transit",

class Segment(Enum):
    CROSS_BORDER = "crossborder"
    APP_COPEC = "app copec"
    PYME = "pyme"
    OTHER = "otro"

class ServiceType(Enum):
    EXPRESS = "EXPRESS"
    PRIORITY = "PRIORITY"
