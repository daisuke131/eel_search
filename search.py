import os

import eel

READ_CSV_PATH = os.path.join(os.getcwd(), "csv/character.csv")
WRITE_CSV_PATH = os.path.join(os.getcwd(), "csv/{csv_name}.csv")


def search(csv_name: str, search_word: str):
    # CSV読み込み
    characters = read_csv()
    if search_word in characters:
        print(f"{search_word}が見つかりました。")
        eel.output_logs(f"{search_word}が見つかりました。")
    else:
        characters.append(search_word)
        print("リストに存在しなかったので追加しました。")
        eel.output_logs("リストに存在しなかったので追加しました。")
        # CSV書き込み
        write_csv(characters, csv_name)


def read_csv():
    with open(READ_CSV_PATH, encoding="utf_8_sig") as f:
        read_csv_str = f.read()
        return read_csv_str.split(",")


def write_csv(characters: str, csv_name: str):
    write_csv_path = WRITE_CSV_PATH.format(csv_name=csv_name)
    with open(write_csv_path, mode="w", encoding="utf_8_sig") as f:
        f.write(",".join(characters))
