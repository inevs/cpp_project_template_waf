#include "gmock/gmock.h"
#include "hello.h"

TEST(Hello, ReturnsHelloString) {
	Hello hello;
	std::string msg = hello.sayHello();
	ASSERT_THAT(msg, testing::Eq("Hello World\n"));
}