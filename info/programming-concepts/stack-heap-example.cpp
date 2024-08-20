#include <iostream>
#include <string>
using namespace std;

struct Fruit
{
    string name;
    int age;
};

Fruit* createFruit(string name, int age);

int main()
{
    Fruit* someFruit = createFruit("Anana", 5);
    cout << "Crazy pointer: " << &someFruit << endl; //0x7fff9dbb1ab0

    cout << "Fruit's name is: " << someFruit->name << endl; //Anana 
    cout << "Reference: " << &someFruit << endl; //0x7fff9dbb1ab0

    // Delete memory in Heap
    delete someFruit;
    someFruit = nullptr; // Set pointer to nullptr after deletion
    cout << "Heap (data after delete): " << someFruit << endl; //0
    cout << "Heap (pointer after delete): " << &someFruit << endl; //0x7fff9dbb1ab0

    return 0;
}

Fruit* createFruit(string name, int age)
{
    // Heap
    Fruit* fruit = new Fruit;
    fruit->name = name;
    fruit->age = age;
    cout << &fruit  << endl; //0x7fff9dbb1ab0

    return fruit;
}
