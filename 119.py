#!/usr/bin/env python3
# def compress_domains(domains):
#     compressed_parts = []
#     compressed_string = ""

#     for domain in domains:
#         parts = domain.split('.')
#         for part in parts:
#             length_hex = hex(len(part))[2:].zfill(2)
#             characters_hex = ''.join([hex(ord(char))[2:].zfill(2) for char in part])
#             compressed_parts.append(length_hex + characters_hex)

#     compressed_string = ''.join(compressed_parts)

#     return compressed_string
def compress_domains(domains):
    hex_string = ""
    for domain in domains.split():
        domain_parts = domain.split('.')
        for part in domain_parts:
            hex_string += format(len(part), '02x') + part.encode('utf-8').hex()
        hex_string += "00"
    return hex_string

def compress_with_pointers(domains_list, input_domains):
    compressed_string = compress_domains(input_domains)
    print(f'full hex list: {compressed_string}')
    hex_string = ""
    compressed_with_pointers = ""
    offset = 0

    for domain in domains_list:
        parts = domain.split('.')
        for part in parts:
            current_part = format(len(part), '02x') + part.encode('utf-8').hex()
            print(f'{part} in hex is: {current_part}')
            if current_part in compressed_with_pointers[offset:]:
                pointer_offset = compressed_with_pointers[offset:].index(current_part)
                print(f'offset: {pointer_offset}')
                compressed_with_pointers += current_part
                print(f'building {compressed_with_pointers}')
            else:
                compressed_with_pointers += current_part
                print(compressed_with_pointers)
                offset += len(current_part)
        # for part in parts:
        #     # print(part)
        #     length_hex = hex(len(part))[2:].zfill(2)
        #     characters_hex = ''.join([hex(ord(char))[2:].zfill(2) for char in part])
        #     current_part = length_hex + characters_hex
        #     print(f'hex length and value of {part}: {current_part}')

        #     if current_part in compressed_string[offset:]:
        #         pointer_offset = compressed_string[offset:].index(current_part)
        #         print(f'pointer_offset: {pointer_offset}')
        #         pointer_hex = hex(pointer_offset | 0xC000)[2:].zfill(4)
        #         print(f'pointer_hex: {pointer_hex}')
        #         compressed_with_pointers += pointer_hex
        #         offset += pointer_offset + len(current_part)
        #         print(f'offset: {offset}')
        #     else:
        #         compressed_with_pointers += current_part
        #         offset += len(current_part)

    return compressed_with_pointers


# Example usage:
input_domains = "google.com yahoo.com"
domains_list = input_domains.split()
compressed_result = compress_with_pointers(domains_list, input_domains)

print(f"Original domains: {input_domains}")
print(f"Compressed result: {compressed_result}")
