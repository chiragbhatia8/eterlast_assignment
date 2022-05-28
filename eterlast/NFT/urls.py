from django.urls import path

from eterlast.NFT.api.api_v1.views import NFTViewSet, CollectionViewSet

app_name = "NFT"

urlpatterns = [
    path(
        "mint/",
        NFTViewSet.as_view({"post": "mint"}),
    ),
    path(
        "NFT/<str:id>",
        NFTViewSet.as_view({"get": "retrieve_nft"}),
    ),
    path(
        "NFTs",
        NFTViewSet.as_view({"get": "list_nfts"}),
    ),
    path(
        "create_collection",
        CollectionViewSet.as_view({"post": "create"}),
    ),
    path(
        "collection/all",
        CollectionViewSet.as_view({"get": "list_collections"}),
    ),
    path(
        "collection/<str:collection_id>",
        CollectionViewSet.as_view({"get": "list_collections"}),
    ),
]
