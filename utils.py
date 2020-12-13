def load_inputs_as_strings(filename: str) -> [str]:
    """Read the input file and return into a list of strings."""
    with open(filename) as f:
        content = f.read()
        return content.strip().split('\n')

def load_inputs_as_ints(filename: str) -> [int]:
    """Read the input file and return into a list of strings."""
    with open(filename) as f:
        content = f.read()
        return [int(x) for x in content.strip().split('\n')]
        return content.strip().split('\n')

def load_input_as_2d_array(filename: str) -> [int]:
    """Read the input file and return into a 2D array of strings."""
    with open(filename) as f:
        array = []
        
        for line in f:
            array.append(list(line.strip()))
        
        return array