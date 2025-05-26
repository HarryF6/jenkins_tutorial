# Nombre del ejecutable
TARGET = hello

# Compilador
CXX = g++

# Archivos fuente
SRC = hello_world.cpp

# Flags de compilación
CXXFLAGS = -Wall -std=c++11

# Regla por defecto
all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

test:
      g++ -std=c++11 helloTest.cpp -lcppunit -o helloTest
      chmod +x hello
      ./helloTest

# Limpiar archivos generados
clean:
	rm -f $(TARGET)
