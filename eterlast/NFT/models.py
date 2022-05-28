
from django.db import models
from django_extensions.validators import HexValidator

from eterlast.users.models import User, UserWallet
from eterlast.core.behaviours import UUIDMixin


class Collection(UUIDMixin):
    """
    User collection model.
    id: uuid,
    name: string,
    description: text,
    creator: User
    creator_network: user_wallet

    """

    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL,blank=True, null=True, related_name="collections",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    creator_network = models.ForeignKey(
        UserWallet, on_delete=models.SET_NULL,blank=True, null=True, related_name="collections",
    )

    def __str__(self):
        return f"{self.creator.username}'s collection {self.name}"



class NFT(UUIDMixin):
    """
    NFT model.
    asset_id: hex(16chars),
    name: string,
    description: text,
    picture: url_bassed_picture,

    external_link: link_your_item_web_page_info,
    collection: Collection,
    supply: number_copies,
    royalties: amount_royalty,
    date_of_creation: current_date,
    buyer: crypto_wallet

    """


    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to="nfts", blank=True)
    external_link = models.URLField(blank=True)

    collection = models.ForeignKey(
        "Collection", on_delete=models.SET_NULL,blank=True, null=True, related_name="nfts",
    )

    supply = models.PositiveIntegerField(default=0)
    royalties = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    buyer = models.ForeignKey(
        User, on_delete=models.SET_NULL,blank=True, null=True, related_name="nfts",
    )
    asset_id = models.CharField(max_length=64, validators=[HexValidator(length=16)])

    def __str__(self):
        return self.name
