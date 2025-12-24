from fastapi import FastAPI, HTTPException, Query
from .utils import load_keyterms, get_term_data

app = FastAPI(
    title="Key Term Lookup API",
    description="API for looking up key term metadata from a JSON configuration.",
    version="1.0.0"
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