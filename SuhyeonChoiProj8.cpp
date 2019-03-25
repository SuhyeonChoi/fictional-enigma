//Implement functions to apply methods of vector class, cctype library, and string class
//
//Created by Suhyeon Choi on 04/23/17

#include <iostream>
#include <string>
#include <vector>
#include <cctype>

using namespace std;

void get_scores(vector<int> &v);
//precondition: none
//postcondition: scores from 0 to 100 will be assigned to a vector from keyboard, when user enter a negative value, 
//               the input process finishes.

void print_stats(vector<int> &v);
//precondition: v contains 0 to 100
//postcondition: the minimum ,maximum, total scores, and average scores will be print out.

bool is_palindrome(string &sentence);
//precondition: string is a sentence
//postcondition: returns true if sentence is a palidrome and false otherwise.

int main()
{
	//solve problem 1
	vector<int> scores;
	get_scores(scores);
	print_stats(scores);

	//solve problem 2
	string s;
	cout << "Enter a sentence, then I will tell you if it is a palindrome: \n";
	getchar();
	getline(std::cin, s);
	if (is_palindrome(s))
		cout << "The sentence \"" << s << "\" is a palindrome\n";
	else
		cout << "The sentence \"" << s << "\" is NOT a palindrome\n";
	return 0;
}

void get_scores(vector<int> &v) {
	int score;
	cout << "Enter scores, then enter -1 to stop: ";
	do {
		cin >> score;
		if (score >= 0)
			v.push_back(score); //add the score the vector v
	} while (score >= 0);
}

void print_stats(vector<int> &v) {
	int low_Score = 101, high_Score = -1, total_Score = 0;
	size_t size = v.size(); // how many elements in v
	if (size == 0) {
		cout << "There is no test score\n";
		return;
	}else {
		for (size_t i = 0; i < size; i++) //step through the vector
		{
			if (v[i] < low_Score)
				low_Score = v[i];
			if (v[i] > high_Score)
				high_Score = v[i];
			total_Score += v[i];
		}
		cout << "There are " << size << " scores\n";
		cout << "The highest score is " << high_Score << endl;
		cout << "The lowest score is " << low_Score << endl;
		cout << "The average score is " << 1.0*total_Score / size << endl;
	}
}

	bool is_palindrome(string &sentence)
		{
		int left = 0; //left index of characters in sentence string
		int right = (int)sentence.length() - 1;//right index of characters in sentence string 
		while (left < right) {
			while (!isalpha(sentence[left])) {
				left++;
				if (left == right) return true;
			}
			while (!isalpha(sentence[right])) {
				right--;
				if (left == right) return true;	
			}
			if (toupper(sentence[left]) != toupper(sentence[right]))//compare if two letters are the same
				return false;//is not a palindrome
			left++;
			right--;
		}
		return true;
	}