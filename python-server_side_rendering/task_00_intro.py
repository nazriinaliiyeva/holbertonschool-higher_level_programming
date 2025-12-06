import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: template should be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees should be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation_text = template

        # Replace placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) if attendee.get(key) else "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", value)

        # Define output file name
        output_file = f"output_{index}.txt"

        # Write to file with error handling
        try:
            with open(output_file, 'w') as f:
                f.write(invitation_text)
            print(f"Generated: {output_file}")
        except Exception as e:
            print(f"Error writing {output_file}: {e}")

