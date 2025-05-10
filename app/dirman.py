# Directory Manager

class DirectoryManager:
    def __init__(self):
        self.directories = []

    # Add directory
    def add(self, directory):
        if directory not in self.directories:
            self.directories.append(directory)
        else:
            print("Directory already in list.")

    # Remove directory
    def remove(self, directory):
        if directory not in self.directories:
            print("Directory not in list.")
        else:
            self.directories.remove(directory)

    # Get directories
    def get_all(self):
        return self.directories
    
    # Set directories
    def set_all(self, directories):
        self.directories = directories