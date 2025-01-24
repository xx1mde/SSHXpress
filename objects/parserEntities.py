ParserValues = type("p_a", (object, ), {
	"subparsersValues": {
		"connect": (
			(("-c", "--confname"), {"type": str, "help": "Local name for ssh config", "required": True}),
			(("--userflags", ), {"type": str, "help": "Other ssh flags"})
		),
		"add": (
			(("-c", "--confname"), {"type": str, "help": "Local name for ssh config", "required": True}),
			(("--host", ), {"type": str, "help": "Remote server IP or domain", "required": True}),
			(("-p", "--port"), {"type": int, "help": "Remote server port"}),
			(("-u", "--username"), {"type": str, "help": "Username on remote server"}),
		),
		"remove": (
			(("-c", "--confname"), {"type": str, "help": "Local name for ssh config", "required": True}),
		),
		"list": (),
	}
})