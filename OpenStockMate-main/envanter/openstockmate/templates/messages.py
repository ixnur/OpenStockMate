from django.contrib import messages

def add_stock_alert(request):
    if request.method == 'POST':
        # Form işlemleri burada yapılır

        # Stok alarmı başarıyla eklendiğinde mesaj eklenir
        messages.success(request, 'Stok alarmı başarıyla eklendi.')

        # Diğer işlemler ve yönlendirme

    return render(request, 'profil.html', context)
