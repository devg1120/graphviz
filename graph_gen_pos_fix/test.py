# coding: utf-8 
from graphviz import Graph
from graphviz import Digraph


###  X.Y
###
###  Y
###  ^
###  |
###  |
###  -----> X
###
###
###  0.2  1.2  2.2  3.2
###  0.1  1.1  2.1  3.1
###  0.0  1.0  2.0  3.0
###

gv = Digraph(engine='neato', format='svg')
# フォント設定
gv.attr('node', fontname="MS Gothic")
# ノード作成
gv.node("項目1", pos="0,0!")
gv.node("項目2", pos="3,0!")
gv.node("項目3", pos="3,2!")
gv.node("項目4", pos="0,2!")
# エッジ作成
gv.edge("項目1", "項目2")
gv.edge("項目2", "項目3")
gv.edge("項目3", "項目4")
gv.edge("項目4", "項目1")

gv.view()

