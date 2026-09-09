# recommend/views.py
import random
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Item

def recommend_view(request):
    if request.method == "POST":
        media_type = request.POST.get("media_type", "movie")
        mood = request.POST.get("mood", "")
        goal = request.POST.get("goal", "")

        # 1. メディアタイプ（映画 or 本）でフィルタリング
        items = Item.objects.filter(media_type=media_type)

        # 2. 選択された「気分」や「目的」のタグが含まれる作品を検索
        if mood:
            items = items.filter(tags__contains=mood)
        if goal:
            items = items.filter(tags__contains=goal)

        # 3. 条件に合う作品がない場合は、そのメディア全体の全作品からフォールバック選出
        if not items.exists():
            items = Item.objects.filter(media_type=media_type)

        # 4. DBに作品が1件以上あればランダムで1つチョイス
        if items.exists():
            item = random.choice(list(items))
            return JsonResponse({
                "status": "success",
                "title": item.title,
                "reason": item.reason,
                "image_url": item.image_url,
            })
        else:
            return JsonResponse({
                "status": "error",
                "error": "作品がまだ登録されていません。管理画面から登録してください。"
            }, status=404)

    return render(request, "recommend/index.html")