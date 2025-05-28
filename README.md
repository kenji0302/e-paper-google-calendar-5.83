# Google Calendar を Raspberry Pi Pico W と e-paer で表示する

![image](https://github.com/user-attachments/assets/1bd21008-3e45-4cf5-a171-41055b5159a4)
（左はサイズ比較用の Raspberry Pi Pico W）

## e-paper描画ライブラリについて

[Pico_ePaper_Code/python/Pico-ePaper-5.83-B.py at main · waveshareteam/Pico_ePaper_Code](https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico-ePaper-5.83-B.py) を元に一部修正したものをレポジトリに含めています。


## 準備

### 必要なもの

- [Raspberry Pi Pico WH — スイッチサイエンス](https://www.switch-science.com/products/8172?_pos=1&_sid=5aa1a1afe&_ss=r)
- [Raspberry Pi Pico用 5.83インチ e-Paper ディスプレイ（白黒赤）648×480 — スイッチサイエンス](https://www.switch-science.com/products/7319)

### なくても良いけどあると便利なもの

- [Amazon.co.jp: オーディオファン 電池ボックス USB出力対応 ON/OFF スイッチ付き USB-A メス 単3電池 4本 1.5V 6V (1.2V 4.8V) 単三電池 出力用 ケース : 産業・研究開発用品](https://www.amazon.co.jp/dp/B0B4W7Z1ML)
- [Amazon.co.jp: オーディオファン microUSB 短い ケーブル 両端子 L字 約12cm L字パターン2 ブラック AFSSLCBL : パソコン・周辺機器](https://www.amazon.co.jp/dp/B091GL481V?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_2&th=1)

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
