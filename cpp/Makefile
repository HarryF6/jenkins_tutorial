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
	./$(TARGET)

clang_compile:
	clang++ $(CXXFLAGS) -o $(TARGET) $(SRC)

format_check:
	clang-format --dry-run --Werror $(SRC)

# Limpiar archivos generados
clean:
	rm -f $(TARGET)
