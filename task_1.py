import os
import shutil
import argparse

def copy_files(src, dest):
    try:
        for item in os.listdir(src):
            path = os.path.join(src, item)
            if os.path.isdir(path):
                # Рекурсивний виклик для піддиректорій
                copy_files(path, dest)
            else:
                file_extension = os.path.splitext(item)[1][1:]  # Отримання розширення файлу
                extension_dir = os.path.join(dest, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)
                shutil.copy(path, extension_dir)
    except Exception as e:
        print(f"Помилка при обробці директорії {src}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Рекурсивно копіює файли за типами у вказану директорію.')
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('-d', '--dest_dir', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist")')
    
    args = parser.parse_args()

    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)

    copy_files(args.src_dir, args.dest_dir)

if __name__ == "__main__":
    main()