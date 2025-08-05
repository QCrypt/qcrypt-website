#!/usr/bin/env python3
"""
Adjust PIDs in JSON files.

This script reads a JSON file containing papers/posters and adds a specified offset 
to all PID values. This is useful for adjusting numbering when merging different 
datasets or avoiding conflicts between different paper categories.
"""

import json
import argparse
import sys
from pathlib import Path

def adjust_pids(input_file, output_file, offset):
    """
    Adjust PIDs in a JSON file by adding an offset to each PID.
    
    Args:
        input_file (str): Path to the input JSON file
        output_file (str): Path to the output JSON file
        offset (int): Number to add to each PID
    """
    # Load the input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Loaded {len(data)} entries from {input_file}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {input_file}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Adjust PIDs
    adjusted_count = 0
    for entry in data:
        if 'pid' in entry:
            old_pid = entry['pid']
            entry['pid'] = old_pid + offset
            adjusted_count += 1
            print(f"Adjusted PID: {old_pid} -> {entry['pid']}")
    
    # Write the adjusted data
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nSuccessfully adjusted {adjusted_count} PIDs and saved to {output_file}")
    except PermissionError:
        print(f"Error: Permission denied writing to '{output_file}'", file=sys.stderr)
        sys.exit(1)
    
    # Summary
    print(f"\nSummary:")
    print(f"  Input file: {input_file}")
    print(f"  Output file: {output_file}")
    print(f"  Offset applied: +{offset}")
    print(f"  Entries adjusted: {adjusted_count}")
    print(f"  Total entries: {len(data)}")

def main():
    """Main function to parse arguments and run the PID adjustment."""
    parser = argparse.ArgumentParser(
        description="Adjust PIDs in JSON files by adding a specified offset.",
        epilog="""
Examples:
  %(prog)s posters.json posters-adjusted.json 100
  %(prog)s --offset 50 input.json output.json
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'input_file',
        help='Input JSON file containing entries with PIDs'
    )
    
    parser.add_argument(
        'output_file', 
        help='Output JSON file for the adjusted data'
    )
    
    parser.add_argument(
        'offset',
        type=int,
        nargs='?',
        default=100,
        help='Number to add to each PID (default: 100)'
    )
    
    parser.add_argument(
        '--offset',
        type=int,
        dest='offset_flag',
        help='Alternative way to specify the offset'
    )
    
    args = parser.parse_args()
    
    # Use --offset flag if provided, otherwise use positional argument
    offset = args.offset_flag if args.offset_flag is not None else args.offset
    
    # Validate input file exists
    if not Path(args.input_file).exists():
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Run the adjustment
    adjust_pids(args.input_file, args.output_file, offset)

if __name__ == "__main__":
    main()
