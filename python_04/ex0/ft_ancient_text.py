
def data_recovery() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        filename = "ancient_fragment.txt"
        file = open(filename)
        print(f"Accessing Storage Vault: {filename}")
        print("Connection established...\n")
        print(file.read())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    data_recovery()
