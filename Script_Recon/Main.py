import nmap
import subprocess
import time

nm = nmap.PortScanner()
target_ip = input ('insert ip: ')
line = '='*10


scan_result = nm.scan (f'{target_ip}', arguments= '-T4') #Caso queira testar um range de portas: (f'{target_ip}', '1-10000')

for host in nm.all_hosts():
    print(f"\nHost: {host} ({nm[host].hostname()})")
    print("State: up" if nm[host].state() == "up" else "State: down")
    
    for proto in nm[host].all_protocols():
        print(f"\nProtocol: {proto}")
        
        for port in nm[host][proto]:
            state = nm[host][proto][port]['state']
            service = nm[host][proto][port].get('name', 'Unknown')
            print(f"Port: {port}\tState: {state}\tService: {service}\tProtocol: {proto}")

print(line)
print('executando o go buster...')
print(line)
time.sleep(5)

def run_gobuster(protocol):
    command = f"gobuster dir -u {protocol}://{target_ip} -w /path/to/wordlist.txt" #Adicione o caminho da sua wordlist de preferencia
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

for protocol in ["http", "https"]:
    result = run_gobuster(protocol)
    if result.returncode == 0:
        print(f"{protocol.upper()} executado com sucesso:\n{result.stdout}")
        break  
    else:
        print(f"Erro ao executar {protocol.upper()}:\n{result.stderr}")

