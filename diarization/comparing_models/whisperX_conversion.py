from config import PATHS

def whisperX_info():
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

    # create the hypoteshis list 
    hyp = []

    # Open the file and read its contents
    with open(PATHS["whisperX"], 'r') as file:
        for line in file:
            word = line.split()

            # Segment the information:
            speaker = str(word[0])
            start_time = float(word[1].split(',')[0][1:])
            end_time = float(word[2][:-2])

            instance = (speaker, start_time, end_time)

            hyp.append(instance)
    return hyp