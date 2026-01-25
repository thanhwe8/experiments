/* note:
in C++, a virtual clone is a design pattern that provides a polymorphic way to copy objects
when you only have access to them through base-class pointer or reference.

It addresses a fundamental limitation of C++: constructors cannot be virtual, so copying via 
a base pointer normally causes object slicing
*/

#include <iostream>
using namespace std;

struct Point{
    double x, y;
};

class Shape {
    public:
        virtual ~Shape() = default;
        virtual Shape* clone() const = 0;     
};


class Circle : public Shape
{
    public:
        double r;
        Circle(double r_): r(r_){}

        Shape* clone() const override
        {
            return new Circle(*this);
        }
};


int main()
{
    Point *p1 = new Point{1.0, 2.0};
    Point *p2 = new Point(*p1); // copy via pointer

    cout << p2 -> x << endl;

    Shape *s1 = new Circle{5.0};
    Shape *s2 = s1 -> clone(); // object slicing if we use new without clone() --> only Shape subobject is copied. The circle part is lost
    // undefined behaviour if shape is abstract

    cout << s2->r << endl; 
}


201 681 4527

Esdras



