# Nombre del ejecutable
TARGET = hello

# Compilador
CXX = g++

# Archivos fuente
SRC = hello_world.cpp

# Flags de compilación
CXXFLAGS = -Wall -std=c++11
COVERAGE_FLAGS = -fprofile-arcs -ftest-coverage

# Regla por defecto
all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

execute:
	./$(TARGET)

cclang:
	clang++ $(CXXFLAGS) -o $(TARGET) $(SRC)

format:
	clang-format -i $(SRC)

coverage: 
	
	$(CXX) $(CXXFLAGS) $(COVERAGE_FLAGS) -o $(TARGET) $(SRC)
	

check:
	clang-format --dry-run --Werror $(SRC)

# Limpiar archivos generados
clean:
	rm -f $(TARGET) *.gcda *.gcno *.gcov
