import urequests, ntptime, time, machine, sys
from cal import jst_ymd, wifi_connect, refresh_access_token, jpredtext, jpblacktext, jst_today_ymdhms_for_api, jst_ymdhms_str, jst_str_to_ymdw
from Pico_ePaper_5_83_B import EPD_5in83_B
from mfont import mfont
from secret import WIFI_SSID, WIFI_PASSWORD,GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_CALENDAR_ID, get_google_refresh_token
from machine import Pin

def main():

    # 処理が始まるとbusyになってしまうので、開発用のコンソール接続の余裕といて5秒待つ
    time.sleep(5)

    led = machine.Pin('LED', Pin.OUT)
    led.value(1)
    
    while True:

        machine.Pin(23, machine.Pin.OUT).high()

        # 画面表示
        epd = EPD_5in83_B()
        epd.Clear(0xff, 0x00)
        epd.imageblack.fill(0xff)
        epd.imagered.fill(0x00)

        mf = mfont()
        mf.setFontSize(24)

        led.value(0)
        time.sleep(0.2)
        led.value(1)

        error_count = 0
        while True:
            try:
                # Wifi接続
                wlan = wifi_connect(WIFI_SSID, WIFI_PASSWORD)
                # NTPで時間セット
                ntptime.settime()
                break
            except Exception as e:
                error_count += 1
                print("ネットワーク例外 : ", e)
                time.sleep(5)
                if error_count >= 3:
                    jpredtext("ネットワークに問題が発生しました、リセットします。", 5, 10, mf, epd)
                    epd.display(epd.buffer_black, epd.buffer_red)
                    epd.delay_ms(2000)
                    machine.reset()

        led.value(0)
        time.sleep(0.2)
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)
        led.value(1)

        # ymd取得
        ymd = jst_ymd()
        # データ更新日表示
        epd.imageblack.text("Updated at : " + jst_ymdhms_str(), 370, 473, 0x00)

        # カレンダー取得
        access_token = refresh_access_token(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, get_google_refresh_token())

        led.value(0)
        time.sleep(0.2)
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)
        led.value(1)

        # deepsleep1時間
        sleep_msec = 3600000
        if access_token is None:
            jpredtext("カレンダーにアクセス出来ません。", 30, 10, mf, epd)
            jpredtext("トークンを更新してください。", 30, 35, mf, epd)
        else:

            calendar_id = "primary"

            ymdhms = jst_today_ymdhms_for_api() 
            
            url = "https://www.googleapis.com/calendar/v3/calendars/" + GOOGLE_CALENDAR_ID + "/events?maxResults=13&timeMin=" + ymdhms + "&orderBy=startTime&singleEvents=True&timeZone=JST"

            headers = {
                "Authorization": "Bearer " + access_token
            }

            response = urequests.get(url, headers=headers)

            if response.status_code == 200:

                events = response.json().get('items', [])            
                
                y = 10
                i = 0
                
                for event in events:
                    if 'date' in event['start']:
                        event_ymd = event['start']['date'][0:4] + event['start']['date'][5:7] + event['start']['date'][8:10]
                        event_str = jst_str_to_ymdw(event['start']['date']) + ' ' + event['summary']
                        print(event_str)
                    elif 'dateTime' in event['start']:
                        event_ymd = event['start']['dateTime'][0:4] + event['start']['dateTime'][5:7] + event['start']['dateTime'][8:10]
                        event_str = jst_str_to_ymdw(event['start']['dateTime'][0:10]) + event['start']['dateTime'][11:16] + ' ' + event['summary']
                        print(event_str)
                    
                    if event_ymd == ymd:
                        jpredtext(event_str, 30, y, mf, epd)
                    else:
                        jpblacktext(event_str, 30, y, mf, epd)
                    y = y + 37
            else:
                print("Failed to retrieve events:", response.status_code, response.text)

        epd.display(epd.buffer_black, epd.buffer_red)
        # sys.exit()
        print("deepsleep")
        
        # time.sleep_ms(sleep_msec)
        machine.Pin(23, machine.Pin.OUT).low()
        machine.deepsleep(sleep_msec)


if __name__=='__main__':
    main()