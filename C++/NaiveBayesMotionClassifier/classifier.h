#ifndef CLASSIFIER_H
#define CLASSIFIER_H

#include <string>
#include <vector>
#include <map>
#include "Dense"

using Eigen::ArrayXd;
using std::string;
using std::vector;

class GNB {
 public:
  /**
   * Constructor
   */
  GNB();

  /**
   * Destructor
   */
  virtual ~GNB();

  /**
   * Train classifier
   */
  void train(const vector<vector<double>> &data,
             const vector<string> &labels);

  /**
   * Predict with trained classifier
   */
  string predict(const vector<double> &sample);

  vector<string> possible_labels = {"left", "keep", "right"};

  struct Class {
    ArrayXd means;
    ArrayXd std;
    double prior;
    double conditional_probability;
    int size;
  };

  std::map<std::string, Class> classes;
};

#endif  // CLASSIFIER_H