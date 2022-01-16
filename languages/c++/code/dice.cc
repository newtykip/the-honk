#include <iostream>
#include <vector>

class Dice {
	private:
		int randomInteger(int lowerBound, int upperBound) {
			return rand() % (upperBound - lowerBound - 1) + 1;
		}

	public:
		int sides;

		// Constructor
		Dice(int sideNum) {
			// Set the number of sides
			sides = sideNum;
		}

		// Roll the dice
		int roll() {
			return randomInteger(1, sides);
		}

		// Roll the dice many times and return thre result in a vector
		std::vector<int> rollMany(int times) {
			std::vector<int> rolls{};

			for (int i = 0; i < times; i++) {
				int rolled = roll();
				rolls.push_back(rolled);
			}

			return rolls;
		}
};

// Print a vector of integers onto one line
void printResults(std::vector<int> data) {
	int length = data.size();

	for (int i = 0; i < length; i++) {
		std::string out = std::to_string(data[i]);
		if (i != length - 1) out += ", ";

		std::cout << out;
	}
}

int main() {
	// Seed the RNG
	srand((unsigned)time(nullptr));

	// Instantiate the dice
	Dice six(6);
	Dice twenty(20);

	// Roll them
	std::vector<int> sixRolled = six.rollMany(10);
	std::vector<int> twentyRolled = twenty.rollMany(10);

	// Display their outputs
	std::cout << "Six Sided Dice:\n";
	printResults(sixRolled);
	std::cout << "\n\nTwenty Sided Dice:\n";
	printResults(twentyRolled);
}
