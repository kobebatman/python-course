def add(num1, num2):
	try:
		sum = int(num1) + int(num2)
		return sum
	except TypeError as err:
		return err
		
		
# уг file-ыг шууд ажиллуулж байгаа бол add() function дуудагдана.
# уг file буюу module-ыг өөр нэг газар import хийж байгаа бол __name__ нь "__main__" биш "utility" байх учир add() function ажиллахгүй.
if __name__ == '__main__':
	add(1, 2)