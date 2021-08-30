class Canvas:
	def __init__(self, width, height):
		self.Width = width
		self.Height = height
		self.ScreenData = []

	def Initialize(self):
		for y in range(self.Height):
			self.ScreenData.append([])
			for x in range(self.Width):
				self.ScreenData[y].append(" ")

	def DrawCanvas(self):
		for y in self.ScreenData:
			print("".join(y))

	def DrawString(self, text, x, y):
		currentY = y
		currentX = x

		currentchar = 0
		while currentchar < len(text):
			if not text[currentchar] == "\n":
				self.ScreenData[currentY][currentX] = text[currentchar]
			else:
				currentX = x-1
				currentY = currentY + 1
			currentX = currentX + 1
			currentchar = currentchar + 1