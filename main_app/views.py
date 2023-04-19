from django.shortcuts import render

def kitchen_form(request):
    if request.method == 'POST':
        type = request.POST.get("q1", "")
        print(type)
        size = request.POST.get("q2", "")
        print(size)
        style = request.POST.get("q3", "")
        print(style)
        fasad = request.POST.get("q4", "")
        print(fasad)
        stoleshnica = request.POST.get("q5", "")
        print(stoleshnica)
        budget = request.POST.get("q7", "")
        print(budget)
        furnitura = request.POST.get("q6", "")
        print(furnitura)
        height = request.POST.get("q0", "")
        print(height)
        name = request.POST.get("name", "")
        print(name)
        phone = request.POST.get("phone", "")
        print(phone)
        comment = request.POST.get("comment", "")
        print(comment)


def home(request):
    return render(request, 'main_app/main.html')
