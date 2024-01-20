#openstockmate algoritma 
import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt

def draw_algorithm():
    G = nx.DiGraph()

    G.add_node("StokPage")
    G.add_node("CustomUserManager")
    G.add_node("CustomUser")
    G.add_node("Category")
    G.add_node("ComponentDocumentLink")
    G.add_node("Component")
    G.add_node("DocumentType")
    G.add_node("Document")
    G.add_node("LocationType")
    G.add_node("Location")
    G.add_node("Manufacturer")
    G.add_node("Package")
    G.add_node("PurchaseDetail")
    G.add_node("Purchase")
    G.add_node("Supplier")

    G.add_edge("CustomUser", "StokPage")
    G.add_edge("CustomUserManager", "CustomUser")
    G.add_edge("ComponentDocumentLink", "Document")
    G.add_edge("Component", "Category")
    G.add_edge("Component", "Manufacturer")
    G.add_edge("Component", "Category")
    G.add_edge("Document", "DocumentType")
    G.add_edge("Location", "LocationType")
    G.add_edge("PurchaseDetail", "Purchase")
    G.add_edge("PurchaseDetail", "Component")
    G.add_edge("Purchase", "Supplier")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=300, node_color="pink", font_size=8, edge_color='black', linewidths=0.5)
    plt.gca().set_facecolor('black')
    plt.show()

if __name__ == "__main__":
    draw_algorithm()
