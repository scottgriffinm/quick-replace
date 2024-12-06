import os

def replace_text_in_files(replacements, file_extensions):
    """
    Replaces exact matches of text in all files with specified extensions in the current working directory.

    :param replacements: List of tuples (textToFind, textToReplace)
    :param file_extensions: List of file extensions to filter files (e.g., ['html', 'css', 'js'])
    """
    # Get the current working directory
    cwd = os.getcwd()
    print(f"Scanning files in: {cwd}")

    # Find all files with the specified extensions in the CWD
    for root, _, files in os.walk(cwd):
        for file_name in files:
            if any(file_name.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file_name)
                try:
                    # Open the file and replace text
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()

                    for text_to_find, text_to_replace in replacements:
                        content = content.replace(text_to_find, text_to_replace)

                    # Write the updated content back to the file
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(content)

                    print(f"Replacements applied successfully to: {file_path}")
                except UnicodeDecodeError:
                    print(f"Failed to decode {file_path}. Ensure it is a text-based file.")
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")


if __name__ == "__main__":
    # Define the list of replacements (textToFind, textToReplace)
    replacements = [
        ("democrat", "left"),
        ("republican", "right"),
        ("Democrat", "Left"),
        ("Republican", "Right"),
    ]

    # Define the file extensions to process
    file_extensions = ['html', 'css', 'js', 'jsx']  # Add extensions as needed

    # Apply replacements
    replace_text_in_files(replacements, file_extensions)