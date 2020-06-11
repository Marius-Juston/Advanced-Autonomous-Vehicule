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
    x = ArrayXd::Map(data_point.data(), data_point.size());
    mean = classes[labels[i]].means;
    classes[labels[i]].std += (x - mean) * (x - mean);
  }

  for (auto &item : classes) {
    item.second.std = (item.second.std / item.second.size).sqrt();
    item.second.prior = (double) item.second.size / labels.size();
  }

  for (const auto &item : classes) {
    std::cout << item.first << std::endl;
    std::cout << "Means: ";

    for (int i = 0; i < item.second.means.size(); ++i) {
      std::cout << item.second.means(i) << ", ";
    }
    std::cout << std::endl << "Std: ";

    for (int i = 0; i < item.second.std.size(); ++i) {
      std::cout << item.second.std(i) << ", ";
    }

    std::cout << std::endl << "Prior: " << item.second.prior << std::endl << "Size: " << item.second.size << std::endl
              << std::endl;

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

  std::map<std::string, double> conditional_probabilities;
  ArrayXd means;
  ArrayXd std;
  ArrayXd sample_array;

  double max_value = -1;
  string max_label;
  for (const std::string &label: possible_labels) {
    means = classes[label].means;
    std = classes[label].std.pow(2);
    sample_array = ArrayXd::Map(sample.data(), sample.size());

    ArrayXd top = Eigen::exp(-(sample_array - means).pow(2) / (2 * std));
    ArrayXd bottom = 1. / (2 * M_PI * std).sqrt();

    conditional_probabilities[label] = result;
    double result = (top * bottom).prod() * classes[label].prior;

    if (result > max_value) {
      max_value = result;
      max_label = label;
    }
  }

  return max_label;
}