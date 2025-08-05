#!/usr/bin/env python3
"""
HotCRP JSON Sanitizer

This script sanitizes JSON exports from HotCRP (conference management system) by removing
sensitive and administrative data fields that should not be published publicly.

The script removes the following sensitive fields:
- email: Author and reviewer email addresses
- pc_conflicts: Program committee conflict information
- metadata: Internal system metadata
- eligible_student_paper_prize: Student prize eligibility status
- talk_poster: Internal talk/poster assignment data
- submitted_at: Submission timestamps
- decision: Editorial decisions (accept/reject)
- status: Internal submission status
- submitted: Submission status flags
- submission: Raw submission data

This allows conference organizers to publish sanitized paper/poster data for public
consumption while protecting sensitive information.
"""

import json
import argparse
import sys
from pathlib import Path

# The keys you want to remove
keys_to_remove = {"email", "pc_conflicts", "metadata", "eligible_student_paper_prize", 
                  "talk_poster", "submitted_at", "decision", "status", "submitted", "submission", "tags", "eligibility_best_student_paper_prize", "full_version"}

def sanitize_data(data):
    """
    Recursively sanitize a dictionary by removing specific keys.
    
    Args:
        data: The data structure to sanitize (dict, list, or primitive)
        
    Returns:
        Sanitized data structure with sensitive keys removed
    """
    if isinstance(data, dict):
        return {key: sanitize_data(value) for key, value in data.items() if key not in keys_to_remove}
    elif isinstance(data, list):
        return [sanitize_data(value) for value in data]
    else:
        return data

def sanitize_json_file(input_file, output_file):
    """
    Read a JSON file, sanitize it, and write the sanitized data to a new JSON file.
    
    Args:
        input_file (str): Path to the input JSON file
        output_file (str): Path to the output JSON file
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        json.JSONDecodeError: If input file is not valid JSON
        PermissionError: If unable to write to output file
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file '{input_file}': {e}", file=sys.stderr)
        sys.exit(1)

    sanitized_data = sanitize_data(data)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sanitized_data, f, indent=4)
        print(f"Successfully sanitized JSON data from '{input_file}' to '{output_file}'")
    except PermissionError:
        print(f"Error: Permission denied writing to '{output_file}'", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to parse arguments and run the sanitization."""
    parser = argparse.ArgumentParser(
        description="Sanitize HotCRP JSON exports by removing sensitive data fields.",
        epilog="""
Examples:
  %(prog)s hotcrp_export.json sanitized_output.json
  %(prog)s data/posters.json public/posters.json
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'input_file',
        help='Input JSON file exported from HotCRP'
    )
    
    parser.add_argument(
        'output_file', 
        help='Output JSON file with sanitized data'
    )
    
    parser.add_argument(
        '--list-removed-keys',
        action='store_true',
        help='List the keys that will be removed during sanitization'
    )
    
    args = parser.parse_args()
    
    if args.list_removed_keys:
        print("Keys that will be removed during sanitization:")
        for key in sorted(keys_to_remove):
            print(f"  - {key}")
        return
    
    # Validate input file exists
    if not Path(args.input_file).exists():
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Run the sanitization
    sanitize_json_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
