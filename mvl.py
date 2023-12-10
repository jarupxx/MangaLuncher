import os
import sys
import subprocess
from functools import cmp_to_key
import winreg
from ctypes import windll

app_path = "C:\\path\\to\\your\\viewer.exe"
image_extensions = ['.avif', '.bmp', '.gif', '.heic', '.jpeg', '.jpg', '.png', '.webp']

def natural_sort_cmp(a, b):
    # StrCmpLogicalW 関数を使用して、自然順ソートのための比較関数を作成する
    cmp_func = windll.Shlwapi.StrCmpLogicalW
    return cmp_func(a, b)

def select_file(file_path):
    try:
        folder_path = os.path.dirname(file_path)

        image_files = [file for file in os.listdir(folder_path) if is_image_file(file)]
        sorted_image_files = sorted(image_files, key=cmp_to_key(natural_sort_cmp))

        file_index = sorted_image_files.index(os.path.basename(file_path))

        if file_index % 2 == 0:
            open_file_path = file_path
        else:
            if file_index > 0:
                open_file_path = os.path.join(folder_path, sorted_image_files[file_index - 1])

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    return open_file_path

def is_image_file(file_path):
    return any(file_path.lower().endswith(ext) for ext in image_extensions)

def check_policy():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                     r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer")
    name = "NoStrCmpLogical"
    try:
        value, _ = winreg.QueryValueEx(key, name)
        if value == 1:
            print("Unsupported policy setting:\nTurn off numerical sorting in File Explorer 'NoStrCmpLogical'.")
            input("Press any key to exit.")
            sys.exit()
    except FileNotFoundError:
        pass

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                     r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer")
    name = "NoStrCmpLogical"
    try:
        value, _ = winreg.QueryValueEx(key, name)
        if value == 1:
            print("Unsupported policy setting:\nTurn off numerical sorting in File Explorer 'NoStrCmpLogical'.")
            input("Press any key to exit.")
            sys.exit()
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    check_policy()

    if not os.path.exists(app_path):
        print("最初にmvl.pyのapp_pathとimage_extensionsをアプリのパスと対応拡張子に書き換えてください。", "\napp_path =", app_path, "\nimage_extensions =", image_extensions)
        sys.exit()
    if len(sys.argv) != 2:
        print('使用方法: mvl.py "C:\\path\\image001.jpg"')
    else:
        file_path = sys.argv[1]
        open_file_path = file_path
        if not os.path.exists(file_path):
            print("指定されたファイルが存在しません。")
        else:
            if is_image_file(file_path):
                open_file_path = select_file(file_path)
            subprocess.Popen([app_path, open_file_path])
