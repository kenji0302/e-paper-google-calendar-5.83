# Google Calendar を Raspberry Pi Pico W と e-paer で表示する

![image](https://github.com/user-attachments/assets/47391cf4-f2a1-41b3-94cd-7e46241f52a3)
（左はサイズ比較用の Raspberry Pi Pico W）

## e-paper描画ライブラリについて

[Pico_ePaper_Code/python/Pico-ePaper-5.83-B.py at main · waveshareteam/Pico_ePaper_Code](https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico-ePaper-5.83-B.py) を元に一部修正したものをレポジトリに含めています。


## 準備

### 必要なもの

- [Raspberry Pi Pico WH — スイッチサイエンス](https://www.switch-science.com/products/8172?_pos=1&_sid=5aa1a1afe&_ss=r)
- [Raspberry Pi Pico用 5.83インチ e-Paper ディスプレイ（白黒赤）648×480 — スイッチサイエンス](https://www.switch-science.com/products/7319)


## 追加するコード

日本語フォント（24pxのみ）。設置方法などは以下を参照。
[Raspberry Pi Pico W で e-paper に日本語を表示する その2（大きめのフォント表示） #micropython - Qiita](https://qiita.com/kenji0302/items/8da4c075dff974d1dc6f)


## 編集が必要なファイル

- secret.php
- secret.py

## Google の TOKEN 取得

```bash
mkdir data
php -S 0.0.0.0:8080
```

<http://localhost:8080> から Google 認証、REFRESH TOKENの取得 でテキストボックスに表示される。
