import requests

def bot_izin_kontrol(url):
    try:
        # Robots.txt dosyasını kontrol et
        robots_txt_url = f"{url}/robots.txt"
        response = requests.get(robots_txt_url)
        
        if response.status_code == 200:
            print(f"Robots.txt:\n{response.text}")
        else:
            print("Robots.txt bulunamadı.")

    except requests.RequestException as e:
        print(f"Hata: {e}")

url = "https://mekatronik.org/"
bot_izin_kontrol(url)
