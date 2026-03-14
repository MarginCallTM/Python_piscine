def crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    try:
        lost_name = ("lost_archive.txt")
        print(f"\nCRISIS ALERT: Attempting access to '{lost_name}'...")
        with open("lost_archive.txt") as lost:
            print(f"Content of the lost archive : {lost.read()}\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        permission_name = ("classified_vault.txt")
        print(f"CRISIS ALERT: Attempting access to '{permission_name}'...")
        with open("classified_vault.txt") as permission:
            print(f"Secret defense content = {permission.read()}\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    try:
        archive_name = ("standard_archive.txt")
        print(f"ROUTINE ACCESS: Attempting access to '{archive_name}'...")
        with open("standard_archive.txt") as archive:
            print(f"SUCCESS: Archive recovered -  '{archive.read()}'")
            print("Normal operations resumed")
    except Exception as e:
        print(f"Error detected in the system : {e}")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
