#include <iostream>
using namespace std;

int main(){
	int saida, duracao, fuso, chegada;
		cin>>saida>>duracao>>fuso;
		chegada = saida+duracao+fuso;
		while(chegada>=24){
			chegada=chegada-24;
		}
		while(chegada<0){
			chegada = chegada+24;
		}
		cout<<chegada<<"\n";
}
