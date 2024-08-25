from getkey import getkey
import readline, json, os, traceback

history = []

try:
    os.mkdir("TL")
except:
    pass

try:
    os.mkdir("TL/temp")
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
        "\033[1m\033[91m[FATUL]: Terminal Lite failed to initialize during environment variables check. \n\033[0m\033[91m"
        + traceback.format_exc()
        + " \033[0m"
    )
    exit(1)

commands = []
if not os.path.exists("./TL/temp/environment"):
    try:
        c = []
        for i in envpath["variables"]["path"]:
            for i, i2, i3 in os.walk(i):
                print("__")
                print(i)
                print(i2)
                print(i3)
        json.dumps(c,open("./TL/temp/environment","w"))
    except Exception as e:
        print(
            "\033[1m\033[91m[FATUL]:\033[91m Terminal Lite failed to initialize during environment creation. \n\033[0m\033[91m"
            + traceback.format_exc()
            + " \033[0m"
        )
        exit(1)
else:
    pass

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
            break
        except EOFError:
            break


def _run(command):
    com = command.split(" ")
    if com[0] == "":
        pass
    elif com[0] == "exit":
        print("Closing Terminal Lite...")
        exit()
    elif com[0] == "clean":
        print("\033c")
    else:
        print("\033[91m[ERROR]: Command not found \n\033[0m")

if __name__ == "__main__":
    while True:
        _run(_in(f"\033[94m@ \033[0m\033[1m\033[92m{path} : \033[0m"))
