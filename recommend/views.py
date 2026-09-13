# recommend/views.py
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Item, Feedback
from .forms import FeedbackForm

def recommend_view(request):
    # --------------------------------------------------
    # POSTリクエスト（コメント投稿 または 診断ボタン）
    # --------------------------------------------------
    if request.method == "POST":
        
        # A. コメント投稿フォームからの送信の場合
        if "action" in request.POST and request.POST.get("action") == "feedback":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('recommend_view')  # ご自身のurls.pyのnameに合わせてください

        # B. 診断ボタン（JavaScript/Ajax）からの送信の場合
        media_type = request.POST.get("media_type", "movie")
        mood = request.POST.get("mood", "")
        goal = request.POST.get("goal", "")

        items = Item.objects.filter(media_type=media_type)

        if mood:
            items = items.filter(tags__contains=mood)
        if goal:
            items = items.filter(tags__contains=goal)

        if not items.exists():
            items = Item.objects.filter(media_type=media_type)

        if items.exists():
            item = random.choice(list(items))
            return JsonResponse({
                "status": "success",
                "title": item.title,
                "reason": item.reason,
                "image_url": item.image_url if hasattr(item, 'image_url') else '',
            })
        else:
            return JsonResponse({
                "status": "error",
                "error": "作品がまだ登録されていません。"
            }, status=404)

    # --------------------------------------------------
    # GETリクエスト（最初のページ表示時）
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