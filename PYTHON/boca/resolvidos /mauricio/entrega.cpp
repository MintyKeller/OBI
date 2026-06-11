#include <iostream>
using namespace std;

bool comp(int x, int y, int z);

int main(){
	int a,b,c;
	cin >> a >> b >> c;
	if(1<=a&&1<=b&&1<=c&&a<=1000&&b<=1000&&c<=1000){
		if(a==b&&b==c){
			cout<<3<<"\n";
		}
		else if(comp(a,b,c)||comp(b,c,a)||comp(c,a,b)||comp(a,c,b)||comp(b,a,c)||comp(c,b,a)){
			cout<<1<<"\n";
		}
		else{
			cout<<2<<"\n";
		}
	}
	return 0;
}
bool comp(int x,int y,int z){
	if(x==y){
		if((x+y)<z){
			return true;
		}
		else{
			return false;
		}
	}
	else if(x<y){
		if(y<z){
			return true;
		}
		else{
			return false;
		}
	}
	else{
		return false;
	}
}
