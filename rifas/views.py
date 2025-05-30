from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rifas.models import NumeroRifa

def home(request):
    return render(request, 'home.html')

@staff_member_required
def criar_numeros(request):
    criados = 0
    for i in range(1681, 1801):
        obj, created = NumeroRifa.objects.get_or_create(numero=i)
        if created:
            criados += 1
    return HttpResponse(f'{criados} números criados com sucesso!')

@login_required
def lista_rifa(request):
    if request.method == "POST":
        # Atualizar nomes e status de pagamento
        for numero_obj in NumeroRifa.objects.all():
            nome = request.POST.get(f'nome_{numero_obj.numero}', '').strip()
            pago = request.POST.get(f'pago_{numero_obj.numero}') == 'on'
            numero_obj.nome = nome
            numero_obj.pago = pago
            numero_obj.save()
        return redirect('lista_rifa')

    numeros = list(NumeroRifa.objects.all().order_by('numero'))
    # Quebrar em grupos de 20
    grupos = [numeros[i:i+20] for i in range(0, len(numeros), 20)]

    return render(request, 'rifas/lista_rifa.html', {'grupos': grupos})
