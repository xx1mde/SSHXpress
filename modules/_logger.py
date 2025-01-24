import colorama
import datetime

colorama.init(autoreset=True)

FR = colorama.Fore.RESET
FC = colorama.Fore.CYAN
FRE = colorama.Fore.RED

Logger = type("lo", (object, ), {
	"stdout": lambda log: print(f"{FC}[{datetime.datetime.now().strftime('%H:%M:%S')}]{FR} - {log}"),
	"stderr": lambda err: print(f"{FRE}[{datetime.datetime.now().strftime('%H:%M:%S')}]{FR} - {err}")
})