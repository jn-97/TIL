from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            messages.success(request, "리뷰 작성이 완료되었습니다.")
            return redirect("reviews:index")
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/form.html", context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect("reviews:detail", review.pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            "form": form,
        }
        return render(request, "reviews/form.html", context)
    else:
        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return redirect("accounts:login")


@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user.pk == review.user.pk:
        review.delete()
        return redirect("reviews:index")
    else:
        messages.warning(request, "작성자만 삭제할 수 있습니다.")
        return redirect("reviews:index")


@login_required
def like(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        "isLiked": is_liked,
        "likeCount": review.like_users.count(),
    }
    return JsonResponse(context)
