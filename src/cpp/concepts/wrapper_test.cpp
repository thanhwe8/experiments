#include<iostream>
#include<algorithm>
#include<stdexcept>

template<typename T>
class Wrapper
{
public:
    explicit Wrapper(T obj) : obj_(std::move(obj)){}

    double operator()(double x) const
    {
        if (x < 0.0)
            throw std::invalid_argument("Input must be non-negative");

        double result = obj_(x);

        std::cout << "Wrapper input = " << x << " Output = " << result << std::endl;

        return result;
    }
    

private:
    T obj_;
};


class CallPayoff{
public:
    explicit CallPayoff(double Strike) : strike_(Strike){}
    double operator()(double spot) const
    {
        return std::max(spot - strike_, 0.0);
    }
private:
    double strike_;
};


int main()
{
    CallPayoff call(100.0);
    Wrapper<CallPayoff> safeCall(call);

    double s1 = safeCall(120.0);
    double s2 = safeCall(100.0);

    return 0;



}


