from django.contrib import admin
from eterlast.NFT.models import NFT, Collection

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'picture')
    search_fields = ('name', 'description', 'picture', 'owner')
    ordering = ('-created',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description', 'creator_network')
    ordering = ('-created',)