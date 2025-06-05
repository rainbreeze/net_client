import socket

SERVER_IP = "172.31.90.54"
SERVER_PORT = 12345  # 서버에서 열어둔 포트


def main():
    # 1. 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[*] 서버에 연결 시도 중...")

    try:
        # 2. 서버에 연결 (connect() 호출)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("[+] 연결 성공!")

        # 3. 사용자 입력 (소문자 문자열)
        message = input("서버로 보낼 소문자 문자열 입력: ").strip()

        # 4. 문자열 전송
        client_socket.sendall(message.encode("utf-8"))

        # 5. 응답 수신
        response = client_socket.recv(1024).decode("utf-8")
        print(f"[<] 서버 응답: {response}")

    except Exception as e:
        print(f"[!] 오류 발생: {e}")
    finally:
        client_socket.close()
        print("[*] 연결 종료")


# 🔧 이 부분이 잘못 쓰였던 걸 수정
if __name__ == "__main__":
    main()
