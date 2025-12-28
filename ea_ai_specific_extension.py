# Example: Automated capability-impact analysis
import networkx as nx

# Create capability dependency graph
G = nx.DiGraph()
G.add_edges_from([
    ('Data_Quality', 'Feature_Engineering'),
    ('Feature_Engineering', 'Model_Training'),
    ('Model_Training', 'Prediction_Serving'),
    ('Prediction_Serving', 'Business_Decision'),
])

# Calculate capability criticality
betweenness = nx.betweenness_centrality(G)
print("Most critical capabilities for AI value flow:")
for capability, score in sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"  - {capability}: {score:.3f}")