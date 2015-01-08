#coding: utf-8
import numpy as np

Numbers = np.array([[1, 0, 0, 0],
					[0, 0, 0, 0],
					[0, 4, 0, 2],
					[0, 0, 3, 0]])
while(0 in Numbers):
	for x in range(4): #横一列
		for y in range(4): #縦一列
			if(x == 0 or x == 1): #ブロックの配分
				if(y == 0 or y == 1):
					block = 1;
				else:
					block = 2;
			else:
				if(y == 0 or y == 1):
					block = 3;
				else:
					block = 4;

			imNum = [1, 2, 3, 4]

			for a in range(1, 5):
				if(block == 1):
					if(a in Numbers[x] or a in Numbers[:, y] or
						a in Numbers[:2, :2]):
					imNum.remove(a)
				elif(block == 2):
					if(a in Numbers[x] or a in Numbers[:, y] or
						a in Numbers[:2, 2:4]):
					imNum.remove(a)
				elif(block == 3):
					if(a in Numbers[x] or a in Numbers[:, y] or
						a in Numbers[2:4, :2]):
					imNum.remove(a)
				else:
					if(a in Numbers[x] or a in Numbers[:, y] or
						a in Numbers[2:4, 2:4]):
					imNum.remove(a)

				if(len(imNum) == 1):
					if(Numbers[x][y] == 0):
						Numbers[x][y] = imNum[0]
				else:
					pass

print Numbers

