#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
	int per;
	double sal;
	cin >> sal;
	sal = round(sal*100)/100;
	if(sal>=0 && sal<=400){
		per=15;
	}
	else if(sal>400 && sal<=800){
		per=12;
	}
	else if(sal>800 && sal<=1200){
		per=10;
	}
	else if(sal>1200 && sal<=2000){
		per=7;
	}
	else if(sal>2000){
		per=4;
	}
	double reaj = round((sal*(per*0.01))*100)/100;
	sal = sal + reaj;
	cout << fixed << setprecision(2)<<"Novo salario: "<< sal << "\nReajuste ganho: " << reaj << "\n" << "Em percentual: " << per << "%\n";

}
