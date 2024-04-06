
import graphviz

def g(g):    # subgraph 

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


