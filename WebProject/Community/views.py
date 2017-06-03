from django.shortcuts import render
from Community.forms import *
import logging

# Create your views here.
logger = logging.getLogger('logger')

def f_write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            logger.error('error')
    else:
        form = Form()

    print('print test')
    return render(request, 'write.html', {'v_form':form})

def f_list(request):
    dtoList = Dto.objects.all()
    return render(request, 'list.html', {'v_dtoList': dtoList})

def f_view(request, num="1"):
    dto = Dto.objects.get(id=num)
    return render(request, 'view.html', {'v_dto': dto})