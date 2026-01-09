#!/usr/bin/env python3
"""
Script to create numbered hadith JSON files (001.json, 002.json, etc.)
"""
import os
import json

def create_hadith_files(count, directory="books/bukhari/hadiths"):
    """
    Create numbered hadith JSON files from 001 to the specified count.
    
    Args:
        count (int): Number of files to create
        directory (str): Directory where files will be created
    """
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Template for hadith JSON structure (you can modify this as needed)
    hadith_template = [{
        "book_id": None,
        "chapter_id": None,
        "hadith_id": None,

        "arabic": "…",
        "english": "…",
        "bangla": "…",

        "tags": ["demo1", "demo2", "demo3"],

        "grades": [
            {
            "grade": "sahih",
            "authority": "al-Bukhari",
            "reference": "Sahih al-Bukhari, Hadith 1"
            },
            {
            "grade": "sahih",
            "authority": "Muslim",
            "reference": "Sahih Muslim 1907"
            }
        ]
    }]
    
    for i in range(1, count + 1):
        # Format number with leading zeros (001, 002, etc.)
        file_number = str(i).zfill(3)
        file_path = os.path.join(directory, f"{file_number}.json")
        
        # Update template with current ID
        hadith_data = hadith_template.copy()
        hadith_data["id"] = i
        
        # Write JSON file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(hadith_data, f, ensure_ascii=False, indent=2)
        
        print(f"Created: {file_path}")
    
    print(f"\n✓ Successfully created {count} hadith files")

if __name__ == "__main__":
    # Get user input
    try:
        num_files = int(input("How many hadith files do you want to create? "))
        if num_files < 1:
            print("Please enter a positive number")
        else:
            create_hadith_files(num_files)
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled")
