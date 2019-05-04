#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {  
    string line;
    int i = 0;
	string j[8];
	string check;
	bool repeat;

    ifstream stats;
    ofstream wStats;

    stats.open ("pokemonStats.txt");
    wStats.open("pokemonCodeStats.txt");
    
    if (stats.is_open() && wStats.is_open()) {
        while (getline(stats, line)){
            if (i <= 6) {
                j[i] = line;
                i ++;
            } else if (i == 7 )  {
                j[i] = line;
                
                if (j[0] != check){
                	wStats << " pkmn = {" << j[0] << ":(stats(hp=" << j[2] << ",attack=" << j[3] << ",defence=" << j[4] << ",sp_attack=" << j[5] << ",sp_defence=" << j[6] << ",speed=" << j[7] << "))} \n";
                	wStats << "return pkmn[" << j[0] << "] \n" << "\n";
				}
                
                check = j[0];
                
                i = 0;
            } else {
                cout << "Something went wrong! i = " << i; 
            }
            
        }

    }

	
    stats.close();
    wStats.close();


    return 0;
}
