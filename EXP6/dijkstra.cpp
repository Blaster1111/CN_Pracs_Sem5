#include <bits/stdc++.h>

using namespace std;

const int INF = 9999;

vector<int> dijistra(vector<vector<int>> &cost, int src)
{
    int n = cost.size();
    vector<bool> taken(n, false);
    vector<int> dist(n);
    for (int i = 0; i < n; i++)
        dist[i] = cost[src][i];
    taken[src] = true;
    dist[src] = 0;

    for (int i = 2; i < n; i++)
    {
        int mn = -1;
        for (int i = 0; i < n; i++)
            if (!taken[i])
                if (mn == -1 || dist[mn] > dist[i])
                    mn = i;
        taken[mn] = true;
        for (int i = 0; i < n; i++)
            if (!taken[i] && dist[i] > dist[mn] + cost[mn][i])
                dist[i] = dist[mn] + cost[mn][i];
    }
    return dist;
}

int main()
{
    int n = 5;
    vector<vector<int>> cost = {{INF, 10, INF, 2, 5},
                                {INF, INF, INF, INF, INF},
                                {1, INF, INF, INF, INF},
                                {INF, 3, 2, INF, INF},
                                {INF, INF, 4, INF, INF}};
    int src;
    cout << "Enter The Source Vertex(0 Indexing) : ";
    cin >> src;
    vector<int> dist = dijistra(cost, src);
    cout << "\n--------------------------------\n";
    cout << " Source | Shorted Path From " << src << " \n";
    cout << "--------------------------------\n";
    for (int i = 0; i < n; i++)
        cout << "   " << i << "   |   " << dist[i] << "   \n";
    cout << "--------------------------------\n";
    return 0;
}