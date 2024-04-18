import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import glob
import logging

# ロギング設定
logging.basicConfig(filename="delete_files.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def delete_files(folder_path, extension):
    # 指定された拡張子のファイルを検索
    pattern = os.path.join(folder_path, '**', f'*.{extension}')
    files = glob.glob(pattern, recursive=True)
    num_deleted = 0
    
    for file in files:
        try:
            os.remove(file)
            logging.info(f"Deleted: {file}")
            print(f"Deleted: {file}")
            num_deleted += 1
        except PermissionError:
            logging.error(f"Permission denied: {file}")
            print(f"Permission denied: {file}")
        except FileNotFoundError:
            logging.error(f"File not found: {file}")
            print(f"File not found: {file}")
        except OSError as e:
            logging.error(f"Error deleting {file}: {e}")
            print(f"Error deleting {file}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error deleting {file}: {e}")
            print(f"Unexpected error deleting {file}: {e}")
    return num_deleted

def main():
    root = tk.Tk()
    root.withdraw()  # Tkのルートウィンドウを非表示

    # ユーザーにフォルダを選択させる
    folder_path = filedialog.askdirectory()
    
    if not folder_path:
        print("No folder selected. Exiting...")
        return
    
    # 拡張子の入力をユーザーに促す (GUIを通じて)
    extension = simpledialog.askstring("Input", "Enter the file extension to delete (e.g., 'txt'):")
    if not extension:
        print("No extension provided. Exiting...")
        return
    
    # ファイル削除の実行
    num_deleted = delete_files(folder_path, extension)
    
    # 完了メッセージの表示
    messagebox.showinfo("Complete", f"Process complete. {num_deleted} files deleted.")

if __name__ == "__main__":
    main()
