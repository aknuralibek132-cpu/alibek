from django.contrib import admin
from .models import Client, LoyaltyRecalculationLog, LoyaltyReward, Product, Order, Stock, SpecialOffer
from django.utils.html import mark_safe
from django.contrib import admin
from .models import Promotion, Product

admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(SpecialOffer)

from django.contrib import admin
from django.utils.html import mark_safe
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "avatar_preview_list")
    readonly_fields = ("avatar_preview",)

    # Превью в списке
    def avatar_preview_list(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50" style="border-radius: 5px; object-fit: cover;" />')
        return "—"
    avatar_preview_list.short_description = "Аватар"

    # Превью в форме редактирования
    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="150" style="border-radius: 10px;" />')
        return "Нет изображения"
    avatar_preview.short_description = "Текущее фото"


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('promotion_name', 'discount_type', 'discount_value',
                    'start_date', 'end_date', 'priority')
    list_filter = ('discount_type', 'start_date', 'end_date')
    search_fields = ('promotion_name',)
    filter_horizontal = ('applicable_products',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(LoyaltyRecalculationLog)
class LoyaltyRecalculationLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'old_points', 'new_points', 'recalculated_at')
    list_filter = ('recalculated_at',)
    search_fields = ('client__name',)

@admin.register(LoyaltyReward)
class LoyaltyRewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'reward_type', 'redeemed_at')
    list_filter = ('redeemed_at', 'reward_type')
    search_fields = ('client__name',)