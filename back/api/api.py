from fastapi import APIRouter

from api.endpoints import videos, subtitles, categories, playlists
from core.config import settings

api_router = APIRouter()

# Include routers for different resources
api_router.include_router(videos.router, prefix="/videos", tags=["videos"], include_in_schema=False)
api_router.include_router(
    subtitles.router, prefix="/subtitles", tags=["subtitles"], include_in_schema=False)
api_router.include_router(
    categories.router, prefix="/categories", tags=["categories"] , include_in_schema=False)
api_router.include_router(
    playlists.router, prefix="/playlists", tags=["playlists"], include_in_schema=False)
