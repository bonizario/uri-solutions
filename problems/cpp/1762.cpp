#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(0);
    cin.tie(0);
    int y, t;
    cin >> y;
    while (y--) {
        unordered_map<string, double> presents;
        double toy_weight, sled_weight, total_weight = 0;
        int toy_quantity;
        string toy_name;
        cin >> t;
        while (t--) {
            cin >> ws;
            getline(cin, toy_name);
            cin >> toy_weight;
            presents[toy_name] = toy_weight;
        }
        cin >> sled_weight;
        while (true) {
            cin >> ws;
            getline(cin, toy_name);
            cin >> toy_quantity;
            if (toy_name == "-" && toy_quantity == 0) break;
            if (presents.find(toy_name) == presents.end()) {
                cout << "NAO LISTADO: " << toy_name << "\n";
                continue;
            } else {
                total_weight += (presents[toy_name] * toy_quantity);
            }
        }
        cout << "Peso total: " << fixed << setprecision(2) << total_weight << " kg\n";
        cout << "Numero de trenos: " << setprecision(0) << ceil(total_weight / sled_weight) << "\n\n";
    }

    return 0;
}
