
import graphviz


def g(g):    # subgraph 
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled', color='lightgrey')
        c.node_attr.update(style='filled', color='white')
        c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
        c.attr(label='process #1')
    
    with g.subgraph(name='cluster_1') as c:
        c.attr(color='blue')
        c.node_attr['style'] = 'filled'
        c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
        c.attr(label='process #2')
    
    g.edge('start', 'a0')
    g.edge('start', 'b0')
    g.edge('a1', 'b3')
    g.edge('b2', 'a3')
    g.edge('a3', 'a0')
    g.edge('a3', 'end')
    g.edge('b3', 'end')
    
    g.node('start', shape='Mdiamond')
    g.node('end', shape='Msquare')

def g4(dot):    # subgraph 
    dot.edge('spam', 'eggs')

    c = graphviz.Graph(name='child', node_attr={'shape': 'box'})
    c.edge('foo', 'bar')
    dot.subgraph(c)

    d = graphviz.Graph(name='child2', node_attr={'shape': 'box'})
    d.edge('zoo', 'poo' )
    d.edge('poo', 'all' )
    dot.subgraph(d)

def g3(dot):    # node label
    dot.node('A', 'std::string')
    dot.node('B', '"spam"')
    dot.node('C', label=r'centered\nleft\lright\r')
    dot.node('tab', label='''<<TABLE>
 <TR>
   <TD>left</TD>
   <TD>right</TD>
 </TR>
</TABLE>>''')

    dot.edge('A', 'B')
    dot.edge('B','C')

def g2(dot):
    #dot.attr('node', shape='star')
    #dot.attr('node', shape='rarrow')
    dot.attr('node', shape='egg')

    dot.attr(rankdir='LR')  

    dot.node('A', 'King Arthur')  
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')
    
    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')

def g1(g):
    g.attr('node', shape='rarrow')
    g.node('1', 'Ni!')
    g.node('2', 'Ni!')
    
    g.node('3', 'Ni!', shape='egg')
    
    g.attr('node', shape='star')
    g.node('4', 'Ni!')
    g.node('5', 'Ni!gusa')


