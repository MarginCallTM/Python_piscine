import sys


def stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archivist_ID = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")
        print(
            f"\n[STANDARD] Archive status from {archivist_ID}:"
            f" {status_report}")
        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=sys.stderr)
        print("[STANDARD] Data transmission complete\n")
    except Exception as e:
        print(f"{e}")
    else:
        print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
