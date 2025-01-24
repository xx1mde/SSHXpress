import colorama

class BeautyDict(object):

	SpaceBase = "\x20" * 4
	SpaceCounter: int = 0
	TypeDictionary: dict = {
		"str": colorama.Fore.LIGHTGREEN_EX,
		"int": colorama.Fore.LIGHTCYAN_EX,
		"NoneType": colorama.Fore.LIGHTRED_EX
	}

	@classmethod
	def print(cls, dictObject: dict) -> None:
		for key in dictObject.keys():
			if isinstance(dictObject[key], dict):
				print(cls.SpaceBase * cls.SpaceCounter + f"{key} {colorama.Fore.LIGHTBLACK_EX} ~")
				cls.SpaceCounter += 1
				cls.print(dictObject[key])
			else: print(cls.SpaceBase * cls.SpaceCounter + f"{key}: {cls.TypeDictionary.get(type(dictObject[key]).__name__, colorama.Fore.LIGHTBLACK_EX)}{dictObject[key]}")
		#print(cls.SpaceBase * cls.SpaceCounter + f"{colorama.Fore.LIGHTBLACK_EX}")
		cls.SpaceCounter -= 1