# recommend/views.py
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Item, Feedback
from .forms import FeedbackForm

def recommend_view(request):
    # --------------------------------------------------
    # 1. 診断ボタンからのAjax (POST) リクエスト処理
    # --------------------------------------------------
    if request.method == "POST":
        # もしフォーム（コメント投稿）からの送信だった場合
        if "media_type" in request.POST and "title" in request.POST:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('recommend')  # ご自身のurls.pyのnameに合わせて変更（例: 'recommend_view' など）
        
        # 診断（おすすめ選出）処理
        media_type = request.POST.get("media_type", "movie")
        mood = request.POST.get("mood", "")
        goal = request.POST.get("goal", "")

        # メディアタイプでフィルタリング
        items = Item.objects.filter(media_type=media_type)

        # 選択された「気分」や「目的」のタグが含まれる作品を検索
        if mood:
            items = items.filter(tags__contains=mood)
        if goal:
            items = items.filter(tags__contains=goal)

        # 条件に合う作品がない場合はフォールバック
        if not items.exists():
            items = Item.objects.filter(media_type=media_type)

        # ランダムで1件選出
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

    # --------------------------------------------------
    # 2. 最初（GETアクセス）でページを開いたときの処理
    # --------------------------------------------------
    form = FeedbackForm()
    feedbacks = Feedback.objects.all()
    items = Item.objects.all()

    context = {
        'items': items,
        'form': form,
        'feedbacks': feedbacks,
    }
    return render(request, "recommend/index.html", context)