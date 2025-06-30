from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="BugFlow Backend",
    version="0.1.0"
)

# Include routers
app.include_router(health_router, prefix="/api")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to BugFlow Backend"}