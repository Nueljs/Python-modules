def secure_archive(file_name: str, action: str = "r",
                   content: str | None = None) -> tuple[bool, str]:
    try:
        with open(file_name, action) as file:
            if action == "r":
                return (True, file.read())
            elif action == "w":
                file.write(content)
                return (True, "Content succesfully written to file")
            else:
                raise OSError
    except OSError as e:
        message: str = str(e)
        return (False, message)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not/existing/file", "r"))
    print("")
    print("Using 'secure_archive' tyo read from an inaccessible file:")
    print(secure_archive("/etc/shadow", 'r'))
    print("")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print("")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", "[FRAGMENT 001] Digital "
                         "preservation protocols established 2087"
                         "[FRAGMENT 002] Knowledge must survive the entropy"
                         " wars [FRAGMENT 003] Every byte saved is a victory"
                         " against oblivion"))
