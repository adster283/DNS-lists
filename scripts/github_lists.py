import requests

def fetch_filter_and_save(url, output_file):
    # Fetch the content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Split the content into lines
        lines = response.text.splitlines()
        
        # Filter out lines starting with '#'
        filtered_lines = [line for line in lines if not line.strip().startswith('#')]
        
        # Join the filtered lines back into a single string
        filtered_content = '\n'.join(filtered_lines)
        
        # Save the filtered content to a file
        with open(output_file, 'w') as file:
            file.write(filtered_content)
        
        print(f"Filtered content saved to {output_file}")
    else:
        print(f"Failed to fetch the file. Status code: {response.status_code}")

# Example usage
url = "https://raw.githubusercontent.com/hagezi/dns-blocklists/refs/heads/main/domains/light.txt"
output_file = "filtered_output.txt"
fetch_filter_and_save(url, output_file)