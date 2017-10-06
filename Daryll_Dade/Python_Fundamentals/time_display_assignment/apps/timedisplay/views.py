  from django.shortcuts import render, HttpResponse

  def firstview(request):
    context = {
    "somekey":"somevalue"
    }

    return render(request,'page.html', context)
