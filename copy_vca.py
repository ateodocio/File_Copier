# Created by Aena Teodocio. May 22, 2022.

# Imports
import os
import shutil


# Functions
def open_file(file):
    """
    Opens a file. Raises an AssertionError if expected parameters are not present.
    Returns a list of strings (text from input_file).

    Expected parameters:
    "source= path_to_file"
    "destination= path_to_file_or_directory"
    "create= filename1, filename2..."

    file (str): an input file name containing the file_copier parameters.

    """
    try:
        input_file = open(file, 'r')
        input_lines = input_file.read().replace(' ', '')
    except:
        return 'Error in reading file.'

    # Check for completeness in parameters
    assert 'source=' in input_lines, 'Missing source path. Could not find "source= path_to_file".'
    assert 'destination=' in input_lines, 'Missing destination path. Could not find "destination= path_to_file_or_directory".'
    assert 'create=' in input_lines, 'Missing names for new folder & file to create. Could not find "create= filename1, filename2..."'

    # Pass on input_lines since there parameters are complete
    input_lines = input_lines.splitlines()
    return input_lines


def read_input(input_lines):
    """
    Returns a dictionary where the keys are the parameter type.
    input_lines (list of strings): text from input_file containing parameters.
    """

    file_dict = {}

    # Extract source path, destination path, and new file names from input file.
    for line in input_lines:
        if line == '':
            continue
        elif 'source' or 'destination' or 'create' in line:
            curr_line = line.split('=')
            file_dict[curr_line[0]] = curr_line[1]
        else:
            continue

    return file_dict


def create_dir(path):
    """
    Creates a directory with the given directory name.
    Raises an AssertionError if given directory already exists.

    path (str): represents a new directory to be created.
    """
    assert not os.path.exists(path), "Directory already existed : {}".format(path)

    if not os.path.exists(path):
        os.makedirs(path)
        print("Created Directory : ", path)


def file_copier(input_file):
    """
    Creates a copy of a .vca file into a new folder using the given naming convention from input_file.
    Number of copies depend on number of file names given in the "create= " parameter.

    input_file (str): file name containing the copying parameters.
    """
    input_lines = open_file(input_file)
    file_dict = read_input(input_lines)

    create_file_names = file_dict['create'].split(',')

    for name in create_file_names:
        new_folder_path = file_dict['destination'] + name

        create_dir(new_folder_path)

        try:
            new_file_name = os.path.join(file_dict['destination'], name, name + '.vca')
            shutil.copy(file_dict['source'], new_file_name)
            print('File has been copied.')
        except shutil.SameFileError:
            print('Source and destination are the same file.')
        except PermissionError:
            print('Permission denied. Destination is not writable.')
        except shutil.Error as e:
            print('An error occurred.')
            print(e)


if __name__ == '__main__':
    file_name = input('Enter input file path (.txt): ')
    file_copier(file_name)



