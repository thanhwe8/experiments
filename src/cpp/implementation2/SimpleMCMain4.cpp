#include "SimpleMC2.h"
#include <iostream>
using namespace std;

int main()
{
    double Expiry;
    double Strike;
    double Spot;
    double Vol;
    double r;
    unsigned long NumberOfPaths;
    unsigned long optionType; // 1 for Put, 0 for Call

    Expiry = 1;
    Strike = 100.0;
    Spot = 100.0;
    Vol = 0.3;
    r = 0.05;
    NumberOfPaths = 10000;
    optionType = 0;
    
    PayOff *thePayOffPtr;

    if (optionType == 0)
        thePayOffPtr = new PayOffCall(Strike);
    else
        thePayOffPtr = new PayOffPut(Strike);

    double result = SimpleMonteCarlo2(*thePayOffPtr, Expiry, Spot, Vol, r, NumberOfPaths);
    
    cout << "The price is: " << result << endl;
    delete thePayOffPtr;

    return 0;
}