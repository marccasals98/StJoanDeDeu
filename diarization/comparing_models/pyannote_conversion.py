from config import PATHS


def pyannote_info():
    """
    Returns a list of tuples with the speaker ID, the start time and the end time.
    
    Arguments: 
    ----------
    (void)

    Returns:
    --------
    ref: list(tuple(str, double, double)) 
        A list of tuples where each element of the list is a tuple that contains the speaker, the start time of speech and the end time.
    """        
    file_path = PATHS['pyannote']  # Replace with the actual path to your file


    hyp = []

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into individual words
            words = line.split()

            # Extract information from the words
            start_time = float(words[0].split('=')[1][:-1])  # Extract and convert start time to float
            stop_time = float(words[1].split('=')[1][:-1])   # Extract and convert stop time to float
            speaker = words[2].split('_')[2]                 # Extract speaker information
            
            # We put all in a list
            instance = (str(speaker), start_time, stop_time)
            hyp.append(instance)
    
    return hyp


