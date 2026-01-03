from pydantic import BaseModel

class KeytermInsight(BaseModel):
    KEYTERM_INSIGHT_ID: int
    ORDER_NUMBER: int
    KEYTERM_CODE: str
    CLASSIFICATIONVALUE: str
    CLASSIFICATION_TERM_PRESENT: str
    CLASSIFICATION_RESULT: str
    ES_HITS: int