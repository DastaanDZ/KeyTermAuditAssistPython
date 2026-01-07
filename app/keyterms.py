from pydantic import BaseModel


class Keyterms(BaseModel):
    ORDER_NUMBER: int
    KEYTERM_CODE: str
    USER_CLASSIFICATION_VALUE: str 


