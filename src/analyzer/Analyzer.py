# Analyzer for C++ sources

from pathlib import Path
import clang.cindex

class FileAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.index = clang.cindex.Index.create()
        self.translation_unit = None

    def parse(self):
        if not self.file_path.exists() or not self.file_path.is_file():
            raise FileNotFoundError(f"File {self.file_path} does not exist or is not a file.")
        
        self.translation_unit = self.index.parse(str(self.file_path))
        if not self.translation_unit:
            raise RuntimeError(f"Failed to parse {self.file_path}")

    def get_functions(self):
        if not self.translation_unit:
            raise RuntimeError("Translation unit is not parsed. Call parse() first.")
        
        functions = []
        for cursor in self.translation_unit.cursor.get_children():
            if cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                functions.append(cursor.spelling)
        return functions
