import time
import webbrowser

try:
    import pyautogui
except ImportError:
    pyautogui = None


def abrir_com_pyautogui(urls):
    if pyautogui is None:
        return False

    pyautogui.PAUSE = 0.5

    for url in urls:
        pyautogui.hotkey("ctrl", "t")
        time.sleep(0.5)
        pyautogui.write(url)
        pyautogui.press("enter")
        time.sleep(1)

    return True


def abrir_com_webbrowser(urls):
    for url in urls:
        ok = webbrowser.open(url, new=1)
        print(f"Abrindo {url}: {'OK' if ok else 'falhou'}")
        time.sleep(0.5)


if __name__ == "__main__":
    urls = ["https://www.example.com", "https://www.linkedin.com"]

    print("Iniciando automação...")

    if abrir_com_pyautogui(urls):
        print("Automação executada com pyautogui.")
    else:
        print("pyautogui não disponível; usando o navegador padrão como fallback.")
        abrir_com_webbrowser(urls)

    print("Processo finalizado.")

