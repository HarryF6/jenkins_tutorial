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
execute:
	./hello

clange_format:
	$(SRC) $(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC) -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++

# Limpiar archivos generados
clean:
	rm -f $(TARGET)
