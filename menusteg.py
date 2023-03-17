import mystegrar as msr
import mystegpyth as msp
try:
	ch=int(input('Do you want to compress the file:\nPress "1"'))
	if ch==1:
		msp.mymainsteg()
	else:
		pass
except Exception as e:
	print(str(e))
finally:
	input('Exit')