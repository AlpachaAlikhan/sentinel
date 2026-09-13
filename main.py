from scanner.port_scanner import scan_ports


def main():
    target = "127.0.0.1"

    results = scan_ports(target, 1, 1024)

    for result in results:
        if result.state == "OPEN":
            print(f"{result.port}/tcp OPEN")


if __name__ == "__main__":
    main()