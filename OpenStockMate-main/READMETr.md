# OpenStockMate.org

OpenStockMate, açık kaynaklı ve özgür bir komponent stok takip uygulamasıdır.

## Hakkında

Bu proje, [mekatronik.org/forum](https://mekatronik.org/forum/) adresindeki forum topluluğu tarafından geliştirilmektedir. Amaç, kullanıcıların elektronik komponent stoklarını etkili bir şekilde yönetmelerini sağlamaktır.

## Özellikler

- Komponent stok yönetimi
- Komponent stok uyarı e-maili
- Kayıt e-mail
- her kullanıcının ayrı stok sayfası
- 180 gün şifre süresi
- 8 karakter büyü küçük harf duyarlılığı
- aktivasyon e-maili
  

## Kurulum

1. Projeyi bilgisayarınıza klonlayın.
    ```bash
    git clone https://github.com/CodeWizardette/OpenStockMate.git
    ```

2. Proje dizinine gidin.
    ```bash
    cd OpenStockMate
    ```

3. Gerekli bağımlılıkları yükleyin.
    ```bash
    # Gerekirse sanal ortamı oluşturun
    python -m venv venv
    # Sanal ortamı etkinleştirin
    source venv/bin/activate   # Linux
    venv\Scripts\activate       # Windows

    # Gerekli paketleri yükleyin
    pip install -r requirements.txt
    ```

4. Veritabanını oluşturun ve uygulamayı başlatın.
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. Tarayıcınızda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) adresine gidin.

## Katkıda Bulunma

Eğer projeye katkıda bulunmak istiyorsanız, lütfen bulunun.:)

## Lisans

Bu proje [MIT Lisansı] altında lisanslanmıştır. 
