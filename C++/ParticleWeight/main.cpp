#include "Dense"
#include <iostream>
#include <cmath>

using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

int main() {
  double x_std = .3;
  double y_std = .3;

  double x = 6;
  double y = 3;

  double landmark_x = 5;
  double landmark_y = 3;

  double weight =
      exp(-(pow(x - landmark_x, 2) / (2 * x_std * x_std) + pow(y - landmark_y, 2) / (2 * y_std * y_std))) / (2 * M_PI * x_std * y_std);

  cout << weight << endl;

  return 0;
};
