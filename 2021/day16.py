from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace


example = """
D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780
F600BC2D8F
9C005AC2F8F0
9C0141080250320F1802104A08
"""

actual = """
C20D7900A012FB9DA43BA00B080310CE3643A0004362BC1B856E0144D234F43590698FF31D249F87B8BF1AD402389D29BA6ED6DCDEE59E6515880258E0040A7136712672454401A84CE65023D004E6A35E914BF744E4026BF006AA0008742985717440188AD0CE334D7700A4012D4D3AE002532F2349469100708010E8AD1020A10021B0623144A20042E18C5D88E6009CF42D972B004A633A6398CE9848039893F0650048D231EFE71E09CB4B4D4A00643E200816507A48D244A2659880C3F602E2080ADA700340099D0023AC400C30038C00C50025C00C6015AD004B95002C400A10038C00A30039C0086002B256294E0124FC47A0FC88ACE953802F2936C965D3005AC01792A2A4AC69C8C8CA49625B92B1D980553EE5287B3C9338D13C74402770803D06216C2A100760944D8200008545C8FB1EC80185945D9868913097CAB90010D382CA00E4739EDF7A2935FEB68802525D1794299199E100647253CE53A8017C9CF6B8573AB24008148804BB8100AA760088803F04E244480004323BC5C88F29C96318A2EA00829319856AD328C5394F599E7612789BC1DB000B90A480371993EA0090A4E35D45F24E35D45E8402E9D87FFE0D9C97ED2AF6C0D281F2CAF22F60014CC9F7B71098DFD025A3059200C8F801F094AB74D72FD870DE616A2E9802F800FACACA68B270A7F01F2B8A6FD6035004E054B1310064F28F1C00F9CFC775E87CF52ADC600AE003E32965D98A52969AF48F9E0C0179C8FE25D40149CC46C4F2FB97BF5A62ECE6008D0066A200D4538D911C401A87304E0B4E321005033A77800AB4EC1227609508A5F188691E3047830053401600043E2044E8AE0008443F84F1CE6B3F133005300101924B924899D1C0804B3B61D9AB479387651209AA7F3BC4A77DA6C519B9F2D75100017E1AB803F257895CBE3E2F3FDE014ABC
"""


def solve(inp):
    inp = inp.strip().split('\n')
    for i in inp:
        binary = ''.join(map(to_binary, i))
        print(f'{i}: {parse_packetb(binary)}')
    

def parse_packet(binary):
    version = from_binary(binary[0:3])
    type_id = from_binary(binary[3:6])

    if type_id == 4:
        value, end = parse_literal(binary[6:])
        end += 6
        return [version], end
    else:
        length_type = binary[6]
        if length_type == '0':
            subpacket_length = from_binary(binary[7:22])
            start = 22
            end = 22
            versions = [version]
            while end < subpacket_length + 22:
                v, e = parse_packet(binary[start:])
                end = e + start
                start = end
                versions.extend(v)
            return versions, end
        else:
            num_subpackets = from_binary(binary[7:18])
            start = 18
            end = 18
            versions = [version]
            num_parsed = 0
            while num_parsed < num_subpackets:
                v, e = parse_packet(binary[start:])
                end = e + start
                start = end
                versions.extend(v)
                num_parsed += 1
            return versions, end


def parse_packetb(binary):
    version = from_binary(binary[0:3])
    type_id = from_binary(binary[3:6])

    if type_id == 4:
        value, end = parse_literal(binary[6:])
        end += 6
        return value, end
    else:
        length_type = binary[6]
        values = []
        end = 0
        if length_type == '0':
            subpacket_length = from_binary(binary[7:22])
            start = 22
            end = 22
            while end < subpacket_length + 22:
                v, e = parse_packetb(binary[start:])
                end = e + start
                start = end
                values.append(v)
        else:
            num_subpackets = from_binary(binary[7:18])
            start = 18
            end = 18
            num_parsed = 0
            while num_parsed < num_subpackets:
                v, e = parse_packetb(binary[start:])
                end = e + start
                start = end
                values.append(v)
                num_parsed += 1
        if type_id == 0:
            return sum(values), end
        elif type_id == 1:
            return prod(values), end
        elif type_id == 2:
            return min(values), end
        elif type_id == 3:
            return max(values), end
        elif type_id == 5:
            return int(values[0] > values[1]), end
        elif type_id == 6:
            return int(values[0] < values[1]), end
        elif type_id == 7:
            return int(values[0] == values[1]), end
        assert False


def parse_literal(bin_str):
    parts = []
    end = 0
    for i in range(int(len(bin_str)/5)):
        group = bin_str[i * 5: i * 5 + 5]
        parts.append(group[1:])
        if group[0] == '0':
            end = i * 5 + 5
            break
    return from_binary(''.join(parts)), end


def to_binary(char):
    return bin(int(char, 16))[2:].zfill(4)


def from_binary(binary_str):
    return int(binary_str, 2)


if __name__=='__main__':
    example_ans = solve(example)
    print(f'example:\n {example_ans}')

    actual_ans = solve(actual)
    print(f'actual:\n {actual_ans}')

