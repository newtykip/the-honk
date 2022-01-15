#include <iostream>
#include <vector>
using namespace std;

// Calculate Pascal's triangle
vector<vector<int>> pascal(int rowCount) {
	vector<vector<int>> rows{{1}};
	
	for (int i = 0; i < rowCount; i++) {
		vector<int> previousRow = rows[rows.size() - 1];
		vector<int> newRow{1};

		for (int j = 0; j < previousRow.size() - 1; j++) {
			newRow.push_back(previousRow[j] + previousRow[j + 1]);
		}

		newRow.push_back(1);
		rows.push_back(newRow);
	}

	return rows;
}

int vectorStringLength(vector<int> vector) {
	int value = vector.size();

	for (int i = 0; i < vector.size(); i++) {
		value += to_string(vector[i]).size();
	}

	return value;
}

int main() {
	vector<vector<int>> pascalsTriangle = pascal(10);
	int bottomRowSize = vectorStringLength(pascalsTriangle[pascalsTriangle.size() - 1]);

	// Output the triangle
	for (int i = 0; i < pascalsTriangle.size(); i++) {
		vector<int> currentRow = pascalsTriangle[i];
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
