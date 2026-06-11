#include <iostream>
#include <string>
using namespace std;

int main(){
	string estado;
	cin >> estado;
	if(estado=="roraima"||estado=="acre"||estado=="amapa"||estado=="amazonas"||estado=="para"||estado=="rondonia"||estado=="tocantins"){
		cout << "Regiao Norte\n";
	}
	else{
		cout << "Outra Regiao\n";
	}
	return 0;
}
