from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

all_posts = [
    {
        'slug':'hike-in-the mountains',
        'image':'mountains.jpg',
        'author':'Eren',
        'date':date(2023,12,30),
        'title':'Mountain Hiking',
        'excerpt':"here's nothing like the views you get when hiking in the mountains! and I wasn't even prepared for what happened whilst I was enjoying the view!",
        'content':""""
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        """    
    },

    {
        'slug':'ski',
        'image':'mountains.jpg',
        'author':'Eren',
        'date':date(2023,12,30),
        'title':'Mountain Hiking',
        'excerpt':"here's nothing like the views you get when hiking in the mountains! and I wasn't even prepared for what happened whilst I was enjoying the view!",
        'content':""""
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        """    
    },

    {
        'slug':'Travelling',
        'image':'mountains.jpg',
        'author':'Eren',
        'date':date(2023,12,30),
        'title':'Mountain Hiking',
        'excerpt':"here's nothing like the views you get when hiking in the mountains! and I wasn't even prepared for what happened whilst I was enjoying the view!",
        'content':""""
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        tag defines the contact information for the author/owner of a document or an article.
        The contact information can be an email address, URL, physical address, phone number,
        social media handle, etc.
        """    
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_list = sorted(all_posts,key=get_date)
    latest_post = sorted_list[-3:]
    return render(request,'blog/index.html',{'posts':latest_post,})

def posts(request):
    return render(request,'blog/all-posts.html')

def post_detail(request,slug):
    return render(request,'blog/post-detail.html')