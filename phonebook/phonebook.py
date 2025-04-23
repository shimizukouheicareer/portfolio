import pickle
import os

PHONEBOOK_FILE = 'phonebook.pkl'

def load_phonebook():
    """電話帳をpickleから復元"""
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_phonebook(phonebook):
    """電話帳をpickleへ書き出し"""
    with open(PHONEBOOK_FILE, 'wb') as f:
        pickle.dump(phonebook, f)

def display_menu():
    """メインメニューを表示"""
    print('''
番号を入力してください。
1: 電話番号を検索
2: 電話番号を登録
3: 電話番号を削除
4: 電話番号を一覧表示
0: プログラムの終了
-> ''', end='')

def search_phone(phonebook):
    """検索コマンド"""
    name = input("検索する名前を入力してください: ")
    if name in phonebook:
        print(f"{name}の電話番号は {phonebook[name]} です")
    else:
        print(f"{name}は登録されていません")

def register_phone(phonebook):
    """登録コマンド"""
    name = input("登録する名前を入力してください: ")
    phone = input("登録する電話番号を入力してください: ")
    if not phone.isdigit():
        print("不適切な電話番号です。数字のみを入力してください。")
        return
    phonebook[name] = phone
    print(f"{name}を登録しました")

def delete_phone(phonebook):
    """削除コマンド"""
    name = input("削除する名前を入力してください: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name}を削除しました")
    else:
        print(f"{name}は登録されていません")

def list_phones(phonebook):
    """一覧コマンド"""
    if phonebook:
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("電話帳は空です")

def main():
    phonebook = load_phonebook()
    while True:
        display_menu()
        choice = input().strip()
        if choice.isdecimal():
            cmd = int(choice)
            if cmd == 1:
                search_phone(phonebook)
            elif cmd == 2:
                register_phone(phonebook)
            elif cmd == 3:
                delete_phone(phonebook)
            elif cmd == 4:
                list_phones(phonebook)
            elif cmd == 0:
                save_phonebook(phonebook)
                print("プログラムを終了します")
                break
            else:
                print("不適切な選択です。もう一度試してください")
        else:
            print("コマンド番号を入力してください")

if __name__ == "__main__":
    main()
