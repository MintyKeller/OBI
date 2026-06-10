#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
	double alc, gas, rendAlc, rendGas;
	cin>>setprecision(2)>>alc>>gas>>rendAlc>>rendGas;
	if(0.01<=alc&&0.01<=gas&&0.01<=rendAlc&&0.01<=rendGas&&alc<=10&&gas<=10&&rendAlc<=20&&rendGas<=20){
		alc = round(alc*100)/100;
		gas = round(gas*100)/100;
		rendAlc = round(rendAlc*100)/100;
		rendGas = round(rendGas*100)/100;
		if(alc*rendGas>=gas*rendAlc){
			cout<<"G\n";
		}
		else{
			cout<<"A\n";
		}
	}
}
