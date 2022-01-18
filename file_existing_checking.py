from os.path import exists


def main():
    path = 'D:\Code\Sirius\sirius21-cv\README.md'  # эту строчку можно изменять для тестирования программы

    # Начало кода решения

    existing = exists(path)

    if not existing:
        print('Invalid file path. Type correct path.')
        exit()

    # Конец кода решения

    print("File exists. Path OK")  # эту строчку перемещать и изменять нельзя


if __name__ == "__main__":
    main()
