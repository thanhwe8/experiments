#include<iostream>
using namespace std;

enum Color {
    Red,
    Green,
    Blue,
};


enum class ErrorCode{
    OK = 0,
    NotFound = 404,
    ServerError = 500,
};

void handle(ErrorCode code){
    if (code == ErrorCode::NotFound){
        cout << "Not Found ErrorCode" << endl;
    } else if (code == ErrorCode::OK){
        cout << "OK no ErrorCode" << endl;
    } else {
        cout << "ServerError" << endl;
    }
}

enum class Day {
    Mon, Tue, Wed, Thu, Fri
};


enum Level{
    LOW = 25,
    MEDIUM = 50,
    HIGH = 75,
};


int main(){
    MEDIUMjkkkllColo
    if (c == Red){
        cout << "Color is red" << endl;
    }

    Level myVar = MEDIUM;
    cout << myVar << endl;

    myVar = HIGH;
    cout << myVar << endl;

    return 0;
}

