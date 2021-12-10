from datetime import datetime

def isNested(dict_to_check: dict) -> bool:
    for _, value in dict_to_check.items():
        if isinstance(value, dict):
            return True
    return False

def DatetimeConversion(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M:%S')