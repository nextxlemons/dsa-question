def determine_color(s):
    """
    Write your logic here to determine the color based on the string s.
    Parameters:
        s (str): Input string representing a position.
    Returns:
    """
    x ="abcdefgh".index(s[0]) + 1
    y = int(s[1])

    return "Black" if (x + y) % 2 == 0 else "White"

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the input string
    
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()