#!/usr/bin/env python3
import argparse

def convert_domains_to_option_119(domains):
  compressed_data = bytearray()
  pointers = {}

  for domain in domains:
    parts = domain.lower().split('.')
    for part in parts:
      if part in pointers:
        pointer = pointers[part]
        compressed_data.extend([0xc0, 0x00 | pointer])
      else:
        pointers[part] = len(compressed_data)
        compressed_data.extend([len(part), *[ord(char) for char in part]])
    compressed_data.append(0x00)

  return compressed_data.hex().upper()

def format_as_windows(hex_string):
    byte_string = " ".join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])
    return byte_string

def format_as_meraki(hex_string):
    byte_string = ":".join([hex_string[i:i+2] for i in range(0, len(hex_string), 2)])
    return byte_string

def format_as_cisco(hex_string):
    byte_string = ".".join([hex_string[i:i+4] for i in range(0, len(hex_string), 4)])
    return byte_string

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("domain_input", nargs='+', help="Enter the domain name or names as space seperated")
    args = parser.parse_args()
    domain_list = ' '.join(args.domain_input)
    print(f'Domain list: {domain_list}')
    option_119_hex = convert_domains_to_option_119(args.domain_input)
    meraki_119_string = format_as_meraki(option_119_hex)
    windows_119_string = format_as_windows(option_119_hex)
    cisco_119_string = format_as_cisco(option_119_hex)
    print(f'Meraki: {meraki_119_string}')
    print(f'Windows: {windows_119_string}')
    print(f'Cisco: {cisco_119_string}')
