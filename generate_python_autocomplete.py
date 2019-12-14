import sys
from inspect import isroutine, getdoc, signature
from types import ModuleType
from xml.sax.saxutils import quoteattr

__author__ = 'Gregori Gerebtzoff'
__version__ = '1.2'
__update__ = '11/10/2011'

def generate_python_autocomplete(python_script, **keywords):
	""" Generates a xml to be used by Notepad++ for python autocompletion
	Keywords: (bool) namespace, 
	(bool) private: to include namespaces (functions starting with two underscores) and private (starting with one underscore) functions
	(bool) no_builtin: to exclude builtin functions, 
	(int) level: to go to a user-defined level of deepness in functions browsing (default=2) """
	imports = {}
	errors = []
	namespace = False
	private = False
	no_builtin = False
	level = 2
	if 'namespace' in keywords:
		namespace = keywords['namespace']
	if 'private' in keywords:
		private = keywords['private']
	if 'no_builtin' in keywords:
		no_builtin = keywords['no_builtin']
	if 'level' in keywords:
		level = keywords['level']
	if type(python_script) == bytes:
		python_script = python_script.split("\n")
	for line in python_script:
		line = line.strip()
		if line[0:7] == "import " or line[0:5] == "from " or line[0:16] == "sys.path.append(":
			try:
				exec(line)
			except:
				errval = sys.exc_info()[1]
				if len(errval.args) == 2: # syntax error
					errors.append("\t-> %s: %s" % (errval.text, errval.msg))
					errors.append("\t   %s^" % ' '.join("" for i in range(errval.offset)))
				else: # import error
					errors.append("\t-> %s: %s" % (line, errval.args[0]))
	if no_builtin == False:
		import builtins
	for func in dir():
		imports[func] = 0
	outputs = {}
	while len(imports) > 0:
		new_imports = {}
		for key, val in imports.items():
			process = False
			item = key.split(".")[-1]
			if no_builtin == False and key == "__builtin__":
				process = True
			elif item[0:2] == "__" and namespace == True:
				process = True
			elif item[0:1] == "_" and private == True:
				process = True
			elif item[0:1] != "_" and item[-1] != "_":
				process = True
			if process == True:
				current_function = False
				if key.find("$") == -1: # found in some lucene functions
					try:
						current_function = eval(key)
					except:
						pass
				if current_function:
					docs = ""
					try:
						doc = getdoc(current_function)
						if doc is not None:
							docs = quoteattr(doc.strip())
							docs = docs.replace("\n", "&#x0a;")
					except:
						pass
					if isroutine(current_function):
						argspec = None
						try:
							argspec = signature(current_function)
							args = argspec[0]
							keywords = argspec[2]
							if argspec[3] is None:
								defaults = []
							else:
								defaults = list(argspec[3])
							if keywords != None:
								args.append("**")
								defaults.append("")
							if key.split(".")[0] == "__builtin__":
								outputs[item] = [argspec[0], defaults, docs]
								for k in key.split(".")[1:]:
									if k not in outputs:
										outputs[k] = [[], (), ""]
							else:
								outputs[key] = [argspec[0], defaults, docs]
								counter = 0
								for k in key.split("."):
									if k not in outputs:
										if counter == 0:
											doc = quoteattr("Module")
										elif counter < len(key.split(".")):
											doc = quoteattr("Function of %s" % ".".join(key.split(".")[0:-1]))
										else:
											doc = ""
										doc
										outputs[k] = [[], (), doc]
									counter += 1
						except:
							if key.split(".")[0] == "__builtin__":
								outputs[item] = [[], (), docs]
								for k in key.split(".")[1:]:
									if k not in outputs:
										outputs[k] = [[], (), ""]
							else:
								outputs[key] = [[], (), docs]
								counter = 0
								for k in key.split("."):
									if k not in outputs:
										if counter == 0:
											doc = quoteattr("Module")
										elif counter < len(key.split(".")):
											doc = quoteattr("Function of %s" % ".".join(key.split(".")[0:-1]))
										else:
											doc = ""
										outputs[k] = [[], (), doc]
									counter += 1
						if key.split(".")[0] != "__builtin__" and key not in outputs:
							outputs[key] = [[], (), ""] #if we add the docs here, the autocomplete won't show the function description when used together with the module, for instance re.findall() vs. findall()
					elif type(current_function) == type or (type(current_function) == ModuleType and len(key.split(".")) == 1): # to avoid sourcing modules in subclasses
						if key.split(".")[0] == "__builtin__":
							if len(key.split(".")) > 1:
								outputs[key.split(".", 2)[1]] = [[], (), docs]
						else:
							outputs[key] = [[], (), docs]
						for func in dir(current_function):
							if key + "." + func not in new_imports and val < level: # the value here is used to set how deep we go in the tree
								new_imports[key + "." + func] = val + 1
					elif len(key.split(".")) > 1 and key.split(".")[0] != "__builtin__" and type(current_function) != ModuleType:
						doc = quoteattr("(%s)" % type(current_function).__name__)
						outputs[key] = [[], (), doc]
		imports = new_imports
	if no_builtin == False:
		from keyword import kwlist
		for kw in kwlist + ["True", "False", "None"]:
			outputs[kw] = [[], (), ""]
	keys = list(outputs.keys())
	keys.sort()
	xml = '<?xml version="1.0" encoding="Windows-1252" ?>\n\
	<!--\n\
	@author Gregori Gerebtzoff\n\
	@version %s\n\
	-->\n<NotepadPlus>\n\
	<AutoComplete>\n\
		<Environment ignoreCase="no" startFunc="(" stopFunc=")" paramSeparator="," additionalWordChar = "." />\n' % __version__
	for key in sorted(outputs.keys()):
		items = key.split(".")
		if outputs[key][2] == "" and len(outputs[key][1]) == 0:
			xml += '\t\t<KeyWord name="%s" />\n' % key
		else:
			xml += '\t\t<KeyWord name="%s" func="yes">\n' % key
			xml += '\t\t\t<Overload retVal="" descr=%s>\n' % outputs[key][2]
			if len(outputs[key][0]) != 0:
				paramcounter = len(outputs[key][0])
				close_bracket = ""
				for param in outputs[key][0]:
					if paramcounter > len(outputs[key][1]):
						xml += '\t\t\t\t<Param name="%s" />\n' % param
					elif paramcounter == 1:
						if str(outputs[key][1][-paramcounter]) != "":
							xml += '\t\t\t\t<Param name="[%s=%s]%s" />\n' % (param, str(outputs[key][1][-paramcounter]), close_bracket)
						else:
							xml += '\t\t\t\t<Param name="[%s]%s" />\n' % (param, close_bracket)
					else:
						if str(outputs[key][1][-paramcounter]) != "":
							xml += '\t\t\t\t<Param name="[%s=%s" />\n' % (param, str(outputs[key][1][-paramcounter]))
						else:
							xml += '\t\t\t\t<Param name="[%s" />\n' % param
						close_bracket += "]"
					paramcounter -= 1
			xml += '\t\t\t</Overload>\n\t\t</KeyWord>\n'
	xml += '\t</AutoComplete>\n</NotepadPlus>\n'
	return xml, errors

##################################################################################
## Main
##################################################################################
if __name__ == "__main__":
	namespace = False
	private = False
	no_builtin = False
	level = 2
	argList = sys.argv[1:]
	for i in range(len(argList)) :
		if argList[i] in ["-h", "--help"]:
			_usage()
		elif argList[i] in ["-s", "--namespace"]:
			namespace = True
		elif argList[i] in ["-p", "--private"]:
			private = True
		elif argList[i] in ["-b", "--no_builtin"]:
			no_builtin = True
		elif argList[i] in ["-l", "--level"]:
			level = int(argList[i+1])
	python_script = ""
	if not sys.stdin.isatty():
		python_script = sys.stdin.readlines()
	xml, errors = generate_python_autocomplete(python_script, namespace=namespace, private=private, no_builtin=no_builtin, level=level)
	sys.stdout.write(xml)
	if len(errors) > 0:
		sys.stderr.write("Warning: could not process all imports:\n" + "\n".join(errors) + "\n")