#include "libx.hpp"
#include <iostream>

void Libx::Printx() const {
  std::cout << x << std::endl;
}

int main() {
  Libx a;
  a.x = 100;
  a.Printx();
  return 0;
}

