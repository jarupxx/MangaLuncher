# MangaViewerLuncher
## 概要
見開き漫画ビューア用ランチャー

偶数ページを開くとページの割り当てが逆になる問題を解決するために、画像の関連付けを調整するランチャーを作りました。

最初にmvl.pyのここをアプリのパスと対応拡張子に書き換えてください。

```app_path = "C:\\path\\to\\your\\viewer.exe"```

```image_extensions = ['.avif', '.bmp', '.gif', '.heic', '.jpeg', '.jpg', '.png', '.webp']```

## 使用方法

[Default Programs Editor](https://defaultprogramseditor.com/)で関連付けを変更してください。

```"C:\Users\you\AppData\Local\Programs\Python\Python3xx\pythonw.exe" "C:\MangaLuncher\mvl.py" "%1"```

![defaultprogramseditor](https://github.com/jarupxx/MangaLuncher/assets/20138367/1d9c65be-3271-464f-8221-04c6d74e9d04)

## 見開き方向を調整するランチャー

https://github.com/jarupxx/MangaLuncher/tree/ltr_settings
