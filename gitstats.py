import subprocess
import os
from collections import defaultdict

def get_git_files():
    """Get a list of all files tracked by Git."""
    files = subprocess.check_output(["git", "ls-files"]).decode("utf-8").splitlines()
    return files

def get_file_blame(filename):
    """Get the blame information for a single file."""
    blame_output = subprocess.check_output(["git", "blame", "--line-porcelain", filename]).decode("utf-8")
    return blame_output

def normalize_name(name):
    """Normalize the author names to handle variations."""
    return ' '.join(name.lower().strip().split())

def merge_similar_names(contributions):
    """Merge similar author names that are subsets of each other."""
    normalized_contributions = defaultdict(int)

    for author in sorted(contributions.keys(), key=len, reverse=True):
        normalized_author = normalize_name(author)
        
        # Check if the current author name is a subset of any other existing normalized author name
        found = False
        for existing_author in normalized_contributions.keys():
            if normalized_author in existing_author:
                normalized_contributions[existing_author] += contributions[author]
                found = True
                break
        
        if not found:
            normalized_contributions[normalized_author] += contributions[author]

    return normalized_contributions

def calculate_contributions():
    files = get_git_files()
    contributions = defaultdict(int)
    total_lines = 0
    
    for file in files:
        try:
            blame_output = get_file_blame(file)
            for line in blame_output.splitlines():
                if line.startswith("author "):
                    author = line.split("author ")[1]
                    contributions[author] += 1
                    total_lines += 1
        except Exception as e:
            print(e)

    # Merge similar names
    contributions = merge_similar_names(contributions)

    return contributions, total_lines

def print_contributions(contributions, total_lines):
    print("------------------------")
    print("Contributions by author:\n")
    
    # Sort authors by the number of lines they contributed, in descending order
    sorted_contributions = sorted(contributions.items(), key=lambda x: x[1], reverse=True)
    
    for author, lines in sorted_contributions:
        percentage = (lines / total_lines) * 100
        print(f"{author} ---> ( {percentage:.2f}% )")
    print("------------------------")

if __name__ == "__main__":
    contributions, total_lines = calculate_contributions()
    print_contributions(contributions, total_lines)
