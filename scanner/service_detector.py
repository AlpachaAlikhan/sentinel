import socket


COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
}


def detect_service(
        target: str,
        port: int,
        timeout: float = 1.0
) -> tuple[str | None, str | None]:

    service = COMMON_SERVICES.get(port)

    banner = None

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((target, port))

            if port in (80, 8080, 8000):
                request = (
                    "HEAD / HTTP/1.0\r\n"
                    f"Host: {target}\r\n"
                    "Connection: close\r\n\r\n"
                )

                sock.sendall(request.encode())

            else:
                try:
                    banner = sock.recv(1024).decode(
                        errors="ignore"
                    ).strip()
                except socket.timeout:
                    pass

    except(socket.timeout, OSError):
        pass

    return service, banner