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
    return label

#G = graphviz.Graph('network',  format='svg')


file1 = open('network.data', 'r')
Lines = file1.readlines()
  
count = 0
nets = {}
nodes_label = {}
nodes_ip = {}

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

    if param[0] == "host":
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


    elif param[0] == "net":
         #print("net    "+param[0])
         nets[param[1]]  = param[2]
    else:
         print("...    "+param[0])

for key in nets:
    print("net  " + key + "  " + nets[key])

for key in nodes_ip:
    print("    " + key + " ip  " + str(nodes_ip[key]))
    if key in nodes_label:
         print("              " + " label  " + str(nodes_label[key]))

G = graphviz.Graph('network',  format='svg')

#G.engine = "fdp"
#G.engine = "circo"
#G.engine = "twopi"
G.engine = "neato"

#G.margin = "0.2"
#G.pad = "0.2"
#G.nodesep = "0.5"
#G.ranksep = 0.7
#G.attr('node', margin="0.1" )
#G.attr('edge', margin="0.1" )
G.attr('edge', len="2.0" )

for key in nets:
    G.node(key, shape = "ellipse", label = key + '\n' + nets[key])

for key in nodes_ip:
    if key in nodes_label:
        G.node(key, shape = "box" ,  label = key + '\n' + nodes_label[key])
    else:
        G.node(key, shape = "box" ,  label = key)

for key in nodes_ip:
    for ip in nodes_ip[key]:
        net = cnv_net(ip)
        oct4 = cnv_oct4(ip)
        print(key + " " + ip + " -> " + net)
        G.edge(key, net,  taillabel = "." + oct4 , labeldistance = "2.3" , labelfloat = "false")

#print(G.source)

G.view()


