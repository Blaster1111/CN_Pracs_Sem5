#include <bits/stdc++.h>
using namespace std;

const int inf = INT_MAX;
int n = 5;

vector<int> bellmanFordAlgo(vector<vector<int>> &edges, int src) 
{
    int E = edges.size();
    int inf = 99999;
    vector<int> dist(n, inf);
    dist[src] = 0;
    
    // Main relaxation loop
    for (int i = 0; i < n - 1; i++) 
    {
        for (int j = 0; j < E; j++) 
        {
            int u = edges[j][0];
            int v = edges[j][1];
            int cost = edges[j][2];
            
            if (dist[u] + cost < dist[v])
                dist[v] = dist[u] + cost;
        }
    }
    
    // Check for negative cycles
    for (int j = 0; j < E; j++) 
    {
        int u = edges[j][0];
        int v = edges[j][1];
        int cost = edges[j][2];
        
        if (dist[u] + cost < dist[v]) {
            cout << "Graph contains negative weight cycle!" << endl;
            return vector<int>(n, -inf); // Return all distances as -inf to indicate negative cycle
        }
    }
    
    return dist;
}

int main() 
{
    int E = 7;
    vector<vector<int>> edges = {
        // u, v, w => there is an edge from u to v with weight w
        {0, 1, 10},
        {0, 3, 2},
        {0, 4, 5},
        {2, 0, 1},
        {3, 1, 3},
        {3, 2, 2},
        {4, 2, 4}
    };
    
    int src;
    cout << "Enter The Source Vertex (0 Indexing): ";
    cin >> src;
    
    vector<int> dist = bellmanFordAlgo(edges, src);
    
    cout << "\n--------------------------------\n";
    cout << " Source | Shortest Path From " << src << " \n";
    cout << "--------------------------------\n";
    
    for (int i = 0; i < n; i++) {
        if (dist[i] == -inf)
            cout << "   " << i << "   |   -INF (Part of negative cycle)   \n";
        else
            cout << "   " << i << "   |   " << dist[i] << "   \n";
    }
    
    cout << "--------------------------------\n";
    return 0;
}