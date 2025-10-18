from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from datetime import datetime, timezone
from slowapi import Limiter
from slowapi.util import get_remote_address
from .config import settings
import httpx
import logging

CAT_FACT_URL = "https://catfact.ninja/fact?max_length=140"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="HNG13 Backend Stage0 Dynamic Profile Endpoint",
    description=(
        "A simple RESTful API that returns profile information "
        "and a dynamic cat fact fetched from an external API."
    ),
    contact={"email": settings.CONTACT_EMAIL},
)

app.state.limiter = limiter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "localhost",
        "127.0.0.1",
        "0.0.0.0",
        "hng13-backend-stage0-dynamic-profile-endpoint-production.up.railway.app",
    ],
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


async def get_cat_fact() -> str:
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(CAT_FACT_URL)
            response.raise_for_status()
            data = response.json()
            fact = data.get("fact", "No fact availableat the moment.")
            logger.info("Fetched cat fact successfully.")
            return fact

    except httpx.RequestError as e:
        logger.error(f"Network error while fetching cat fact: {e}")
        raise HTTPException(status_code=502, detail="Failed to fetch cat fact.")

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error.")


@app.get("/")
@limiter.limit("10/minute")
async def root(request: Request):
    logger.info(f"Root endpoint accessed by {request.client.host}")
    return {"message": "Journey to becoming a finalist begins with this task."}


@app.get("/me")
@limiter.limit("5/minute")
async def profile(request: Request):
    logger.info(f"/me endpoint accessed by {request.client.host}")
    cat_fact = await get_cat_fact()
    return {
        "status": "success",
        "user": {
            "email": settings.CONTACT_EMAIL,
            "name": "Anaeto Anthony Ifeanyi",
            "stack": "Python/FastAPI",
        },
        "timestamp": utc_now(),
        "fact": cat_fact,
    }
