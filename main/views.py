from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
def home_shop(request):
    posts = Shop.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'index.html', {'posts':posts})

def detail_shop(request, id):
    post = get_object_or_404(Shop, id=id)
    return render(request, 'detail.html', {'post':post})

def create_shop(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        images = request.FILES.get('images')
        is_active = 'is_active' in request.POST

        Shop.objects.create(
            title=title,
            description=description,
            price=price,
            images=images,
            is_active = is_active
        )
        return redirect('home')
    return render(request, 'create.html')

def delete_shop(request, id):
    post = get_object_or_404(Shop, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete.html', {'post':post})

def update_shop(request, id):
    post = get_object_or_404(Shop, id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        images = request.FILES.get('images')

        if title:
            post.title = title

        if description:
            post.description = description

        if images:
            post.images = images

        if price:
            post.price = price    

        post.is_active = 'is_active' in request.POST    

        post.save()
        return redirect('detail-shop', post.id)    

    return render(request, 'update.html', {'post':post})            