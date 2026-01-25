#include<iostream>
#include<cmath>
using namespace std;

class PayOff{
    public:
        virtual double operator()(double Spot) const = 0;
        virtual PayOff* clone() const = 0;
        virtual ~PayOff(){}
};

class PayOffCall: public PayOff{
    public:
        PayOffCall(double Strike_) : Strike(Strike_){}
        virtual double operator()(double Spot) const
        {
            return std::max(Spot - Strike, 0.0);
        }

        virtual PayOff* clone() const
        {
            return new PayOffCall(*this);
        }
    private:
        double Strike;
};   

class VanillaOption
{
    public:
        VanillaOption(const PayOff& payoff_, double Expiry_) : payoff(payoff_.clone()), Expiry(Expiry_){}

        VanillaOption(const VanillaOption& other) : payoff(other.payoff->clone()), Expiry(other.Expiry){}
    
        VanillaOption& operator=(const VanillaOption& other)
        {
            if (this != &other){
                delete payoff;
                payoff = other.payoff->clone();
                Expiry = other.GetExpiry();
            }
            return *this;
        }

        ~VanillaOption()
        {
            delete payoff;
        }

        double OptionPayoff(double Spot) const{
            return (*payoff)(Spot);
        }

        double GetExpiry() const {
            return Expiry;
        }


    private:
        PayOff* payoff;
        double Expiry;

};


int main(){
    PayOffCall callPayoff(100.0);

    VanillaOption option1(callPayoff, 1.0);
    VanillaOption option2(option1);

    cout << option1.OptionPayoff(120.0) << endl;
    cout << option2.OptionPayoff(120.0) << endl;
}

