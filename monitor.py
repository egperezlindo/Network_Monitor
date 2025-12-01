import subprocess
import platform
import datetime

def hacer_ping(host):
    # Detectamos SO: Windows usa '-n', el resto '-c'
    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Armamos el comando como lista para subprocess
    comando = ['ping', parametro, '1', host]
    
    try:
        # Ejecutamos en silencio (mandamos la salida a la basura)
        respuesta = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Si el código es 0, respondió bien
        return respuesta.returncode == 0
    except Exception:
        return False
    

def test_pings():
    archivo_hosts = "servidores.txt"
    try:
        with open(archivo_hosts, "r") as f:
            lista_hosts = f.readlines()

        for host in lista_hosts:
            host = host.strip() # Limpiamos espacios y saltos de línea
            if not host: continue # Si la línea está vacía, pasamos

            if hacer_ping(host):
                print(f"{host:<25} [ ONLINE  ] 🟢")
            else:
                print(f"{host:<25} [ OFFLINE ] 🔴")
                
    except FileNotFoundError:
        print(f"❌ No encontré '{archivo_hosts}'. Créalo primero.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

       

def main():
    
    
    print(f"\n--- 🔎 MONITOR DE RED: {datetime.datetime.now().strftime('%H:%M:%S')} ---")
    print(f"{'HOST':<25} {'ESTADO'}")
    print("-" * 40)

    test_pings()

  
if __name__ == "__main__":
    main()


