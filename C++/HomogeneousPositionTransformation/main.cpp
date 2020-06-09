#include "Dense"
#include <iostream>
#include <cmath>

using Eigen::MatrixXd;
using Eigen::VectorXd;
using namespace std;

int main() {
  double x_particle, y_particle, x_observation, y_observation, theta_heading;

  x_particle = 4;
  y_particle = 5;
  x_observation = 2;
  y_observation = 2;
  theta_heading = -M_PI / 2;

  MatrixXd transformation_matrix(3, 3);
  transformation_matrix << cos(theta_heading), -sin(theta_heading), x_particle,
      sin(theta_heading), cos(theta_heading), y_particle,
      0, 0, 1;

  VectorXd observation(3);
  observation << x_observation, y_observation, 1;

  MatrixXd result = transformation_matrix * observation;

  cout << result << endl;

  return 0;
};
