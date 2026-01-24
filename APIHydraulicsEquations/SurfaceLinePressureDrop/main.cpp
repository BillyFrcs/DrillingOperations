#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double Np = 3.32 * std::log10(34.0 / 53.0);
    double Kp = (5.11 * 53) / std::pow(1022, 0.64);

    std::cout << Np << std::endl;
    std::cout << Kp << std::endl;

    return 0;
}