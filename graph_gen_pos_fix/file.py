from graphviz import Source
path = 'test4.dot'
#s = Source.from_file(path, engine="neato", format = "svg")
s = Source.from_file(path,  format = "svg")
s.view()

