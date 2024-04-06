import graphviz

ni = graphviz.Graph('ni',  format='svg')  

ni.attr('node', shape='rarrow')
ni.node('1', 'Ni!')
ni.node('2', 'Ni!')

ni.node('3', 'Ni!', shape='egg')

ni.attr('node', shape='star')
ni.node('4', 'Ni!')
ni.node('5', 'Ni!')


#print(ni.source)

ni.view()

#ni.render(format='svg', filename='out')
#ni.save("g.dot")




