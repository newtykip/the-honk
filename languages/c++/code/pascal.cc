#include <iostream>
#include <vector>

// Calculate Pascal's triangle
std::vector<std::vector<long long>> pascal(int rowCount) {
	std::vector<std::vector<long long>> rows{{1}};
	
	for (int i = 0; i < rowCount; i++) {
		std::vector<long long> previousRow = rows[rows.size() - 1];
		std::vector<long long> newRow{1};

		for (int j = 0; j < previousRow.size() - 1; j++) {
			newRow.push_back(previousRow[j] + previousRow[j + 1]);
		}

		newRow.push_back(1);
		rows.push_back(newRow);
	}

	return rows;
}

// Find the length of a vector if it were outputted as a string with a space between each value
int vectorStringLength(std::vector<long long> vector) {
	int value = vector.size();

	for (int i = 0; i < vector.size(); i++) {
		value += std::to_string(vector[i]).size();
	}

	return value;
}

// Draw Pascal's Triangle
void drawPascalTriangle(int rowCount) {
	std::vector<std::vector<long long>> pascalsTriangle = pascal(rowCount);
	int bottomRowSize = vectorStringLength(pascalsTriangle[pascalsTriangle.size() - 1]);

	for (int i = 0; i < pascalsTriangle.size() - 1; i++) {
		std::vector<long long> currentRow = pascalsTriangle[i];

		int rowSize = vectorStringLength(currentRow);

		int sizeDifference = bottomRowSize - rowSize;

		std::string spacing = "";

		for (int j = 0; j < sizeDifference / 2; j++) {
			spacing += " ";
		}

		for (int j = 0; j < currentRow.size(); j++) {
			if (j == 0) {
				std::cout << spacing;
			}

			std::cout << std::to_string(currentRow[j]) + " ";

			if (j == currentRow.size() - 1) {
				std::cout << spacing;
			}
		}

		if (i != pascalsTriangle.size() - 1) {
			std::cout << "\n";
		}
	}
}

int main() {
	std::cout << "How many rows of Pascal's Triangle would you like to calculate? ";

	int rowCount;
	std::cin >> rowCount;

	drawPascalTriangle(rowCount);
}
