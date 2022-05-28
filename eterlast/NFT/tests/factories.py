from typing import Any, Sequence


from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from eterlast.NFT.models import NFT

class NFTFactory(DjangoModelFactory):

    name = Faker("name")
    description = Faker("description")
    picture = Faker("picture")


    class Meta:
        model = NFT
        django_get_or_create = ["username"]
