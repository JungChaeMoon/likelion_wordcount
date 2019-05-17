from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from count.models import Star, Vote
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse


def view(request):
    return render(request, 'count/wordcount.html')


def detail(request):

    full_text = request.POST['fulltext']
    word_list = full_text.split()
    word_dictionary ={}
    #context = {'fulltext':full_text, 'total':len(word_list), 'dictionary':word_dictionary.items()}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, 'count/wordcount1.html', {'fulltext':full_text, 'total':len(word_list), 'dictionary':word_dictionary.items()})


def about(request):

    return render(request, 'count/wordcount2.html')


def see(request):
    star_list = Star.objects.all()
    return render(request, 'count/wordcount3.html', {'star_list': star_list})


def vote(request, *args, **kwargs):
    star_id = request.POST.get('star_id')

    star_id_text = get_object_or_404(Star, pk=star_id)

    vote = Vote()

    vote.star = star_id_text
    vote.save()

    # star.votes.all()
    #Vote.objects.filter(star=star_id_text)

    # Vote.objects.create(
    #     star=star_id_text
    # )
    return HttpResponseRedirect(reverse('count:result'))


def results(request, *args, **kwargs):
    stars = Star.objects.all()
    return render(request, 'count/wordcount4.html', {'stars': stars})