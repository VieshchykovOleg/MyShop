# comments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Product
from .models import Comment
from .forms import CommentForm

def comments_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('comments', product_id=product.id)
    else:
        form = CommentForm()

    return render(request, 'comments/comments_list.html', {
        'product': product,
        'comments': comments,
        'form': form
    })
