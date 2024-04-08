
import graphviz


def subg_2():    # subgraph 
    c = graphviz.Graph(name='cluster_0') 
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
    c.attr(label='process #1')
    return c

def subg_3():    # subgraph 
    c = graphviz.Graph(name='cluster_1') 
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
    c.attr(label='process #2')
    return c

def node_attr(name, label):    # subgraph 
    #c = graphviz.Graph(name=name) 
    c = graphviz.Graph(name) 
    #c.attr(color='blue')
    c.attr(style='filled', color='lightgrey')
    #c.attr(label='process #3')
    c.attr(label=label)
    c.node(name+'-'+'X1', 
               label='JJ2', 
               shape='box',
               fixedsize = "true",         #ノードの大きさを指定可能とする
               width = "1.5",              #ノードの幅(インチ)
               height = "1.2",             #ノードの高さ(インチ)
               style = "solid,filled",     #ノードの枠線のスタイルと塗つぶしの指定
               color = "#336666",          #ノードの枠線の色
               fillcolor = "#CC9999",      #ノードを塗りつぶす色
               fontname = "Migu 1M",       #ノードラベルフォント
               fontsize = "16",            #ノードラベルフォントサイズ
               fontcolor = "blue"          #ノードラベルフォントカラー
            )
    c.node(name+'-'+'X2') 
    return c

def edge_attr(name, label):    # subgraph 
    #c = graphviz.Graph(name=name) 
    c = graphviz.Graph(name ) 
    #c.attr(color='blue')
    c.attr(style='filled', color='lightgrey')
    #c.attr(label='process #3')
    c.attr(label=label)
    c.attr(ranksep = "1.1")

    c.node(name+'-'+'X1', label='X1') 
    c.node(name+'-'+'X2', label='X2') 
    c.edge(name+'-'+'X1',name+'-'+'X2',
            label = "a-b",            #エッジラベル
            labelfloat = "true",        #ラベルの重なりを許可する
            headlabel = "head",       #エッジの終端にラベルをつける
            taillabel = "tail",       #エッジの始端にラベルをつける
            labeldistance = "2.5",      #ラベルの位置をノードからの距離で指定する
            labelangle = "70",          #ラベルの位置を角度で指定する
            color = "blue",             #エッジカラー
            style = "solid",            #エッジスタイル
            dir = "both",               #エッジの矢印を指定する
            arrowhead = "normal",       #エッジの終端の形状を指定
            arrowtail = "normal",       #エッジの始端の形状を指定
            arrowsize = "1",            #矢印の大きさ倍率で指定
            weight = "5",               #エッジの重み付け 重みが大きいエッジが結ぶノードがより近く配置される
            fontname = "Migu 1M",     #エッジラベルフォント
            fontsize = "14",            #エッジラベルフォントサイズ
            fontcolor = "red"          #エッジラベルフォントカラー
            )
    return c


def sub_graph(name, label):    # subgraph 
    #c = graphviz.Graph(name=name) 
    p = graphviz.Graph(name ) 
    p.attr(label=label)
    p.attr(labelloc="t")
    p.attr(labeljust="c")
    p.attr(bgcolor="#343434")
    p.attr(fontcolor="white")
    p.attr(fontsize="18")
    p.attr(style="filled")

    p.attr(rankdir = "TB")
    p.attr(margin = "0.2")
    p.attr(nodesep = "0.5")
    p.attr(ranksep = "0.8")
    p.attr(compound = "true")
    p.node_attr.update(style='solid,filled', color='red')
    p.edge_attr.update( color='white')

    with p.subgraph(name='cluster_0') as c:
        c.attr(label='clu0')
        c.attr(labelloc='t')
        c.attr(labeljust='l')
        c.attr(fillcolor='#ababab')
        c.node('alpha', label = 'alpha', shape = "box")
        c.node('beta', label = 'beta', shape = "box")
        c.node('gamma', label = 'gamma', shape = "box")
        c.node('eta', label = 'eta', shape = "box")
        c.edge('alpha', 'beta')
        c.edge('alpha', 'gamma')
        c.edge('alpha', 'eta')

    with p.subgraph(name='cluster_1') as c:
        c.attr(label='clu1')
        c.attr(labelloc='t')
        c.attr(labeljust='l')
        c.attr(fillcolor='#ababab')
        c.node('delta', label = 'delta', shape = "box")
        c.node('epsilon', label = 'epsilon', shape = "box")
        c.node('zeta', label = 'zeta', shape = "box")
        c.node('theta', label = 'theta', shape = "box")
        c.edge('delta', 'epsilon')
        c.edge('delta', 'zeta')
        c.edge('delta', 'theta')

    with p.subgraph(name='cluster_2') as c:
        c.attr(label='clu2')
        c.attr(labelloc='t')
        c.attr(labeljust='l')
        c.attr(fillcolor='#888888')
        c.node('lambda', label = 'lambda', shape = "octagon")
        c.node('mu', label = 'mu', shape = "octagon")
        c.edge('lambda', 'mu')
    
    with p.subgraph(name='cluster_3') as c:
        c.attr(label='clu3')
        c.attr(labelloc='t')
        c.attr(labeljust='l')
        c.attr(fillcolor='#888888')
        c.node('nu', label = 'nu', shape = "trapezium")
        c.node('xi', label = 'xi', shape = "trapezium")
        c.edge('nu', 'xi')

    with p.subgraph(name='sg') as c:
        c.node('iota', label = 'iota', shape = "Mdiamond")
        c.node('kappa', label = 'kappa', shape = "Mdiamond")
        c.edge('iota', 'kappa')

    p.edge('alpha', 'delta')
    p.edge('beta', 'lambda')
    p.edge('gamma', 'lambda')
    p.edge('epsilon', 'nu')
    p.edge('eta', 'mu')
    return p

def subg2(name, label ):    # subgraph 
    #c = graphviz.Graph(config["name"]) 
    c = graphviz.Graph(name) 
    #c.attr(label=config["label"])
    c.attr(label=label)
    c.node('1alpha', label='alpha2')
    c.node('1beta',  label='beta1')
    c.node('1yan',   label='yan1')
    c.node('1top',   label='top1')
    c.edge('1alpha', '1beta')
    c.edge('1alpha', '1yan')
    c.edge('1yan', '1top')
    c.edge('1top', '1beta')
    return c

def subg3(config):    # subgraph 
    #c = graphviz.Graph(name=config["name"]) 
    c = graphviz.Graph(config["name"]) 
    c.attr(label=config["label"])
    for key in config["nodes"]:
         print(key)
         c.node(config["name"]+'.'+key, label=key)
    for (f, t) in config["edges"]:
         c.edge(config["name"]+'.'+f, config["name"]+'.'+t)
    return c

def subg4(name, label, config):    # subgraph 
    c = graphviz.Graph(name) 
    c.attr(label=label)
    for key in config["nodes"]:
         print(key)
         c.node(name+'.'+key, label=key)
    for (f, t) in config["edges"]:
         c.edge(name+'.'+f, name+'.'+t)
    return c

def g(g):    # subgraph 
    #g.attr(rankdir="LR")
    #g.attr(rankdir="TB")
    #g.attr(layout="dot")
    g.attr(layout="fdp")


    config = {
              #"name"  : "cluster_6",
              #"name"  : "cluster_6",
              #"label" : "top-tree4",
              "nodes" : ["alpha1","beta", "yan", "top"],
              "edges" : [
                         ("alpha1", "beta"),
                         ("beta", "yan"),
                         ("yan", "top"),
                         ("top", "alpha1"),
                        ]
            }

    config2 = {
              "name"  : "cluster_6",
              "label" : "top-tree9",
              "nodes" : ["alpha1","beta", "yan", "top"],
              "edges" : [
                         ("alpha1", "beta"),
                         ("beta", "yan"),
                         ("yan", "top"),
                         ("top", "alpha1"),
                        ]
            }

    g.subgraph(node_attr('cluster11', "node attr"))
    g.subgraph(edge_attr('cluster10', "edge attr"))
    g.subgraph(sub_graph('cluster12', "sub graph"))
    #g.subgraph(subg2('cluster_9', "top-tree"))
    #g.subgraph(subg3(config2))
    g.subgraph(subg4("cluster_21","tree1",config))
    g.subgraph(subg4("cluster_22","tree2",config))
    g.subgraph(subg4("cluster_23","tree3",config))


def g6(g):    # subgraph 

    g.attr(splines="true", nodesep="0.8",label="Complex Architecture", labelloc = "t")
    #g.edge_attr.update(dir="both")
    g.attr('edge',dir="both")

    #g.attr(layout="dot")
    #g.attr(rankdir="LR")
    g.attr(rankdir="TB")

    #g.attr(layout="neato")
    g.attr(layout="fdp")
    #g.attr(layout="circo")
    #g.attr(layout="twopi")

    with g.subgraph(name='cluster_clients_mobvm_a') as c:
        c.attr(label='xvm_a Clients')
        c.attr(style='dashed' )
        c.attr(rank='same' )
        c.node('mobvm_a_req',label='xvm_a Application ..', shape='Mrecord')
        c.node('mobvm_a_req1',label='xvm_a Application 1', shape='Mrecord')

    with g.subgraph(name='cluster_clients_prot_a') as c:
        c.attr(label='Z Clients')
        c.attr(style='dashed' )
        c.attr(rank='same' )
        c.node('z_req',label='Z Application ..', shape='Mrecord')
        c.node('z_req1',label='Z Application 1', shape='Mrecord')

    with g.subgraph(name='cluster_prot_asrv') as c:
        c.attr(label='Z Shapeshifters\n(Configurable\nZ Shapeshifter')
        c.attr(style='dashed' )
        c.node('z_shapeshifter',label='Z Shapeshifter Appearances', shape='Mrecord')
        g.edge('z_req1', 'z_shapeshifter',dir="both", constraint="true", headlabel="H100",  taillabel="T100")
        g.edge('z_req', 'z_shapeshifter',dir="both", constraint="true")

    with g.subgraph(name='cluster_machsrv') as c:
        c.attr(label='Machsrv Shapeshifter')
        c.node('machsrv_xprot_gen',label='<f0>Machsrv Core|<f1>PROT_A-to-XPROT Converter', shape='Mrecord')

        g.edge('z_shapeshifter', 'machsrv_xprot_gen:f0',dir="both", constraint="true")
        g.edge('mobvm_a_req1', 'machsrv_xprot_gen:f0',dir="both", constraint="true")
        g.edge('mobvm_a_req', 'machsrv_xprot_gen:f0',dir="both", constraint="true")

    #with g.subgraph(name='cluster_accel') as c:
    #    c.attr(label='NOXd Shapeshifter')
    #    c.node('accel_appearance',label='NOXd Appearance', shape='Mrecord')

    with g.subgraph(name='cluster_yours_trulybox') as c:
        c.attr(label='YoursTruly')

        with c.subgraph(name='cluster_tunnel') as c1:
            c1.attr(label='Foo Reactor')
            c1.node('tunnel_ingress',label='Ingress Shapeshifter', shape='Mrecord')
            c1.node('accel',label='NOX Shapeshifter', shape='Mrecord')
            c1.node('tunnel_egress',label='Egress Shapeshifter', shape='Mrecord')

            g.edge('tunnel_ingress', 'accel',dir="both")
            g.edge('accel', 'tunnel_egress',dir="both")
            g.edge('accel_appearance', 'accel',dir="both", constraint="true")

        with c.subgraph(name='cluster_frontend') as c1:
            c1.attr(label='YoursTruly Front-End')
            c1.node('others',label='Other Chunks', shape='Mrecord')
            c1.node('other_xprot',label='XPROT \"crystalizer\"', shape='Mrecord')
            c1.node('front_end_jz',label='JZ Chunk', shape='Mrecord')
            c1.node('arbiter_vadam',label='Arbiter Chunks', shape='Mrecord')

            g.edge('arbiter_vadam', 'other_xprot',style="dotted")
            g.edge('arbiter_vadam', 'front_end_jz',style="dotted")
            g.edge('arbiter_vadam', 'others',style="dotted")

            g.edge('front_end_jz', 'tunnel_ingress',dir="both", label="XPROT over PROT_G")
            g.edge('front_end_jz', 'other_xprot',dir="both" )
            g.edge('other_xprot', 'machsrv_xprot_gen',dir="both", label="XPROT over PROT_G",constraint="tru")



    with g.subgraph(name='cluster_shapeshifter_misc') as c:
        c.attr(label='Other Shapeshifters')
        c.attr(style='dashed' )
        c.node('handle_x',label='Shapeshift X', shape='Mrecord')
        c.node('handle_1',label='Shapeshift 1', shape='Mrecord')

        g.edge('others', 'handle_1',style="dotted", dir="both",constraint="true")
        g.edge('others', 'handle_x',style="dotted", dir="both",constraint="true")

    with g.subgraph(name='cluster_accel') as c:
        c.attr(label='GS NOXd Shapeshifter')
        c.node('accel_appearance',label='NOXd Appearance', shape='Mrecord')


    with g.subgraph(name='cluster_space_ship_a') as c:
        c.attr(label='ShipX')

        with c.subgraph(name='cluster_vm_a') as c1:
            c1.attr(label='ReactorX')
            with c1.subgraph(name='cluster_tungsten') as c2:
               c2.attr(label='Tungsten')
               c2.node('zzz',label='ZZZ', shape='Mrecord')
               c2.node('yyy',label='YYY', shape='Mrecord')


        with c.subgraph(name='cluster_piston') as c1:
            c1.attr(label='ReactorY')
            c1.node('zzz_worker',label='ZZZ Worker', shape='Mrecord')
            c1.node('yyy_worker',label='YYY Worker', shape='Mrecord')
            c1.node('foo_agent',label='Foo Agent', shape='Mrecord')

            g.edge('foo_agent', 'zzz_worker',dir="both",constraint="true", label="MechCmd")
            g.edge('foo_agent', 'yyy_worker',dir="both",constraint="true", label="MechCmd")

            g.edge('zzz_worker','zzz', dir="both",constraint="true", label="SCADA_A()")
            g.edge('yyy_worker','yyy', dir="both",constraint="true", label="SCADA_A()")

            g.edge('tunnel_egress', 'foo_agent',dir="both", label="Raw PROT_G",constraint="true")





def g5(g):    # subgraph 
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


