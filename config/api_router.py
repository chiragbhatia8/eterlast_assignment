from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import re_path, include
from eterlast.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "nft-api"

router.register("users", UserViewSet)
api_urls = [
    re_path(
        r"(?P<version>(v1))/",
        include(("eterlast.NFT.urls", "NFT"), namespace="NFT"),
    ),
]


urlpatterns = router.urls + api_urls
