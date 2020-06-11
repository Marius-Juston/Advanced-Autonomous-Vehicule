#include "classifier.h"
#include <math.h>
#include <string>
#include <vector>
#include <iostream>

using Eigen::ArrayXd;
using std::string;
using std::vector;

// Initializes GNB
GNB::GNB() {
  /**
   * TODO: Initialize GNB, if necessary. May depend on your implementation.
   */
  int n_features = 4;

  for (const string &label: possible_labels) {
    classes[label].std = ArrayXd(n_features);
    classes[label].std << 0, 0, 0, 0;
    classes[label].means = ArrayXd(n_features);
    classes[label].means << 0, 0, 0, 0;
    classes[label].prior = 0;
    classes[label].size = 0;
  }
}

GNB::~GNB() {}

void GNB::train(const vector<vector<double>> &data,
                const vector<string> &labels) {
  /**
   * Trains the classifier with N data points and labels.
   * @param data - array of N observations
   *   - Each observation is a tuple with 4 values: s, d, s_dot and d_dot.
   *   - Example : [[3.5, 0.1, 5.9, -0.02],
   *                [8.0, -0.3, 3.0, 2.2],
   *                 ...
   *                ]
   * @param labels - array of N labels
   *   - Each label is one of "left", "keep", or "right".
   *
   * TODO: Implement the training function for your classifier.
   */

  vector<double> data_point;
  for (int i = 0; i < data.size(); ++i) {
    data_point = data[i];
    classes[labels[i]].means += ArrayXd::Map(data_point.data(), data_point.size());
    ++classes[labels[i]].size;
  }

  for (auto &x : classes) {
    x.second.means /= x.second.size;
  }

  ArrayXd mean;
  ArrayXd x;
  for (int i = 0; i < data.size(); ++i) {
    data_point = data[i];
    mean = classes[labels[i]].means;
    classes[labels[i]].std += ArrayXd::Map(data_point.data(), data_point.size()) - classes[labels[i]].std;
    ++classes[labels[i]].size;
  }
}

string GNB::predict(const vector<double> &sample) {
  /**
   * Once trained, this method is called and expected to return
   *   a predicted behavior for the given observation.
   * @param observation - a 4 tuple with s, d, s_dot, d_dot.
   *   - Example: [3.5, 0.1, 8.5, -0.2]
   * @output A label representing the best guess of the classifier. Can
   *   be one of "left", "keep" or "right".
   *
   * TODO: Complete this function to return your classifier's prediction
   */

  return this->possible_labels[1];
}