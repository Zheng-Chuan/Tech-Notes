#include <iostream>
using namespace std;


int main() {
    int a[2][3] = {{1,2,3}, {4,5,6}};
    int *p[][] = &a;
    cout << p << endl;

    return 0;
}