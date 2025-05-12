from typing import Union

from fastapi import FastAPI
from app.api.v1.routers import account_router, creators_router, billing_router, rewards_router, webhooks_router

app = FastAPI()

app.include_router(account_router)
app.include_router(creators_router)
app.include_router(billing_router)
app.include_router(rewards_router)
app.include_router(webhooks_router)
