from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from .models import KitchenRequest
import requests


def kitchen_form(request):
    if request.method == 'POST':
        type = request.POST.get("q1", "")
        size = request.POST.get("q2", "")
        style = request.POST.get("q3", "")
        fasad = request.POST.get("q4", "")
        stoleshnica = request.POST.get("q5", "")
        furnitura = request.POST.get("q6", "")
        height = request.POST.get("q0", "")
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        comment = request.POST.get("comment", "")
        contact = request.POST.get("contact", "")
        print(contact)
        try:
            k_request = KitchenRequest(
                type=type,
                size=size,
                style=style,
                fasad=fasad,
                stoleshnica=stoleshnica,
                furnitura=furnitura,
                height=height,
                name=name,
                phone=phone,
                comment=comment,
                contact=contact
            )
        except Exception:
            print('error while creating KitchenRequest')
        else:
            k_request.save()
        
        bot_token = settings.BOT_TOKEN
        chat_id = settings.CHAT_ID
        base_url = 'https://api.telegram.org/bot'
        url = base_url + bot_token + '/sendMessage'
        contact = "Позвонить" if contact == "call" else 'Написать'
        text = 'Новый запрос на подсчет стоимости\n\n' \
                f'**Тип**: {type}\n' \
                f'**Высота**: {height}\n' \
                f'**Размер**: {size}\n' \
                f'**Стиль**: {style}\n' \
                f'**Фасад**: {fasad}\n' \
                f'**Столешница**: {stoleshnica}\n' \
                f'**Фурнитура**: {furnitura}\n' \
                f'**Имя**: {name}\n' \
                f'**Телефон**: {phone}\n' \
                f'**Комментарий**: {comment}\n' \
                f'**Как связаться**: {contact}\n'
        print(text)
        params = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'markdown'
        }
        resp = ''
        try:
            resp = requests.get(url, params=params)
        except Exception:
            print('error while sending message to telegram')
        print(resp.status_code, resp.text)
        return render(request, 'main_app/done_kitchen.html', context={'success': True if resp.status_code == 200 else False})



def home(request):
    return render(request, 'main_app/main.html')

