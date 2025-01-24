import subprocess, sys, json, os, copy

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import Terminal256Formatter

os.makedirs(os.path.abspath(f"{os.path.dirname(sys.argv[0])}/config/"), exist_ok=True)

from modules import Parser, Logger, Config
from objects import ParserValues

class MainCore(object):

	_DESEREALIZED_CONFIG: dict = {}
	__PATH: str = os.path.abspath(f"{os.path.dirname(sys.argv[0])}/config/config.json")
	__PATH_OLD: str = os.path.abspath(f"{os.path.dirname(sys.argv[0])}/config/config.json.old")

	def __init__(self, *args, **kwargs):
		super(MainCore, self).__init__(*args, **kwargs)

		self.commandObject: object = Parser.parse(_commandLineArgs=list(sys.argv[1:]), _parserValues=ParserValues.subparsersValues)
		self.loadJSONConfig(_command=self.commandObject.command)
		getattr(self, self.commandObject.command)()

	def loadJSONConfig(self, _command: str):

		if os.path.exists(self.__PATH):
			try:
				if os.path.getsize(self.__PATH) != 0:
					with open(self.__PATH, "r") as _json: self._DESEREALIZED_CONFIG = json.loads(_json.read())
			except Exception as e:
				Logger.stderr(f"Config error. Exception: <{e}>.")
				Config.recreateConfig(self.__PATH, self.__PATH_OLD)
				Logger.stdout("Config recreated.")
		else:
			Config.newConfig(self.__PATH)
			Logger.stdout("New config created.")

	def list(self): print(highlight(json.dumps(self._DESEREALIZED_CONFIG, indent=4), JsonLexer(), Terminal256Formatter(style="lightbulb")))

	def add(self):
		self.commandObjectDeepCopy = copy.deepcopy(self.commandObject.__dict__)
		del self.commandObjectDeepCopy["command"]
		del self.commandObjectDeepCopy["confname"]

		self._DESEREALIZED_CONFIG[self.commandObject.confname] = self.commandObjectDeepCopy
		Config.rewriteConfig(self.__PATH, self._DESEREALIZED_CONFIG)

	def remove(self):
		del self._DESEREALIZED_CONFIG[self.commandObject.confname]
		Config.rewriteConfig(self.__PATH, self._DESEREALIZED_CONFIG)

	def connect(self):
		_localConfigObject = self._DESEREALIZED_CONFIG[self.commandObject.confname]
		_sshRequest = (
			f"ssh "
			f"{_localConfigObject['username']+'@' if _localConfigObject['username'] != None else ''}"
			f"{_localConfigObject['host']}"
			f"{(' -p ' + str(_localConfigObject['port'])) if _localConfigObject['port'] != None else ''}"
		)
		subprocess.run(_sshRequest, shell=True)

if __name__ == "__main__": MainCore()
#subprocess.run("ssh -t 192.168.0.104 -p 8022", shell=True)