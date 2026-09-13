import socket
from concurrent.futures import ThreadPoolExecutor

from models.scan_results import ScanResult

def validate_port_range(start_port: int, end_port: int) -> None:
    if not 1 <= start_port <= 65535:
        raise ValueError("Start port must be between 1 and 65535")

    if not 1 <= end_port <= 65535:
        raise ValueError("End port must be between 1 and 65535")

    if start_port > end_port:
        raise ValueError("Start port cannot be greater than end port")

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
        max_workers: int = 100,
) -> list[ScanResult]:

    validate_port_range(start_port, end_port)

    ports = range(start_port, end_port + 1)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(
            executor.map(
                lambda port: scan_port(target, port, timeout),
                ports,
        )
    )

    results.sort(key=lambda result: result.port)

    return results