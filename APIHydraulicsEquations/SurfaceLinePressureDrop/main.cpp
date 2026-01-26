#include <iostream>
#include <cmath>

int main()
{
    double Np = 3.32 * std::log10(34.0 / 53.0);
    double Kp = (5.11 * 53) / std::pow(1022, 0.64);

    double PPsi = ((0.006025 * std::pow(560.23, 2) * 12.8) / (92916 * 3.826)) * 610;

    std::cout << Np << std::endl;
    std::cout << Kp << std::endl;

    std::cout << PPsi << std::endl;

    return 0;
}