#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double height, width, square_edge;

    cin >> height >> width >> square_edge;

   printf("%.f", (ceil(height/square_edge) * ceil(width/square_edge)) );

    return 0;
}