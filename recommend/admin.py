# recommend/admin.py
from django.contrib import admin
from .models import Item, Feedback

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'tags')
    list_filter = ('media_type',)
    search_fields = ('title', 'tags', 'reason')

# 管理画面で削除や検索がしやすいようにカスタマイズ
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'comment', 'created_at')  # 一覧に表示する項目
    list_filter = ('media_type', 'created_at')  # 絞り込みフィルター
    search_fields = ('title', 'comment')  # 検索ボックス
    ordering = ('-created_at',)  # 新しい順に表示
