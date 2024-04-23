# Configuration file for WebRPA

# Target website URL
URL = 'https://www.example.com'

# Actions to perform
ACTIONS = [
    {
        'type': 'fill_form',
        'url': 'https://www.example.com/form',
        'data': {
            'name': 'John Doe',
            'email': 'john@example.com'
        }
    },
    {
        'type': 'click_button',
        'url': 'https://www.example.com/button'
    },
    {
        'type': 'extract_table_data',
        'url': 'https://www.example.com/table'
    }
]

# Additional settings
OUTPUT_FILE = 'output.txt'  # Output file for storing the generated data
