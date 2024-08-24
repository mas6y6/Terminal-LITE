from getkey import getkey
import time, readline, json, os, traceback

history = []
#de

try:
    os.mkdir("TL")
except:
    pass

try:
    os.mkdir("TL")
except:
    pass

try:
    envpath = json.load(open("./TL/envpath", "r+"))
except:
    envpat = {
        "variables": {"path": [], "startpath": os.path.expanduser("~"), "overwides": {}}
    }
    json.dump(envpat, open("./TL/envpath", "w+"), indent=4)
    envpath = json.load(open("./TL/envpath", "r+"))

try:
    path = envpath["variables"]["startpath"]
except Exception as f:
    print(
        "\033[91,1m[FATUL]:\033[91m Terminal Lite failed to initialize during environment variables check. \n"
        + traceback.format_exc()
        + " \033[0m"
    )


def saveenvpath():
    json.dump(envpath, open("./TL/envpath", "r+"), indent=4)


def _in(prompt="dwda"):
    while True:
        try:
            command = input(prompt)

            if command.strip():
                history.append(command)
                readline.add_history(command)

            return command
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting...")
            break
        except EOFError:
            print("\nEOFError detected. Exiting...")
            break


def _run():
    pass


if __name__ == "__main__":
    while True:
        _run(_in(f"TL {path} :"))
