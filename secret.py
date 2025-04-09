import urequests

WIFI_SSID = 'Wifiのアクセスポイント'
WIFI_PASSWORD = 'Wifiのパスワード'
GOOGLE_CLIENT_ID = "クライアントID"
GOOGLE_REFRESH_TOKEN = "refresh_token"
GOOGLE_CALENDAR_ID = "カレンダーID"

def get_google_refresh_token():

    url = 'https://192.168.0.1/cal5.83/token.dat'   # リフレッシュトークンをローカルネットワークから取得できるようにした場合
    response = urequests.get(url)
    token = response.text
    response.close()

    return token