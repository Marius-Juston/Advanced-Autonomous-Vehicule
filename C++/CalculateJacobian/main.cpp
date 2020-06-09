#include <iostream>
#include <vector>
#include "Dense"

using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::cout;
using std::endl;

MatrixXd CalculateJacobian(const VectorXd &x_state);

int main() {
  /**
   * Compute the Jacobian Matrix
   */

  // predicted state example
  // px = 1, py = 2, vx = 0.2, vy = 0.4
  VectorXd x_predicted(4);
  x_predicted << 1, 2, 0.2, 0.4;

  MatrixXd Hj = CalculateJacobian(x_predicted);

  cout << "Hj:" << endl << Hj << endl;

  return 0;
}

MatrixXd CalculateJacobian(const VectorXd &x_state) {

  MatrixXd Hj(3, 4);
  // recover state parameters
  double px = x_state(0);
  double py = x_state(1);
  double vx = x_state(2);
  double vy = x_state(3);

  // check division by zero
  if (px == 0 && py == 0) {
    cout << "CalculateJacobian() - Error - Division by Zero" << endl;
    return Hj;
  }

  // compute the Jacobian matrix
  double distance = px * px + py * py;
  double px_dist = px / sqrt(distance);
  double py_dist = py / sqrt(distance);
  double bottom_left = (vx * py - vy * px) / pow(distance, 3 / 2.);

  Hj << px_dist, py_dist, 0, 0,
      -py / distance, px / distance, 0, 0,
      py * bottom_left, -px * bottom_left, px_dist, py_dist;

  return Hj;
}