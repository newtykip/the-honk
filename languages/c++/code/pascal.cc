#include <iostream>
#include <vector>
using namespace std;

// Calculate Pascal's triangle
vector<vector<long long>> pascal(int rowCount) {
	vector<vector<long long>> rows{{1}};
	
	for (int i = 0; i < rowCount; i++) {
		vector<long long> previousRow = rows[rows.size() - 1];
		vector<long long> newRow{1};

		for (int j = 0; j < previousRow.size() - 1; j++) {
			newRow.push_back(previousRow[j] + previousRow[j + 1]);
		}

		newRow.push_back(1);
		rows.push_back(newRow);
	}

	return rows;
}

// Find the length of a vector if it were outputted as a string with a space between each value
int vectorStringLength(vector<long long> vector) {
	int value = vector.size();

	for (int i = 0; i < vector.size(); i++) {
		value += to_string(vector[i]).size();
	}

	return value;
}

// Draw Pascal's Triangle
void drawPascalTriangle(int rowCount) {
	vector<vector<long long>> pascalsTriangle = pascal(rowCount);
	int bottomRowSize = vectorStringLength(pascalsTriangle[pascalsTriangle.size() - 1]);

	for (int i = 0; i < pascalsTriangle.size() - 1; i++) {
		vector<long long> currentRow = pascalsTriangle[i];

		int rowSize = vectorStringLength(currentRow);

		int sizeDifference = bottomRowSize - rowSize;

		string spacing = "";

		for (int j = 0; j < sizeDifference / 2; j++) {
			spacing += " ";
		}

		for (int j = 0; j < currentRow.size(); j++) {
			if (j == 0) {
				cout << spacing;
			}

			cout << to_string(currentRow[j]) + " ";

			if (j == currentRow.size() - 1) {
				cout << spacing;
			}
		}

		if (i != pascalsTriangle.size() - 1) {
			cout << endl;
		}
	}
}

int main() {
	cout << "How many rows of Pascal's Triangle would you like to calculate? ";

	int rowCount;
	cin >> rowCount;

	drawPascalTriangle(rowCount);
}
