ParserValues = type("p_a", (object, ), {
	"subparsersValues": {
		"connect": (
			(("-a", "--alias"), {"type": str, "help": "Local name for ssh config", "required": True}),
			(("--userflags", ), {"type": str, "help": "Other ssh flags"})
		),
		"add": (
			(("-a", "--alias"), {"type": str, "help": "Local name for ssh config", "required": True}),
			(("-h", "--host", ), {"type": str, "help": "Remote server IP or domain", "required": True}),
			(("-p", "--port"), {"type": int, "help": "Remote server port"}),
			(("-u", "--user"), {"type": str, "help": "Username on remote server"}),
		),
		"remove": (
			(("-a", "--alias"), {"type": str, "help": "Local name for ssh config", "required": True}),
		),
		"list": (),
	}
})