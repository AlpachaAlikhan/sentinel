from scanner.port_scanner import scan_ports
from scanner.service_detector import detect_service


def main():
    target = "127.0.0.1"

    try:
        results = scan_ports(
            target=target,
            start_port=1,
            end_port=1024,
            timeout=0.5,
            max_workers=100,
        )

    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Scan results for {target}")
    print("-" * 50)

    open_ports = [
        result for result in results
        if result.state == "OPEN"
    ]

    for result in open_ports:
        service, banner = detect_service(
            target,
            result.port,
        )

        result.service = service
        result.version = banner

        print(f"{result.port}/tcp OPEN")

        if service:
            print(f"  Service: {service}")

        if banner:
            print(f"  Banner: {banner[:100]}")

    print("-" * 50)
    print(f"Open ports: {len(open_ports)}")


if __name__ == "__main__":
    main()