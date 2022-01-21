from django.shortcuts import render
import json
from django.http import HttpResponse

# test
def IndexView(request):
  # template = "vue_index.html"

  # if request.method == "POST":
  #     get_data = request.GET.get("info")
  #     post_data = json.loads(request.body).get("info")
  #     return JsonResponse({'get_data': get_data, 'post_data': post_data})

  # context = {
  #     'django': "This is Django text.",
  #   }

  return HttpResponse("Hello World")
