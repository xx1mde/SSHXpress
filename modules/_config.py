import json, os

class Config(object):
	@staticmethod
	def newConfig(configPath: str):
		with open(configPath, "w") as _jsonConfig: print(json.dumps({}, indent=4), file=_jsonConfig)

	@staticmethod
	def recreateConfig(configPath: str, oldconfigPath: str):
		if os.path.exists(oldconfigPath): os.remove(oldconfigPath)
		if os.path.exists(configPath): os.rename(configPath, oldconfigPath)

		Config.newConfig(configPath)

	@staticmethod
	def rewriteConfig(configPath: str, _data: dict):
		with open(configPath, "w") as _jsonConfig: print(json.dumps(_data, indent=4), file=_jsonConfig)