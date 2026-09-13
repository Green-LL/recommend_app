from django.db import models

class Item(models.Model):
    MEDIA_CHOICES = [
        ('movie', '映画'),
        ('book', '本'),
    ]

    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, verbose_name="メディア")
    title = models.CharField(max_length=200, verbose_name="タイトル")
    reason = models.TextField(verbose_name="おすすめ理由・あらすじ")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="画像URL")
    
    # 検索用タグ（カンマ区切り、または特定のキーワード）
    # 例: "疲れた, 癒やされたい, 2時間"
    tags = models.CharField(max_length=200, help_text="カンマ区切りでタグを入力（例: 疲れた, 癒やされたい）", verbose_name="タグ")

    def __str__(self):
        return f"[{self.get_media_type_display()}] {self.title}"


class Feedback(models.Model):
    MEDIA_CHOICES = [
        ('movie', '映画'),
        ('book', '本'),
    ]
    
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, verbose_name="メディア")
    title = models.CharField(max_length=200, verbose_name="好きな作品名")
    comment = models.TextField(blank=True, null=True, verbose_name="コメント・おすすめ理由")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")

    class Meta:
        ordering = ['-created_at']  # 新しい投稿順（降順）に並べる

    def __str__(self):
        return f"[{self.get_media_type_display()}] {self.title}"