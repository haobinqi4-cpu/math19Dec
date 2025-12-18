"""
Module 1: Input-Process-Output Model - Exercises
For MSc Mathematics Students
"""

# ===================================================================
# Exercise 1: Temperature Converter
# ===================================================================

def temperature_converter():
    """
    IPO Example: Convert Celsius to Fahrenheit
    
    INPUT: Temperature in Celsius
    PROCESS: Apply conversion formula
    OUTPUT: Display both temperatures
    """
    # INPUT
    celsius = float(input("Enter temperature in Celsius: "))
    
    # PROCESS
    fahrenheit = (celsius * 9/5) + 32
    
    # OUTPUT
    print(f"{celsius}°C = {fahrenheit}°F")


# ===================================================================
# Exercise 2: Grade Calculator
# ===================================================================

def grade_calculator():
    """
    IPO Example: Calculate grade statistics
    
    INPUT: List of student scores
    PROCESS: Calculate average, min, max
    OUTPUT: Display statistics
    """
    # INPUT
    scores = [85, 92, 78, 90, 88, 76, 95, 89]
    print(f"Student Scores: {scores}")
    
    # PROCESS
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    # OUTPUT
    print(f"\n--- Grade Statistics ---")
    print(f"Average Score: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Range: {highest - lowest}")


# ===================================================================
# Exercise 3: Text Analysis
# ===================================================================

def text_analyzer(filename="sample.txt"):
    """
    IPO Example: Analyze text file
    
    INPUT: Text file
    PROCESS: Count words, characters, lines
    OUTPUT: Display statistics
    """
    try:
        # INPUT
        with open(filename, 'r') as file:
            content = file.read()
        
        # PROCESS
        num_characters = len(content)
        num_words = len(content.split())
        num_lines = content.count('\n') + 1
        
        # OUTPUT
        print(f"\n--- Text Analysis ---")
        print(f"File: {filename}")
        print(f"Characters: {num_characters}")
        print(f"Words: {num_words}")
        print(f"Lines: {num_lines}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# ===================================================================
# Exercise 4: List Statistics
# ===================================================================

def list_statistics(numbers):
    """
    IPO Example: Calculate statistics for a list of numbers
    
    INPUT: List of numbers
    PROCESS: Calculate mean, median, std deviation
    OUTPUT: Return statistics dictionary
    """
    # INPUT (parameter)
    n = len(numbers)
    
    # PROCESS
    mean = sum(numbers) / n
    sorted_nums = sorted(numbers)
    
    # Calculate median
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5
    
    # OUTPUT
    return {
        'mean': mean,
        'median': median,
        'std_dev': std_dev,
        'min': min(numbers),
        'max': max(numbers)
    }


# ===================================================================
# Exercise 5: Data Pipeline
# ===================================================================

def simple_data_pipeline(data_list):
    """
    IPO Example: Complete data processing pipeline
    
    INPUT: Raw data list
    PROCESS: Clean, transform, aggregate
    OUTPUT: Processed results
    """
    # INPUT
    print(f"Raw Data: {data_list}")
    
    # PROCESS 1: Clean data (remove None values)
    cleaned_data = [x for x in data_list if x is not None]
    
    # PROCESS 2: Transform (multiply by 2)
    transformed_data = [x * 2 for x in cleaned_data]
    
    # PROCESS 3: Aggregate (sum)
    total = sum(transformed_data)
    
    # OUTPUT
    result = {
        'original_count': len(data_list),
        'cleaned_count': len(cleaned_data),
        'transformed_data': transformed_data,
        'total': total
    }
    
    return result


# ===================================================================
# Main Execution
# ===================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Module 1: Input-Process-Output Examples")
    print("=" * 60)
    
    # Example 1
    print("\n[1] Temperature Converter")
    print("Convert 25°C to Fahrenheit:")
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
    
    # Example 2
    print("\n[2] Grade Calculator")
    grade_calculator()
    
    # Example 3
    print("\n[3] List Statistics")
    numbers = [12, 15, 18, 20, 22, 25, 28]
    stats = list_statistics(numbers)
    print(f"Numbers: {numbers}")
    print(f"Statistics: {stats}")
    
    # Example 4
    print("\n[4] Data Pipeline")
    raw_data = [5, None, 10, 15, None, 20]
    result = simple_data_pipeline(raw_data)
    print(f"Pipeline Result: {result}")
    
    print("\n" + "=" * 60)
    print("All exercises completed!")
    print("=" * 60)

