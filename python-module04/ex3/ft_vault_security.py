def secure_archive(file_name: str, action: str = "r",
                   content: str | None = None) -> tuple[bool, str]:
    try:
        with open(file_name, action) as file:
            if action == "r":
                print(file.read())
            elif action == "w":
                file.write(content)
            
    except OSError as e:
        return (False, e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    secure_archive("not/existing/file", "r")
    print("")
    print("Using 'secure_archive' tyo read from an inaccessible file:")
    secure_archive("/etc/master.passwd", 'r')
    print("")
    print("Using 'secure_archive' to read from a regular file:")
    secure_archive("ancient_fragment.txt", "r")
    print("")
    print("Using 'secure_archive' to write precious content to a new file:")
    secure_archive("new_file.txt", "w")
