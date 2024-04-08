import graphviz
import build

g = graphviz.Graph('ni',  format='svg')  

build.g(g)



#print(ni.source)

g.view()

#ni.render(format='svg', filename='out')
#ni.save("g.dot")




