#include <iostream>
#include <vector>

using std::vector;

// initialize priors assuming vehicle at landmark +/- 1.0 meters position stdev
vector<float> initialize_priors(int map_size, vector<float> landmark_positions,
                                float position_stdev);

int main() {
  // set standard deviation of position
  float position_stdev = 1.0f;

  // set map horizon distance in meters 
  int map_size = 25;

  // initialize landmarks
  vector<float> landmark_positions {5, 10, 20};

  // initialize priors
  vector<float> priors = initialize_priors(map_size, landmark_positions,
                                           position_stdev);

  for (float &prior : priors)
    std::cout << prior << ' ';
  std::cout << std::endl;

  return 0;
}

vector<float> initialize_priors(int map_size, vector<float> landmark_positions,
                                float position_stdev) {

  // initialize priors assuming vehicle at landmark +/- 1.0 meters position stdev

  // set all priors to 0.0
  vector<float> priors(map_size, 0.0);

  float sum = 0;
  float initial_prior = 1.0;

  for (auto landmark: landmark_positions) {
    for (int position = landmark - position_stdev; position <= (landmark + position_stdev); ++position) {
      if (position >= 0 && position < map_size) {
        if (priors[position] != initial_prior) {
          priors[position] = initial_prior;
          sum += initial_prior;
        }
      }
    }
  }

  for (auto landmark: landmark_positions) {
    for (int position = landmark - position_stdev; position <= (landmark + position_stdev); ++position) {
      if (position >= 0 && position < map_size) {
        priors[position] = initial_prior / sum;
      }
    }
  }

  return priors;
}