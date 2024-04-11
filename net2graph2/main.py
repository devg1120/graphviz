import graphviz
#import build

def cnv_net( ipaddr_sl ):
   param1 = ipaddr_sl.split('/')
   subet_length = param1[1]
   param2 = param1[0].split('.')
   oct1 = param2[0]
   oct2 = param2[1]
   oct3 = param2[2]

   netaddr = oct1 + '.' + oct2 + '.' + oct3 + '.0/' + subet_length
   return  netaddr

def cnv_oct4( ipaddr_sl ):
   param1 = ipaddr_sl.split('/')
   subet_length = param1[1]
   param2 = param1[0].split('.')
   oct1 = param2[0]
   oct2 = param2[1]
   oct3 = param2[2]
   oct4 = param2[3]
   return  oct4

def make_label( param):
    label = ""
    for ele in param:
        label += ele
        label += ' '
    return label.rstrip()

#G = graphviz.Graph('network',  format='svg')


file1 = open('network.data', 'r')
Lines = file1.readlines()
  
count = 0
locdic = {}
nets = {}
nodes_label = {}
nodes_ip = {}
nodes_loc = {}
loc_nodes = {}

for line in Lines:
    line2 = line.strip()
    if line2 == "":
        continue
    if line2.startswith("#"):
        continue
    count += 1
    #print("Line{}: {}".format(count, line2))
    param = line2.split()
    #print(param[0])
    #print("    "+param[1])

    if param[0] == "loc":
         locname =  param[1] 
         label =  make_label( param[2:])
         #print("loc " + locname + "  \"" + label + "\"")
         locdic[locname] = label

    elif param[0] == "host":
         #print("host   "+param[0])
         hostname =  param[1] 
         if param[2] == "ip":
             if hostname in nodes_ip :
                 nodes_ip[hostname].append(param[3])
             else:
                 nodes_ip[hostname] = [param[3]]
         elif param[2] == "label":
                 #nodes_label[hostname] =  param[3] 
                 nodes_label[hostname] =  make_label( param[3:])
         elif param[2] == "loc":
             loc_name=  param[3] 
             nodes_loc[hostname] = loc_name
             if loc_name in loc_nodes :
                 loc_nodes[loc_name].append(hostname)
             else:
                 loc_nodes[loc_name] = [hostname]
                 #nodes_label[hostname] =  make_label( param[3:])


    elif param[0] == "net":
         #print("net    "+param[0])
         nets[param[1]]  = param[2]
    else:
         print("...    "+param[0])

for key in locdic:
    print("loc  " + key + "  \"" + locdic[key] + "\"")

for key in nets:
    print("net  " + key + "  " + nets[key])

for key in nodes_ip:
    print("    " + key + " ip  " + str(nodes_ip[key]))
    if key in nodes_label:
         print("              " + " label  \"" + str(nodes_label[key]) +"\"")

for key in loc_nodes:
    print("loc_nodes  " + key + "  " +  str(loc_nodes[key]))

for key in nodes_loc:
    print("nodes_loc  " + key + "  " +  str(nodes_loc[key]))
print("--------------------------------")

################################################
G = graphviz.Graph('network',  format='svg')

#G.engine = "fdp"
#G.engine = "circo"  // un support cluster
#G.engine = "twopi"
G.engine = "neato"

#G.margin = "0.2"
#G.pad = "0.2"
#G.nodesep = "0.5"
#G.ranksep = 0.7
#G.attr('node', margin="0.1" )
#G.attr('node', sep="0.1" )
#G.attr('edge', margin="0.1" )
G.attr('edge', len="3.0" )

subgraph = {}

for loc in loc_nodes:
    c = graphviz.Graph('cluster_' + loc)
    c.attr(label=loc)
    c.attr(labelloc="t")
    c.attr(labeljust="c")
    subgraph[loc] = c
    #G.subgraph(c)

for key in nets:
    G.node(key, shape = "ellipse", label = key + '\n' + nets[key])

#for key in nodes_ip:
#    if key in nodes_label:
#        G.node(key, shape = "box" ,  label = key + '\n' + nodes_label[key])
#    else:
#        G.node(key, shape = "box" ,  label = key)

for key in nodes_ip:
    if key in nodes_loc:
        loc = nodes_loc[key] 
        if key in nodes_label:
            subgraph[loc].node(key, shape = "box" ,  label =  key + '\n' + nodes_label[key])
        else:
            subgraph[loc].node(key, shape = "box" ,   label =  key)
    else:
        if key in nodes_label:
            G.node(key, shape = "box" ,  pos="10,10", label = key + '\n' + nodes_label[key])
            #G.node(key, shape = "box" ,   label = key + '\n' + nodes_label[key])
        else:
            G.node(key, shape = "box" ,  label = key)

for key in nodes_ip:
    for ip in nodes_ip[key]:
        net = cnv_net(ip)
        oct4 = cnv_oct4(ip)
        print(key + " " + ip + " -> " + net)
        G.edge(key, net,  taillabel = "." + oct4 , labeldistance = "2.3" , labelfloat = "false")

for loc in subgraph:
    G.subgraph(subgraph[loc])

#print(G.source)

G.view()


