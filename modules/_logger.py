import colorama
import datetime

colorama.init(autoreset=True)

FR = colorama.Fore.RESET
FCEX = colorama.Fore.LIGHTCYAN_EX
FREX = colorama.Fore.LIGHTRED_EX

Logger = type("lo", (object, ), {
	"stdout": lambda log: print(f"{FCEX}[{datetime.datetime.now().strftime('%H:%M:%S')}]{FR} - {log}"),
	"stderr": lambda err: print(f"{FREX}[{datetime.datetime.now().strftime('%H:%M:%S')}]{FR} - {err}"),
})