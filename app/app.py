from gui import GUI
from search import FileSearcher
from dirman import DirectoryManager

# Start point of program execution

if __name__ == "__main__":
    dir_manager = DirectoryManager() # Directory Manager
    search_engine = FileSearcher()   # Search engine

    gui = GUI(dir_manager, search_engine)