/*
 * Problem:
 * Create a macro that allows you to log out lines using a stream format.
 *
 * The macro must allow you to continue the streaming on the returned object and automatically
 * handle flushing and new lines at the end of each statement. For simplicity you can use
 * cout as the stream to print directly to stdout
 *
 * Expected output:
 * [WARNING] - Hello World
 * [ERROR] The quick brown fox
 */
#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::endl;

// Add LOG macro here
#define LOG()

int main(int, char*[]) {
  LOG("WARNING") << "Hello" << " World";
  LOG("ERROR") << "The quick" << " brown " << "fox";
  return 0;
}
