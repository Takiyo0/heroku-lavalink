from os import system


class StartLavalink:
    def run(self):
        try:
            system('sed -i "s|DYNAMICPORT|$PORT|" application.yml')
            system("java -jar Lavalink.jar")

        except BaseException as exc:
            print(f"[ERROR] Failed to start Lavalink. Info: {exc}")


StartLavalink().run()
