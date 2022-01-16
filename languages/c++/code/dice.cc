#include <iostream>
#include <vector>
using namespace std;

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
		vector<int> rollMany(int times) {
			vector<int> rolls{};

			for (int i = 0; i < times; i++) {
				int rolled = roll();
				rolls.push_back(rolled);
			}

			return rolls;
		}
};

// Print a vector of integers onto one line
void printResults(vector<int> data) {
	int length = data.size();

	for (int i = 0; i < length; i++) {
		string out = to_string(data[i]);
		if (i != length - 1) out += ", ";

		cout << out;
	}
}

int main() {
	// Seed the RNG
	srand((unsigned)time(nullptr));

	// Instantiate the dice
	Dice six(6);
	Dice twenty(20);

	// Roll them
	vector<int> sixRolled = six.rollMany(10);
	vector<int> twentyRolled = twenty.rollMany(10);

	// Display their outputs
	cout << "Six Sided Dice:" << endl;
	printResults(sixRolled);
	cout << endl << endl << "Twenty Sided Dice:" << endl;
	printResults(twentyRolled);
}
