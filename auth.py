# auth.py
import os
from starlette.authentication import (
    AuthenticationBackend, AuthCredentials, UnauthenticatedUser
)
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse

TOKEN = os.getenv("MCP_BEARER_TOKEN")

class BearerAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        hdr = conn.headers.get("authorization")
        if not hdr:
            return                      # nada → request continuará sem user
        scheme, _, token = hdr.partition(" ")
        if scheme.lower() != "bearer" or token != TOKEN:
            raise AuthError             # token errado → 401
        return AuthCredentials(["authenticated"]), UnauthenticatedUser()

class AuthError(Exception):
    pass

async def auth_exception_handler(request, exc):
    return PlainTextResponse("Unauthorized", status_code=401)
