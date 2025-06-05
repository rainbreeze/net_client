import socket

SERVER_IP = "172.31.90.54"
SERVER_PORT = 12345  # 서버에서 열어둔 포트

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(command.encode('utf-8'))
        
        response = s.recv(1024).decode('utf-8')
        print(f"[서버 응답] {response}")

def main():
    print("=== 도메인 등록/조회 클라이언트 ===")
    print("명령어 예시:")
    print("  등록: write example.com 1.2.3.4")
    print("  조회: read example.com")
    print("종료하려면 'exit' 입력")
    
    while True:
        cmd = input("명령 입력: ").strip()
        if cmd.lower() == 'exit':
            break
        if not cmd:
            continue
        
        send_command(cmd)

if __name__ == "__main__":
    main()
