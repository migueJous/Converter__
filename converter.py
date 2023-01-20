from pydub import AudioSegment
import time, os
from colorama import Fore


_Entrar = True

def _mp3Awav():
    _RutaDelAudio = input("Ingresa la ruta del audio, con su respectiva extencion: ")
    _GuardarEn = input("""
    Ingrese la ruta donde desea guardar el archivo,
    con su respectiva extencion segun vaya a convertir: """)
    _Audio = AudioSegment.from_mp3(f"{_RutaDelAudio}")
    _Audio.export(f"{_GuardarEn}", format='wav')
    time.sleep(2)
    print("Convirtiendo...")
    time.sleep(1.5)
    input("Terminado, presione enter para volver")

def _mp3Aogg():
    _RutaDelAudio = input("Ingresa la ruta del audio, con su respectiva extencion: ")
    _GuardarEn = input("""
    Ingrese la ruta donde desea guardar el archivo,
    con su respectiva extencion segun vaya a convertir: """)
    _Audio = AudioSegment.from_mp3(f"{_RutaDelAudio}")
    _Audio.export(f"{_GuardarEn}", format='ogg')
    time.sleep(2)
    print("Convirtiendo...")
    time.sleep(1.5)
    input("Terminado, presione enter para volver")

def _wavAmp3():
    _RutaDelAudio = input("Ingresa la ruta del audio, con su respectiva extencion: ")
    _GuardarEn = input("""
    Ingrese la ruta donde desea guardar el archivo,
    con su respectiva extencion segun vaya a convertir: """)
    _Audio = AudioSegment.from_wav(f"{_RutaDelAudio}")
    _Audio.export(f"{_GuardarEn}", format='mp3')
    time.sleep(2)
    print("Convirtiendo...")
    time.sleep(1.5)
    input("Terminado, presione enter para volver")

def _wavAogg():
    _RutaDelAudio = input("Ingresa la ruta del audio, con su respectiva extencion: ")
    _GuardarEn = input("""
    Ingrese la ruta donde desea guardar el archivo,
    con su respectiva extencion segun vaya a convertir: """)
    _Audio = AudioSegment.from_wav(f"{_RutaDelAudio}")
    _Audio.export(f"{_GuardarEn}", format='ogg')
    time.sleep(2)
    print("Convirtiendo...")
    time.sleep(1.5)
    input("Terminado, presione enter para volver")

def _oggAmp3():
    _RutaDelAudio = input("Ingresa la ruta del audio, con su respectiva extencion: ")
    _GuardarEn = input("""
    Ingrese la ruta donde desea guardar el archivo,
    con su respectiva extencion segun vaya a convertir: """)
    _Audio = AudioSegment.from_ogg(f"{_RutaDelAudio}")
    _Audio.export(f"{_GuardarEn}", format='mp3')
    time.sleep(2)
    print("Convirtiendo...")
    time.sleep(1.5)
    input("Terminado, presione enter para volver")

def _oggAwav():
    _RutaDelAudio = input("Ingresa la ruta del audio, con su respectiva extencion: ")
    _GuardarEn = input("""
    Ingrese la ruta donde desea guardar el archivo,
    con su respectiva extencion segun vaya a convertir: """)
    _Audio = AudioSegment.from_ogg(f"{_RutaDelAudio}")
    _Audio.export(f"{_GuardarEn}", format='wav')
    time.sleep(2)
    print("Convirtiendo...")
    time.sleep(1.5)
    input("Terminado, presione enter para volver")

while _Entrar:
    os.system("clear")
    print(Fore.BLUE + """
    **********************
    ──▄────▄▄▄▄▄▄▄────▄───
    ─▀▀▄─▄█████████▄─▄▀▀──
    ─────██─▀███▀─██──────
    ───▄─▀████▀████▀─▄────
    ─▀█────██▀█▀██────█▀──
    ----------------------
    > creador: migueJous
    > script: Converter
    > github del creador: https://github.com/migueJous
    **********************
    """)
    print("""
             .:Menu:.
    [01] Extraer audio de video
    [02] Convertir audio a varios formatos
    [99] Salir
    """)
    _SeleccionPrincipal = int(input("Seleccione una opcion: "))
    if _SeleccionPrincipal == 1:
        os.system("clear")
        print("""\t!Si se ingresa una ruta no valida el programa podria fallar,
        asegurese que las rutas y los archovos esten correctos""")
        _RutaVideo = input("\tRuta del video (ejemplo: /home/user/videos/video264.mp4): ")
        print("Leyendo archivo...")
        time.sleep(3)
        _RutaDeGuardado = input("""\tIngrese la ruta donde desea guardar el archivo,
        con el nombre que desea darle (Ejemplo: /home/user/videos/prueba.mp3): """)
        AudioSegment.from_file(_RutaVideo).export(f"{_RutaDeGuardado}", format='mp3')
        time.sleep(2)
        print("El proceso de extraccion demorara segun el tamaño del video...")
        print("Extrayendo audio...")
        time.sleep(2)
        input("Extraccion finalizada! presione enter para volver...")
    
    elif _SeleccionPrincipal == 2:
        os.system("clear")
        print("!Asegurate de escribir bien las rutas y las extenciones de los archivos")
        print("""
        [01] Convertir mp3 a wav 
        [02] Convertir mp3 a ogg 
        [03] Convertir wav a mp3 
        [04] Convertir wav a ogg 
        [05] Convertir ogg a mp3 
        [06] Convertir ogg a wav 
        [99] Salir
        """)
        _TipoDeConversion = int(input("Escoja una opcio: "))
        if _TipoDeConversion == 1:
            _mp3Awav()
        elif _TipoDeConversion == 2:
            _mp3Aogg()
        elif _TipoDeConversion == 3:
            _wavAmp3()
        elif _TipoDeConversion == 4:
            _wavAogg()
        elif _TipoDeConversion == 5:
            _oggAmp3()
        elif _TipoDeConversion == 6:
            _oggAwav()

    elif _SeleccionPrincipal == 99:
        _Entrar = False
        print("Script finalizado...")

    else:
        input("Opcion no valida!! Presiona enter para volver...")
