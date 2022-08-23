from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keywords

app = FastAPI()
MAX_INPUT_LENGTH = 32

# Snippets
@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}

# Keywords
@app.get("/generate_keyword")
async def generate_keywords_api(prompt: str):
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}

# Snippet AND Keywords Together
@app.get("/generate_snippet_and_keyword")
async def generate_keywords_api(prompt: str):
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, 
                            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters."
                        )
        

# uvicorn copykitt_api:app --reload