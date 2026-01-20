#include "PayOff2.h"
#include <minmax.h>

PayOffCall::PayOffCall(double Strike_):Strike(Strike_){}

// const after a member function means that the function does not modify the observable state of the object on which it is called
double PayOffCall::operator()(double Spot) const{
    return max(Spot-Strike, 0.0);
}

PayOffPut::PayOffPut(double Strike_):Strike(Strike_){}

// const after a member function means that the function does not modify the observable state of the object on which it is called
double PayOffPut::operator()(double Spot) const{
    return max(Strike-Spot,0.0);
}

