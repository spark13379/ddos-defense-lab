import psutil
import time

def monitor():
    print("Monitorando sistema... (CTRL+C para sair)\n")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        print(f"CPU: {cpu}% | RAM: {ram}%")

if __name__ == "__main__":
    monitor()