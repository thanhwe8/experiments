#ifndef MINMAX_H
#define MINMAX_H

template<class T> 
T max(T a,T b)
{
    return (a<b) ? b : a;
}


template<class T>
T min(T a,T b)
{
    return (a>b) ? b : a;
}
#endif