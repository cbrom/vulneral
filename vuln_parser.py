# find classes
# find variables
# find functions
# find method calls
# find sources
# find sinks

import time
import phplex
from phpparse import make_parser
import simplejson

class Node:
	def __init__(self, name):
		self.name = name
		self.children = []
		self.parent = None

class AssignmentNode(Node):
	def __init__(self, name, source, dest):
		Node.__init__(self, name)
		self.source = source
		self.dest = dest

class FunctionCall(Node):
	def __init__(self, name, function_name, params, dest):
		Node.__init__(self, name)
		self.function_name = function_name
		self.params = params
		self.dest = dest

class Class():
	def __init__(self):
		pass

class Function():
	def __init__(self, function_node):
		self.function_node = function_node
		self.dataflow = Dataflow(self.function_node)


class Dataflow:
	def __init__(self, parsed_result):
		root = Node("root")

	def scan_function_call(self):
		pass

	def scan_classes(self):
		pass

	def scan_variables(self, node_value):
		pass

	def scan(self):
		# get assignments
		# get function calls
		# get loops ...

		# Assignment
		parsed_variables = []
		for token in self.tokens:
			node_type = token[0]
			if node_type == "Assignment":
				self.scan_variables(node_value)
			elif node_type == "FunctionCall":
				self.scan_variables
				node_value = token[1]
				expr = node_value['expr']
				# check arrayoffset assignment, variable assignment, function call
				# check expr
				source = ''
				dest = node_value['node']['variable']['name']
				if expr[0] == "ArrayOffset":
					source = expr[1]['node']['variable']['name']

				variable = Variable(dest, source)
				parsed_variables



class Analyzer:
	def __init__(self, tokens):
		self.tokens = tokens
		self.global_variables = []
		self.global_functions = []
		self.global_classes = []


	def analyze(self):
		# scan variables
		# scan functions
		# scan classes
		self.scan_variables()
		self.scan_functions()
		self.scan_classes()

		self.detect_vulns()

	def scan_functions(self):
		pass

	def scan_classes(self):
		pass

	def scan_variables(self):
		# get assignments
		# get function calls
		# get loops ...

		# Assignment
		parsed_variables = []
		for token in self.tokens:
			node_type = token[0]
			if node_type == "Assignment":
				node_value = token[1]
				expr = node_value['expr']
				# check arrayoffset assignment, variable assignment, function call
				# check expr
				source = ''
				dest = node_value['node']['variable']['name']
				if expr[0] == "ArrayOffset":
					source = expr[1]['node']['variable']['name']

				variable = Variable(dest, source)
				parsed_variables




class Variable:
	def __init__(self, name, source):
		self.id = time.time()
		self.name = name
		self.source = source

class Function:
	def __init__(self, name):
		self.name = name


def export(items):
    result = []
    if items:
       for item in items:
           if hasattr(item, 'generic'):
               item = item.generic(with_lineno=with_lineno)
           result.append(item)
    return result


if __name__ = "__main__":
	with_lineno = True



	parser = make_parser()

	file = "auth_controller.php"
	# file = "test_json.py"
	with open(file, "r") as f:
	    input_file = f.read()

	parsed_result = export(parser.parse(input_file, lexer=phplex.lexer.clone(), tracking=with_lineno))

	analyzer = Analyzer(parsed_result)

	analyzer.analyze()