import sys
from inspect import isroutine
from types import ModuleType
from keyword import kwlist

__author__ = 'Gregori Gerebtzoff'
__version__ = '1.2'
__update__ = '11/10/2011'

def generate_python_autocomplete(python_script):
  ''' 
  Generates a xml to be used by Notepad++ for python autocompletion
  
  Command :
    python generate_python_autocomplete.py < my_imports.py > python.xml
  '''
  imports = set()
  level = 3
  
  for line in python_script:
    exec(line)
    
  for func in dir():
    imports.add(func)

  outputs = set()
  while len(imports) > 0:
    new_imports = set()
    for key in imports :        
      current_function = False
      try :
        current_function = eval(key)
      except :
        continue
        
      if current_function :
        # このコード中に含まれる変数を弾く
        if type(current_function) != ModuleType and len(key.split('.')) == 1 :
          continue
          
        # モジュール名はそのまま追加
        if type(current_function) == ModuleType and len(key.split('.')) == 1 :
          outputs.add(key)
        
        for func in dir(current_function):
          if 'Error' in func or 'Warning' in func or 'Exception' in func :
            continue
          if func[0] == '_' or func[-1] == '_' :
            continue
          
          outputs.add(func)
          if key.count('.') < level :
            new_imports.add(key + '.' + func)
            
    imports = new_imports
    
  for kw in kwlist :
    outputs.add(kw)
    
  keys = list(outputs)
  keys.sort()
  xml = '<?xml version="1.0" encoding="Windows-1252" />\n<NotepadPlus>\n\t<AutoComplete>\n'
  for key in keys :
    xml += '\t\t<KeyWord name="{}" />\n'.format(key)
  xml += '\t</AutoComplete>\n</NotepadPlus>\n'
  return xml

if __name__ == '__main__':
  python_script = ''
  if not sys.stdin.isatty():
    python_script = sys.stdin.readlines()
  xml = generate_python_autocomplete(python_script)
  sys.stdout.write(xml)