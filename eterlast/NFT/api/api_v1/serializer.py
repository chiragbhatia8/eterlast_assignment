from rest_framework import serializers
from eterlast.NFT.models import NFT, Collection


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = (
            "id",
            "asset_id",
            "name",
            "description",
            "picture",
            "external_link",
            "collection",
            "supply",
            "royalties",
            "buyer",
        )

    def create(self, validated_data):
        return NFT.objects.create(**validated_data)



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "description",
            "is_public",
            "creator_network",
        )

    def create(self, validated_data):
        return Collection.objects.create(**validated_data)