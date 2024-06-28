import keyboard

def main():
    print("Pressione as teclas (Pressione 'Esc' para sair):")
    
    with open('captura.txt', 'w') as arquivo:
        arquivo.write("Teclas pressionadas:\n")
        
        while True:
            try:
                # Captura a próxima tecla pressionada
                event = keyboard.read_event()
                
                # Verifica se a tecla Esc foi pressionada para sair
                if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
                    print("Saindo...")
                    break
                
                # Ignora eventos de tecla 'Ctrl'
                if event.event_type == keyboard.KEY_DOWN and not event.name.startswith('ctrl'):
                    # Obtém a tecla pressionada
                    tecla = event.name
                    
                    # Verifica se é a tecla Caps Lock
                    if tecla == 'caps lock':
                        continue  # Pula para a próxima iteração do loop
                    
                    # Converte a tecla para maiúscula se Caps Lock estiver ativo
                    if keyboard.is_pressed('caps lock'):
                        tecla = tecla.upper()
                    else:
                        tecla = tecla.lower()
                    
                    # Ajusta o espaço para ser registrado como espaço em branco no arquivo
                    if tecla == 'space':
                        tecla = ' '
                    
                    print(f"Tecla pressionada: {tecla}")
                    
                    # Escreve a tecla no arquivo
                    arquivo.write(tecla)
            
            except KeyboardInterrupt:
                pass  # Ignora o KeyboardInterrupt para que 'q' não pare o programa

if __name__ == "__main__":
    main()
