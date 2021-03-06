#-*- coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import InvalidPage, Paginator
from django.utils.decorators import method_decorator

from stucampus.articles.forms import ArticleForm
from stucampus.articles.forms import CategoryFormset
from stucampus.articles.models import Article, Category
from stucampus.utils import get_client_ip 
from stucampus.account.permission import check_perms

import re

NO_CATEGORY = u'未分类'

@check_perms('articles.article_add')
def manage(request):
    category = request.GET.get('category')
    editor = request.user
    pageid = request.GET.get('page')
    if editor.has_perm('articles.article_manage'):
        if not category:
            article_list = Article.objects.all()
        else:
            if category == NO_CATEGORY:
                article_list = Article.objects.filter(category=None)
            else:
                category = get_object_or_404(Category, name=category)
                article_list = Article.objects.filter(category=category)
    else:
        article_list = Article.objects.filter(editor=editor)
    paginator = Paginator(
            article_list.filter(deleted=False).order_by('-pk'), 10)
    try:
        page = paginator.page(pageid)
    except InvalidPage:
        pageid=1
        page = paginator.page(1)
    return render(request, 'articles/manage.html',
            {'page': page , 'pageid': pageid})


class AddView(View):

    @method_decorator(check_perms('articles.article_add'))
    def get(self, request):
        form = ArticleForm()
        return render(request, 'articles/article-form.html',
                {'form': form, 'post_url': reverse('articles:add')})

    @method_decorator(check_perms('articles.article_add'))
    def post(self, request):
        form = ArticleForm(request.POST)
        if not form.is_valid():
            return render(request, 'articles/article-form.html',
                    {'form': form, 'post_url': reverse('articles:add')})
        article = form.save(commit=False)
        article.editor = request.user
        article.create_ip = get_client_ip(request)

        re.sub(r'./imageTemp', "http://7xrrsw.com1.z0.glb.clouddn.com/stucampus-for-jiangxia", article.content)
        img_id = re.split(',', article.img_list)
        id_num = len(img_id)
        i = 0
        while(i < id_num):
            temp_obj1 = re.compile('<img id="' + id_num[i] + '.*?>')
            temp_obj2 = re.compile('value1=".*?"')
            temp_obj2b = re.compile('value2=".*?"')
            temp_obj3 = re.compile('[\d]+')
            temp_obj5 = re.compile('">')

            temp_str1 = temp_obj1.search(article.content)
            temp_str1b = temp_str1
            temp_str2 = temp_obj2.search(temp_str1)
            temp_str2b = temp_obj2b.search(temp_str1)
            temp_val1 = temp_obj3.search(temp_str2)
            temp_val2 = temp_obj3.search(temp_str2b)
            temp_str1 = re.sub(temp_obj5, '?imageView/2/w/' + temp_val1 + '/h/' + temp_val2 + '">', temp_str1)
            article.content = re.sub(temp_str1b, temp_str1, article.content)
            
        article.save()
        return HttpResponseRedirect(reverse('articles:manage'))

        execfile('./getImage.py')

class ModifyView(View):

    @method_decorator(check_perms('articles.article_add'))
    def get(self, request):
        article_id = request.GET.get('id')
        article = get_object_or_404(Article, pk=article_id)
        form = ArticleForm(instance=article)
        page = request.GET.get('page')
        return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id, 'page': page,
                 'post_url': reverse('articles:modify')})

    @method_decorator(check_perms('articles.article_add'))
    def post(self, request):
        article_id = request.GET.get('id')
        article = get_object_or_404(Article, pk=article_id)
        form = ArticleForm(request.POST, instance=article)
        page = request.GET.get('page')
        if not form.is_valid():
            return render(request, 'articles/article-form.html',
                {'form': form, 'article_id': article_id,
                 'post_url': reverse('articles:modify')})
        form.save()
        return HttpResponseRedirect(reverse('articles:manage')+'?page='+page)


@check_perms('articles.article_manage')
def del_article(request):
    article_id = request.GET.get('id')
    article = get_object_or_404(Article, pk=article_id)
    article.deleted = not article.deleted
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))


@check_perms('articles.article_manage')
def set_important(request):
    article_id = request.GET.get('id')
    article = get_object_or_404(Article, pk=article_id)
    article.important = not article.important
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))

@check_perms('articles.article_manage')
def publish(request):
    article_id = request.GET.get('id')
    article = get_object_or_404(Article, pk=article_id)
    article.publish = not article.publish
    article.save()
    return HttpResponseRedirect(reverse('articles:manage'))


class CategoryView(View):

    @staticmethod
    def create_category_list():
        category_list = Category.objects.all()
        category_list = {category.name: \
                len(Article.objects.filter(category=category, deleted=False)) \
                for category in Category.objects.all()}
        category_list[NO_CATEGORY] = \
                len(Article.objects.filter(category=None, deleted=False))
        return category_list

    @method_decorator(check_perms('articles.article_manage'))
    def get(self, request):
        category_list = CategoryView.create_category_list()
        formset = CategoryFormset()
        return render(request, 'articles/category-form.html',
                {'formset': formset, 'category_list': category_list})

    @method_decorator(check_perms('articles.article_manage'))
    def post(self, request):
        formset = CategoryFormset(request.POST)
        if not formset.is_valid():
            category_list = CategoryView.create_category_list()
            return render(request, 'articles/category-form.html',
                    {'formset': formset, 'category_list': category_list})
        formset.save()
        return HttpResponseRedirect(reverse('articles:category'))


def article_list(request, category=None):
    category = get_object_or_404(Category, english_name=category)
    article_list = Article.objects.filter(category=category,
                                          publish=True,
                                          deleted=False).order_by('-pk')
    paginator = Paginator(article_list, 10)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)

    hot_articles_list = \
        Article.objects.filter(
                publish=True,
                deleted=False).order_by('click_count')[:10]
    newest_articles_list = \
        Article.objects.filter(
                publish=True,
                deleted=False).order_by('-pk')[:10]
    return render(request, 'articles/article-list.html',
            {'page': page, 'category': category,
             'hot_articles_list': hot_articles_list,
             'newest_articles_list': newest_articles_list})


def article_display(request, id=None):
    article = get_object_or_404(Article, pk=id, publish=True, deleted=False)
    article.click_count += 1
    article.save()
    return render(request, 'articles/article-display.html',
            {'article': article})

