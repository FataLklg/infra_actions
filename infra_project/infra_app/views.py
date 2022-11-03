from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'У меня получилось! В сотый то раз не могло не получиться)'
    )


def second_page(request):
    return HttpResponse('А это вторая страница!')
