# Перевести текст в байты
def text_to_binary(mes):
    bin_mes = ""
    for char in mes:
        num_int = char.encode("utf-8")
        num_bin = bin(num_int[0])[2:]
        num_bin = (8 - len(num_bin))*"0" + num_bin
        bin_mes += num_bin
    return bin_mes

# def text_to_binary(event):
#     return [int(format(ord(elem), 'b')) for elem in event]

# def binary_to_text(event):
#     return [chr(int(str(elem), 2)) for elem in event][0]

# Заменить последний бит
def change_last_bit(width, height, pix, bin_mes, draw):
	count_channels = len(pix[0, 0])
	index = 0
	for x in range(width):
		for y in range(height):
			for z in range(count_channels):
				if index == len(bin_mes):
					return pix
				bit = int(bin_mes[index])
				channel = pix[x, y][z]
				if (bit == 0b0):
					channel &=  ~0b1
				else:
					channel |=  0b1
				channels = list(pix[x, y])
				channels[z] = channel
				channels = tuple(channels)
				draw.point((x, y), channels)
				index += 1

def decode_image(width, height, pix):
	string = ""
	byte = ""
	count_channels = len(pix[0, 0])
	count_bits = 0
	for x in range(width):
		for y in range(height):
			for z in range(count_channels):
				if (count_bits == 8):
					num_int = int(byte, 2)
					num_byte = num_int.to_bytes(1, byteorder="big")
					char = num_byte.decode("utf-8")
					if (char == "@"):
						return string
					string += char
					count_bits = 0
					byte = ""
				channel = pix[x, y][z]
				bit = channel & 0b1
				byte += str(bit)
				count_bits += 1