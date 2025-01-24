import argparse
import colorama
import sys

colorama.init(autoreset=True)

class Parser(object):

	@staticmethod
	def parse(_commandLineArgs: list, _parserValues: dict) -> None:

		localParser = argparse.ArgumentParser(exit_on_error=False)
		localParser.error = lambda _err: (
			print(f"{colorama.Fore.RED}{_err} {set(_parserValues.keys())}."),
			sys.exit(0)
		)

		subparsers = localParser.add_subparsers(dest="command", help="Action: connect, add, remove", required=True)

		for parserName, parserInfo in zip(
			tuple(_parserValues.keys()),
			("Connect to ssh server", "Add new ssh configuration", "Remove ssh configuration", "Display available ssh configs")
		):
			_subparser = subparsers.add_parser(parserName, help=parserInfo)

			_subparser.error = lambda _err: (
				print(f"{colorama.Fore.RED}{_err}. Try -h (--help)"),
				sys.exit(0)
			)
			for subargs in _parserValues[parserName]: _subparser.add_argument(*subargs[0], **subargs[-1])

		return localParser.parse_args(_commandLineArgs)