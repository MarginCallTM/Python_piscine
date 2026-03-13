def archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        filename = ('new_discovery.txt')
        file = open(filename, 'w')
        print(f"Initializing new storage unit: {filename}")
        print("Storage unit created sucessfully...")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("Data inscription complete. Storage unit sealed.")
        file.close()
        print(f"Archive {filename} ready for long-term preservation")
    except Exception:
        print(f"ERROR: During the creation of the files:  {filename}.")


if __name__ == "__main__":
    archive_creation()
