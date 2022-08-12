from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import JsonResponse
from test2.models import DataModel


def test1(request):
    if request.method == "POST":
        data = DataModel.objects.get(name="test1")
        data.text += mark_safe(request.POST['text'])
        data.save()
        return JsonResponse({"nice": 1})
    else:
        data = DataModel.objects.get(name="test2")
        text = data.text
        data.text = ''
        data.save()
        return JsonResponse({"text": text})

def page(request):
    return render(request, 'page.html')

#for other client
def test2(request):
    if request.method == "POST":
        data = DataModel.objects.get(name="test2")
        data.text += mark_safe(request.POST['text'])
        data.save()
        return JsonResponse({"nice": 1})
    else:
        data = DataModel.objects.get(name="test2")
        text = data.text
        data.text = ''
        data.save()
        return JsonResponse({"text": text})