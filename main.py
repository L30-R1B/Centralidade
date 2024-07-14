import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de Análise de Redes', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_page_with_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

def analyze_network():
    G = nx.karate_club_graph()

    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    pagerank = nx.pagerank(G)

    sorted_degree = sorted(degree_centrality.items(), key=itemgetter(1), reverse=True)
    sorted_closeness = sorted(closeness_centrality.items(), key=itemgetter(1), reverse=True)
    sorted_betweenness = sorted(betweenness_centrality.items(), key=itemgetter(1), reverse=True)
    sorted_pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)

    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G)
    sizes = [10000 * degree_centrality[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_size=sizes, node_color='skyblue', edge_color='gray', font_weight='bold')
    plt.title('Rede com tamanhos proporcionais à centralidade de grau')
    plt.show()

    return {
        'degree': sorted_degree,
        'closeness': sorted_closeness,
        'betweenness': sorted_betweenness,
        'pagerank': sorted_pagerank
    }

# Gera o relatório
def generate_report(results):
    pdf = PDF()
    pdf.add_page()
    
    # Adiciona resultados ao relatório
    for centrality, data in results.items():
        title = f'Ranking de Vértices por Centralidade ({centrality.capitalize()})'
        body = '\n'.join([f'{node}: {value:.4f}' for node, value in data])
        pdf.add_page_with_chapter(title, body)
    
    # Salva o relatório em PDF
    pdf.output('network_analysis_report.pdf')

# Função principal
def main():
    results = analyze_network()
    generate_report(results)

if __name__ == "__main__":
    main()

