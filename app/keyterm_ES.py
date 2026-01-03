from pydantic import BaseModel

class KeytermES(BaseModel):
    ES_ID: int
    ORDER_NUMBER: int
    KEYTERM_CODE: str
    PAGE_NUMBER: int
    SECTIONHEADER: str
    PARAGRAPHTEXT: str
    