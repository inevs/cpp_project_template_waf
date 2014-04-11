#include "gmock/gmock.h"

TEST(Hello, ReturnsHelloString) {
	std::string msg = "Hello";
	ASSERT_THAT(msg, testing::Eq("Hello"));
}