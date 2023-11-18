from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , HttpResponse
from Calculator.forms import AddNumbersForm
# Create your views here.


def Home(request):
    form = AddNumbersForm()
    result = None

    if request.method == 'POST':
        form = AddNumbersForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            result =num1 + num2

    return render(request, 'base.html', {'form': form, 'result': result})
