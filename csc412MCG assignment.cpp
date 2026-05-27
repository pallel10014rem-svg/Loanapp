#include <iostream>
#include <vector>
#include <set>

using namespace std;

void generateSequence(int seed)
{
    int a = 13;
    int m = 64;

    vector<int> sequence;
    set<int> seen;

    int x = seed;
    int period = 0;

    while (seen.find(x) == seen.end())
    {
        seen.insert(x);
        sequence.push_back(x);

        x = (a * x) % m;
        period++;
    }

    cout << "\n=========================\n";
    cout << "Seed: " << seed << endl;
    cout << "a = 13" << endl;
    cout << "m = 64\n" << endl;

    cout << "Sequence:\n";

    for (int num : sequence)
    {
        cout << num << " ";
    }

    cout << "\n\nPeriod = " << period << endl;
}

int main()
{
    int choice;

    do
    {
        int seed;

        cout << "\nMULTIPLICATIVE CONGRUENTIAL GENERATOR\n";
        cout << "-------------------------------------\n";

        cout << "Enter seed value (1 - 4): ";
        cin >> seed;

        generateSequence(seed);

        cout << "\nTry another seed?\n";
        cout << "1. Yes\n";
        cout << "0. Exit\n";
        cout << "Choice: ";
        cin >> choice;

    } while (choice != 0);

    return 0;
}
