#ifndef MINMAX_H
#define MINMAX_H

template<class T> 
T max(a,b)
{
    return (a<b) ? b : a;
}


template<class T>
T min(a,b)
{
    return (a>b) ? b : a;
}
#endif