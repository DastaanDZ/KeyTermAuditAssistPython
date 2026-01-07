from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from .utils import load_keyterms, get_term_data,keyterm_parsing
from .keyterm_classification import KeytermClassification
from .keyterms import Keyterms
from .keyterm_insight import KeytermInsight
from .keyterm_ES import KeytermES
from supabase import create_client

SUPABASE_URL = "https://xmhxmedbthkfnsjjgaie.supabase.co"
SUPABASE_KEY = "sb_secret_HxVENnifk1lihvWhfQ9L-A_KnDy9nvR"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(
    title="Key Term API", description="API for fetching keyterm data.", version="1.0.0"
)

keyterms_data = load_keyterms()


@app.get("/keyterm")
def keyterm_lookup(keyterm: str = Query(..., description="The keyterm to look up")):
    """
    Get data for a specific keyterm using a query parameter.
    Example: /keyterm?keyterm=Recovery%20Time%20Objective
    """
    result = get_term_data(keyterms_data, keyterm)
    if not result:
        raise HTTPException(status_code=404, detail="Key term not found")
    return result


@app.get("/keytermsClassification", response_model=List[KeytermClassification])
def get_keyterm_classification(
    ordernumber: Optional[int] = Query(None, description="Order number (BIGINT)"),
    keyterm: Optional[str] = Query(None, description="Keyterm code"),
):
    # Start base query
    query = supabase.table("KEYTERM_CLASSIFICATION_ALL").select("*")

    # Apply filters only if present
    if ordernumber is not None:
        query = query.eq("ORDER_NUMBER", ordernumber)

    if keyterm is not None:
        query = query.eq("KEYTERM_CODE", keyterm_parsing(keyterm))

    response = query.execute()
    data = response.data

    if not data:
        raise HTTPException(
            status_code=404, detail="No records found for given filters"
        )

    return data


@app.get("/keytermsInsight", response_model=List[KeytermInsight])
def get_keyterm_insight(
    ordernumber: Optional[int] = Query(None, description="Order number (BIGINT)"),
    keyterm: Optional[str] = Query(None, description="Keyterm code"),
):
    # Start base query
    query = supabase.table("KEYTERM_INSIGHT").select("*")

    # Apply filters only if present
    if ordernumber is not None:
        query = query.eq("ORDER_NUMBER", ordernumber)

    if keyterm is not None:
        query = query.eq("KEYTERM_CODE", keyterm_parsing(keyterm))

    response = query.execute()
    data = response.data

    if not data:
        raise HTTPException(
            status_code=404, detail="No records found for given filters"
        )

    return data


@app.get("/keytermsES", response_model=List[KeytermES])
def get_keyterm_insight(
    ordernumber: Optional[int] = Query(None, description="Order number (BIGINT)"),
    keyterm: Optional[str] = Query(None, description="Keyterm code"),
):
    # Start base query
    query = supabase.table("KEYTERM_ES_INTEGRATION").select("*")

    # Apply filters only if present
    if ordernumber is not None:
        query = query.eq("ORDER_NUMBER", ordernumber)

    if keyterm is not None:
        query = query.eq("KEYTERM_CODE", keyterm_parsing(keyterm))

    response = query.execute()
    data = response.data

    if not data:
        raise HTTPException(
            status_code=404, detail="No records found for given filters"
        )

    return data


@app.get("/keyterms", response_model=List[Keyterms])
def get_keyterm_classification(
    ordernumber: Optional[int] = Query(None, description="Order number (BIGINT)")
):
    # Start base query
    query = supabase.table("KEYTERMS_ALL").select("*")

    # Apply filters only if present
    if ordernumber is not None:
        query = query.eq("ORDER_NUMBER", ordernumber)

    response = query.execute()
    data = response.data

    if not data:
        raise HTTPException(
            status_code=404, detail="No records found for given filters"
        )

    return data

@app.get("/test")
def test():
    return "4.5"
