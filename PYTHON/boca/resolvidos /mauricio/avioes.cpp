#include <iostream>
using namespace std;

int main(){
	int competidores, papeis, papnec;
	cin >> competidores >> papeis >> papnec;
	if(1<=competidores && 1<=papeis && 1<=papnec && competidores <=1000 && papeis<=1000 && papnec<=1000){
		if((competidores*papnec)>papeis){
			cout << "N\n";
		}
		else{
			cout << "S\n";
		}
	}
	return 0;
}
