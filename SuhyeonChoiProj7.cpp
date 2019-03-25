//Implement some functions to handle arrays

#include <iostream>
using namespace std;

void fill_array(int arr[], int size)
//precondition: The arr has actual size that is greater than or equal to size
//postcondition: arr[0],  ..., arr[size-1] is filled from keyboard
{
	int integer;
	for (int i = 0; i < size; i++) {
		cout << "integer " << i << ":";
		cin >> integer;
		arr[i] = integer;
		cout << endl;
	}
}

void print_array(int arr[], int size)
//precondition: The arr has actual size that is greater than or equal to size
//postcondition: arr[0], ..., arr[size-1] is printed to screen with 5 elements per line
{
	for (int i = 0; i < size; i++) {
		cout << arr[i] << "  ";
		if (i % 5 == 4) {
			cout << endl;
		}
	}
	cout << endl;
}

int linear_search(int arr[], int size, int key)
//precondition: arr has given size
//postcondition: The index of first occurrence of key in arr is returned. If the key cannot be found in arr, -1 is returned.
{
	for (int i = 0; i < size; i++) {
		if (arr[i] == key) {
			return i;
		}
	}
	return -1;
}

void swap(int arr[], int idx1, int idx2)
//precondition: arr is smaller than idx 1 and idx 2
//postcondition: the value of arr_idx are swapped.
{
	int tmp = arr[idx1];
	arr[idx1] = arr[idx2];
	arr[idx2] = tmp;
}
void select_sort(int arr[], int size)
//precondition: arr has given size
//postcondition: the elements in arr are rearranged from least to largest
{
	int min_idx, tmp;
	for (int step = 0; step < size - 1; step++) {
		min_idx = step;
		for (int j = step; j < size; j++) {
			if (arr[min_idx] > arr[j]) {
				min_idx = j;
			}
		}
		swap(arr, step, min_idx);
	}
}

void insert_sort(int arr[], int size)
//precondition: arr has given size
//postcondition: the elements in arr are rearranged from least to largest
{
	for (int target = 0; target < size; target++) {
		for (int comp = target - 1; comp >= 0; comp--) {
			if (arr[comp + 1] <= arr[comp]) {
				swap(arr, comp + 1, comp);
			}
			else {
				break;
			}
		}
	}
}

void bubble_sort(int arr[], int size)
//precondition: arr has given size
//postcondition: the elements in arr are reagrranged from least to largest
{
	for (int step = 0; step<size - 1; step++) {
		for (int i = 0; i<size - 1; i++) {
			if (arr[i] > arr[i + 1]) {
				swap(arr, i, i + 1);
			}
		}
	}
}


void menu()
//menu for user to choose
{
	cout << "********************************\n";
	cout << "*            Menu              *\n";
	cout << "* 1. Test Linear Search        *\n";
	cout << "* 2. Test Select Sort          *\n";
	cout << "* 3. Test Insert Sort          *\n";
	cout << "* 4. Test Bubble Sort          *\n";
	cout << "* 5. Quit                      *\n";
	cout << "********************************\n";

}

int main() {
	int choice;
	int a[9];
	do {
		menu();
		cout << "Enter your choice: ";
		cin >> choice;
		switch (choice)
		{
		case 1:
		{
			fill_array(a, 9);
			cout << "Enter the key you want to search: ";
			int key;
			cin >> key;
			int index = linear_search(a, 9, key);
			if (index == -1)
				cout << "The key " << key << " is not in array\n";
			else
				cout << "The key " << key << " is #" << (index + 1) << " element in array\n";
			break;
		}
		case 2:
		{
			fill_array(a, 9);
			select_sort(a, 9);
			cout << "After sort, the array is:\n";
			print_array(a, 9);
			break;
		}
		case 3:
		{
			fill_array(a, 9);
			insert_sort(a, 9);
			cout << "After sort, the array is:\n";
			print_array(a, 9);
			break;
		}
		case 4:
		{
			fill_array(a, 9);
			bubble_sort(a, 9);
			cout << "After sort, the array is:\n";
			print_array(a, 9);
			break;
		}
		case 5:
		{
			cout << "Thank you for using the array functions\n";
			break;
		}
		default:
		{
			cout << "Wrong choice. Please choose from menu: ";
			break;
		}
		}
	} while (choice != 5);
	return 0;
}