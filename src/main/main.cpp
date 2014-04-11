#include <iostream>
#include "hello.h"

int main(int argc, char const *argv[]) {
	Hello hello;
	std::string msg = hello.sayHello();
	std::cout << msg;
	return 0;
}