from config.models import SideBar
from django.shortcuts import render

from .models import Post, Category


# Create your views here.
def post_list(request,category_id=None,tag_id=None):
    # content = 'post_list category_id={category_id},tag_id={tag_id}'.format(
    #     category_id = category_id,
    #     tag_id = tag_id
    # )
    # return HttpResponse(content)
    # return render(request,'blog/list.html',context={'name':'post_list'})
    tag = None
    category = None
    if tag_id:
        # 一
        # try:
        #     tag = Tag.objects.get(id=tag_id)
        # except Tag.DoesNotExist:
        #     post_list = []
        # else:
        #     post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
        # 二
        # post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        # post_list = post_list.filter(tag__id=tag_id)
        # 三
        tag,post_list = Post.get_by_tag(tag_id)
    elif category_id:
    # else:
        # 一
        # try:
        #     category = Category.objects.get(id = category_id)
        # except Category.DoesNotExist:
        #     post_list = []
        # else:
        #     post_list = category.post_set.filter(status = Post.STATUS_NORMAL)
        # 二
        # post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        # if category_id:
        #     post_list = post_list.filter(category_id = category_id)
        # 三
        category, post_list = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    content = {
        'category':category,
        'tag':tag,
        'post_list':post_list,
        'sidebars': SideBar.get_all()
    }
    content.update(Category.get_nav())
    return render(request,'blog/list.html',context=content)


def post_detail(request,post_id=None):
    # return render(request,'blog/detail.html',context={'name':'post_detail'})
    try:
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post':post,
        'sidebars':SideBar.get_all()
    }
    context.update(Category.get_nav())
    return render(request,'blog/detail.html',context=context)
