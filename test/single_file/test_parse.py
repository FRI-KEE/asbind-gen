import pytest
import analyzer.Analyzer as Analyzer

# Pytest for analyzing a single C++ file

@pytest.mark.single_file
def test_parse_single_file():
    # Path, is under same directory as this test file
    file_path = "test/single_file/test.hpp"
    analyzer = Analyzer.FileAnalyzer(file_path)
    
    # Test parsing the file
    analyzer.parse()
    
    # Test retrieving functions
    functions = analyzer.get_functions()
    print(functions)

    assert "f1" in functions
    assert "f3" in functions
    assert "f2" not in functions  # f2 is not annotated
