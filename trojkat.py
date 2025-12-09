prev_globals = set(globals().keys())
def print_diff_globals():
	global prev_globals
	x = set(globals().keys())
	print(x - prev_globals)
	prev_globals = x

def draw_triangle(n):
	print("LOCALS", locals())
	output = []
	print("LOCALS", locals())
	for i in range(n):
		print("LOCALS", locals())
		txt = "*" * (i + 1)
		print("LOCALS", locals())
		output.append(txt)
	print("LOCALS", locals())
	return output

print_diff_globals()
t = draw_triangle(10)
print_diff_globals()
print('\n'.join(t))
print_diff_globals()