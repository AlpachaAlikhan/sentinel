import socket
from concurrent.futures import ThreadPoolExecutor

from models.scan_results import ScanResult



def scan_port(target: str, port: int, timeout: float = 1.0) -> ScanResult:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))

            if result == 0:
                state = "OPEN"
            else: 
                state = "CLOSED"

    except socket.timeout:
        state = "TIMEOUT"

    except OSError:
        state = "ERROR"

    return ScanResult(
        target=target,
        port=port,
        state=state,
    )


def scan_ports(
        target: str,
        start_port: int,
        end_port: int,
        timeout: float = 1.0,
) -> list[ScanResult]:

    ports = range(start_port, end_port + 1)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(
            executor.map(
                lambda port: scan_port(target, port, timeout),
                ports,
        )
    )
    
    return results