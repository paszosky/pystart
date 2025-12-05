def draw_triangle(n):
	output = []
	for i in range(n):
		txt = "*" * (i + 1)
		output.append(txt)
	return output

t = draw_triangle(10)
print('\n'.join(t))