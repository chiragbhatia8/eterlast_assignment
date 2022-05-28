from rest_framework import viewsets, response, status, permissions

from eterlast.NFT.models import NFT, Collection
from eterlast.NFT.api.api_v1.serializer import NFTSerializer, CollectionSerializer




class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]

    def mint(self, request, *args, **kwargs):
        """
        Mint NFT
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve_nft(self, request, *args, **kwargs):
        """
        Retrieve NFT
        """
        nft = self.get_object()
        serializer = self.get_serializer(nft)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def list_nfts(self, request, *args, **kwargs):
        """
        List NFTs
        """
        nfts = self.get_queryset()
        serializer = self.get_serializer(nfts, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create Collection
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve_collection(self, request, *args, **kwargs):
        """
        Retrieve Collection
        """
        collection = self.get_object()
        serializer = self.get_serializer(collection)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def list_collections(self, request, *args, **kwargs):
        """
        List Collections
        """
        collections = self.get_queryset()
        serializer = self.get_serializer(collections, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)