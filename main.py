# Codespace for logic and backen functions


def get_commands():
    return ["/add","/delete", "/clear", "/list"]

def add(command, playlist):
    action = command.split(" ")[0]
    song = command.split(" ")[1:]

    if action == "/add":
    print(action)
    print(song)


    playlist.append(song)
    return playlist


if __name__ == "__main__":
    list = add("/add shine bright", [])
    print(list)






