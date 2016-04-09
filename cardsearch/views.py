from django.shortcuts import render

def card_list(request):
    return render(request, 'cardsearch/card_list.html', {})