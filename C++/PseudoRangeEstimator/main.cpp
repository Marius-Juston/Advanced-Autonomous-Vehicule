#include <algorithm>
#include <iostream>
#include <vector>

#include "helpers.h"

using std::vector;

// set standard deviation of control:
float control_stdev = 1.0f;

// meters vehicle moves per time step
float movement_per_timestep = 1.0f;

// number of x positions on map
int map_size = 25;

// define landmarks
vector<float> landmark_positions{5, 10, 12, 20};

// declare pseudo_range_estimator function
vector<float> pseudo_range_estimator(vector<float> landmark_positions,
                                     float pseudo_position);

int main() {
  // step through each pseudo position x (i)
  for (int i = 0; i < map_size; ++i) {
    auto pseudo_position = float(i);
    // get pseudo ranges
    vector<float> pseudo_ranges = pseudo_range_estimator(landmark_positions,
                                                         pseudo_position);
    // print to stdout
    if (!pseudo_ranges.empty()) {
      for (float pseudo_range : pseudo_ranges) {
        std::cout << "x: " << i << "\t" << pseudo_range << std::endl;
      }
      std::cout << "-----------------------" << std::endl;
    }
  }

  return 0;
}

// TODO: Complete pseudo range estimator function
vector<float> pseudo_range_estimator(vector<float> landmark_positions,
                                     float pseudo_position) {
  // define pseudo observation vector
  vector<float> pseudo_ranges;

  // loop over number of landmarks and estimate pseudo ranges
  for (float landmark_position : landmark_positions) {
    if (landmark_position > pseudo_position) {
      pseudo_ranges.push_back(landmark_position - pseudo_position);
    }
  }

  // sort pseudo range vector

  return pseudo_ranges;
}