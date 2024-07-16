#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return
    
    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendees in enumerate(attendees, start=1):
        processed_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:

            value = attendees.get(key, 'N/A') if attendees.get(key) is not None else 'N/A'
            if key == 'even_date' and value == 'N/A':
                value = "event_date: N/A"

            value = attendees.get(key, 'N/A') if attendees.get(key) is not None else 'N/A'
            processed_template = processed_template.replace(f'{{{key}}}', value)

        output_filename = f'output_{idx}.txt'

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
        print("Generate {}".format(output_filename))