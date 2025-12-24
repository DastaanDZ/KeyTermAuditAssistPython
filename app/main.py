from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from .utils import load_keyterms, get_term_data
from .keyterm_entity import KeytermInsight
from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
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


@app.get("/keyterms", response_model=List[KeytermInsight])
def get_keyterm_insights(
    order_number: Optional[int] = Query(None, description="Order number (BIGINT)"),
    keyterm_code: Optional[str] = Query(None, description="Keyterm code"),
):
    # Start base query
    query = supabase.table("KEYTERM_CLASSIFICATION_ALL").select("*")

    # Apply filters only if present
    if order_number is not None:
        query = query.eq("ORDER_NUMBER", order_number)

    if keyterm_code is not None:
        query = query.eq("KEYTERM_CODE", keyterm_code)

    response = query.execute()
    data = response.data

    if not data:
        raise HTTPException(
            status_code=404, detail="No records found for given filters"
        )

    return data
