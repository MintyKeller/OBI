#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
	double banca1, banca2, banca3;
	double p1, p2, desconto, juros;
	cin >>fixed>>setprecision(2)>>p1>>p2>>desconto>>juros;
	banca1 = round(((p1+p2)+((p1+p2)*juros*0.01)-((p1+p2)*desconto*0.01))*100)/100;
	cin >>setprecision(2)>>p1>>p2>>desconto>>juros;
	banca2 = round(((p1+p2)+((p1+p2)*juros*0.01)-((p1+p2)*desconto*0.01))*100)/100;
	cin >>setprecision(2)>>p1>>p2>>desconto>>juros;
	banca3 = round(((p1+p2)+((p1+p2)*juros*0.01)-((p1+p2)*desconto*0.01))*100)/100;
	if(min({banca1, banca2, banca3})==banca1){
		cout<<fixed<<setprecision(2)<<"R$ "<<banca1<<" Banca 1\n";
	}
	if(min({banca1, banca2, banca3})==banca2){
		cout<<fixed<<setprecision(2)<<"R$ "<<banca2<<" Banca 2\n";
	}
	if(min({banca1, banca2, banca3})==banca3){
		cout<<"R$ "<<fixed<<setprecision(2)<<banca3<<" Banca 3\n";
	}
	return 0;
}
