#include <iostream>
using namespace std;

int main(){
	int e, d, r;
	cin >> e >> d;
	if(e>d){
		r = e+d;
	}
	else{
		r= 2*(d-e);
	}
	cout << r << "\n";
	return 0;
}
