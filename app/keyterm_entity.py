from pydantic import BaseModel


class KeytermInsight(BaseModel):
    KEYTERM_INSIGHT_ID: int
    ORDER_NUMBER: int
    KEYTERM_CODE: str
    SYSTEM_VALUE: str
    USER_VALUE: str 
    LAST_UPDATE_DATE: str
    LAST_UPDATE_BY: str