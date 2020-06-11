#include <cmath>
#include <iostream>
#include <vector>

#include "Dense"
#include "grader.h"

using std::vector;
using Eigen::MatrixXd;
using Eigen::VectorXd;

vector<double> JMT(vector<double> &start, vector<double> &end, double T) {
  /**
   * Calculate the Jerk Minimizing Trajectory that connects the initial state
   * to the final state in time T.
   *
   * @param start - the vehicles start location given as a length three array
   *   corresponding to initial values of [s, s_dot, s_double_dot]
   * @param end - the desired end state for vehicle. Like "start" this is a
   *   length three array.
   * @param T - The duration, in seconds, over which this maneuver should occur.
   *
   * @output an array of length 6, each value corresponding to a coefficent in 
   *   the polynomial:
   *   s(t) = a_0 + a_1 * t + a_2 * t**2 + a_3 * t**3 + a_4 * t**4 + a_5 * t**5
   *
   * EXAMPLE
   *   > JMT([0, 10, 0], [10, 10, 0], 1)
   *     [0.0, 10.0, 0.0, 0.0, 0.0, 0.0]
   */

  double s_s = start[0];
  double v_s = start[1];
  double a_s = start[2];
  double s_f = end[0];
  double v_f = end[1];
  double a_f = end[2];

  double t_2 = T * T;
  double t_3 = t_2 * T;
  double t_4 = t_3 * T;
  double t_5 = t_4 * T;

  VectorXd C(3);
  C << s_f - (s_s + v_s * T + .5 * a_s * t_2),
      v_f - (v_s + a_s * T),
      a_f - a_s;

  MatrixXd TMatrix(3, 3);

  TMatrix << t_3, t_4, t_5,
      3 * t_2, 4 * t_3, 5 * t_4,
      6 * T, 12 * t_2, 20 * t_3;

  MatrixXd result = TMatrix.inverse() * C;

  return {s_s, v_s, a_s / 2., result(0, 0), result(1, 0), result(2, 0)};
}

int main() {

  // create test cases
  vector<test_case> tc = create_tests();

  bool total_correct = true;

  for (int i = 0; i < tc.size(); ++i) {
    vector<double> jmt = JMT(tc[i].start, tc[i].end, tc[i].T);
    bool correct = close_enough(jmt, answers[i]);
    total_correct &= correct;
  }

  if (!total_correct) {
    std::cout << "Try again!" << std::endl;
  } else {
    std::cout << "Nice work!" << std::endl;
  }

  return 0;
}