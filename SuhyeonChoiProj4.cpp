//This project is about converting celsius to farenheit in the given depth.
#include <iostream>

using namespace std;

void print_introduction(void);
double celsius_at_depth(double depth);
double celsius_to_farenheit(double celsius);
void conclusion(double depth);

int main() {
	char ans;
	double depth;
	do {
		print_introduction();
		cout << "Enter the depth: ";
		cin >> depth;
		conclusion(depth);
		cout << "Would you like to do it agian? (Y/N):";
		cin >> ans;
		cout << endl;
	} while (ans == 'y' || ans == 'Y');
}
void print_introduction() {
	cout << "Hello! The program will tell you the temperature of"
		<< "the earth at any depth" << endl;
	return;
}

double celsius_at_depth(double depth) {
	double celsius;
	celsius = 10 * depth + 20;
	return celsius;
}

double celsius_to_farenheit(double celsius) {
	double farenheit;
	farenheit = 1.8 * celsius + 32;
	return farenheit;
}

void conclusion(double depth) {
	cout << "The temperature of the earth at a depth of " << depth
		<< " KM is " << celsius_at_depth(depth) << " in Celcius, and "
		<< celsius_to_farenheit(celsius_at_depth(depth)) << " in Fareneheit." << endl;
}