import graphviz
import build

ni = graphviz.Graph('ni',  format='svg')  

build.g(ni)


#print(ni.source)

ni.view()

#ni.render(format='svg', filename='out')
#ni.save("g.dot")




