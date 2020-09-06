#include <iostream>
#include <string>

using namespace std;

string reverse(string::iterator& it){
	char head = *it;
	it++;
	if (head == 'w' || head == 'b')
		return string(1, head);
	string upperLeft = reverse(it);
	string upperRight = reverse(it);
	string lowerLeft = reverse(it);
	string lowerRight = reverse(it);
	return string("x") + lowerLeft + lowerRight + upperLeft + upperRight;
}

int main(void){
	int testCase;
	cin >> testCase;
	while (testCase--) {
		string picture;
		cin >> picture;
		string::iterator it = picture.begin();
		cout<<reverse(it)<<"\n";
	}
}