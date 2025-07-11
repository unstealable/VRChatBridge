from fastapi import APIRouter, HTTPException, Query
import httpx
import json
from typing import Optional
from app.env import CLIENT_NAME, API_BASE
from app.vrchat_context import get_context_safely
router = APIRouter()

@router.get("/users/me")
async def get_bot_users_profile():
    """Get the current bot's user profile."""
    vrchat = get_context_safely()
    if not vrchat.auth_cookie or not vrchat.auth_cookie.startswith("authcookie_"):
        raise HTTPException(status_code=401, detail="Token not found, please authenticate first")

    auth_cookie = vrchat.auth_cookie
    if not auth_cookie:
        raise HTTPException(status_code=401, detail="Auth cookie missing in token")

    headers = {"User-Agent": CLIENT_NAME}
    cookies = {"auth": auth_cookie}
    url = f"{API_BASE}/users/{vrchat.user_id}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, cookies=cookies)

    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=f"Failed to fetch user (current bot) info: {r.text}")

    return r.json()

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    """Get a user's profile by user ID."""
    vrchat = get_context_safely()
    if not vrchat.auth_cookie or not vrchat.auth_cookie.startswith("authcookie_"):
        raise HTTPException(status_code=401, detail="Token not found, please authenticate first")

    auth_cookie = vrchat.auth_cookie
    if not auth_cookie:
        raise HTTPException(status_code=401, detail="Auth cookie missing in token")

    headers = {"User-Agent": CLIENT_NAME}
    cookies = {"auth": auth_cookie}
    url = f"{API_BASE}/users/{user_id}"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, cookies=cookies)

    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=f"Failed to fetch user info: {r.text}")

    return r.json()

@router.get("/users/{user_id}/friends/status")
async def get_user_friend_status(user_id: str):
    """Get the friend status of a user by user ID."""
    vrchat = get_context_safely()
    if not vrchat.auth_cookie or not vrchat.auth_cookie.startswith("authcookie_"):
        raise HTTPException(status_code=401, detail="Token not found, please authenticate first")

    auth_cookie = vrchat.auth_cookie
    if not auth_cookie:
        raise HTTPException(status_code=401, detail="Auth cookie missing in token")

    headers = {"User-Agent": CLIENT_NAME}
    cookies = {"auth": auth_cookie}
    url = f"{API_BASE}/users/{user_id}/friendStatus"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, cookies=cookies)

    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=f"Failed to fetch user friend status info: {r.text}")

    return r.json()

@router.get("/users/{user_id}/groups")
async def get_user_groups(user_id: str):
    """Get the groups a user belongs to by user ID."""
    vrchat = get_context_safely()
    if not vrchat.auth_cookie or not vrchat.auth_cookie.startswith("authcookie_"):
        raise HTTPException(status_code=401, detail="Token not found, please authenticate first")

    auth_cookie = vrchat.auth_cookie
    if not auth_cookie:
        raise HTTPException(status_code=401, detail="Auth cookie missing in token")

    headers = {"User-Agent": CLIENT_NAME}
    cookies = {"auth": auth_cookie}
    url = f"{API_BASE}/users/{user_id}/groups"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, cookies=cookies)

    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=f"Failed to fetch user groups info: {r.text}")

    return r.json()

@router.get("/users/{user_id}/worlds")
async def get_user_worlds(user_id: str, n: int = Query(default=100), offset: int = Query(default=0)):
    """Get the worlds created by a user by user ID."""
    vrchat = get_context_safely()
    if not vrchat.auth_cookie or not vrchat.auth_cookie.startswith("authcookie_"):
        raise HTTPException(status_code=401, detail="Token not found, please authenticate first")

    auth_cookie = vrchat.auth_cookie
    if not auth_cookie:
        raise HTTPException(status_code=401, detail="Auth cookie missing in token")

    headers = {"User-Agent": CLIENT_NAME}
    cookies = {"auth": auth_cookie}
    params = {
        "releaseStatus": "public",
        "sort": "updated",
        "order": "descending",
        "userId": user_id,
        "n": str(n),
        "offset": str(offset)
    }   
    url = f"{API_BASE}/worlds"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, cookies=cookies, params=params)

    if r.status_code != 200:
        raise HTTPException(status_code=r.status_code, detail=f"Failed to fetch user worlds info: {r.text}")

    return r.json()