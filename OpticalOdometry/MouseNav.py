class MouseNav:
	def __init__(self):
		self.angle = 0.0
		self.LX = 0.0
		self.LY = 0.0
		self.RX = 0.0
		self.RY = 0.0

	def calc_dxdy(acc_LX, acc_LY, acc_RX, acc_RY):
		if(acc_LY == acc_RY):
			return acc_LX, acc_LY, acc_RX, acc_RY, 0
		else:
			fixed_distance = 10.0
			if(acc_RY == 0):
				theta = acc_LY / fixed_distance
				left_y = fixed_distance * math.sin(theta)
				left_angle = ( math.pi / 2 ) - ( math.pi - theta ) / 2
				left_x = left_y / math.tan(left_angle)
				right_y = 0
				right_x = 0
			elif(acc_LY == 0):
				theta = -acc_RY / fixed_distance
				right_y = fixed_distance * math.sin(theta)
				right_angle = ( math.pi / 2 ) - ( math.pi - theta ) / 2
				right_x = right_y / math.tan(right_angle)
				left_y = 0
				left_x = 0
			else:
				#first we figure out the x and y values of the arc (accumulated y)
				#re-arrangment of L/R = (r + D) / r
				radius = (fixed_distance * acc_RY) / (acc_LY - acc_RY)
				#angle measurments done in radians
				theta = acc_LY / (fixed_distance + radius)
				left_inner_angle = (math.pi - theta) / 2
				right_inner_angle = (2 * math.pi - 2 * left_inner_angle) / 2
				left_angle = (math.pi / 2) - left_inner_angle
				right_angle = (math.pi / 2) - right_inner_angle

				left_y = (fixed_distance + radius) * math.sin(theta)
				left_x = left_y / math.tan(left_angle)
				right_y = radius * math.sin(theta)
				right_x = right_y / math.tan(right_angle)
			#now we add the accumulated x under the assumption that the x value was accumulated evenly accross the time of the arc
			half_theta = theta / 2
			#in theory acc_LX should always equal acc_RX or atleast be within 1-2 dots
			if(acc_LX == acc_RX):
				X = acc_LX
			else:
				X = (acc_LX + acc_RX) / 2
			shift_x = X * math.cos(half_theta)
			shift_y = X * math.sin(half_theta)
			left_dx = left_x + shift_x
			left_dy = left_y + shift_y
			right_dx = right_x + shift_x
			right_dy = right_y + shift_y

			return left_dx, left_dy, right_dx, right_dy, theta

	def adjust_deltas(left_dx, left_dy, right_dx, right_dy, theta):
		global angle
		global LX
		global LY
		global RX
		global RY
		s = math.sin(angle)
		c = math.cos(angle)
		LX += left_dy * s + left_dx * c
		LY += left_dy * c - left_dx * s
		RX += right_dy * s + right_dx * c
		RY += right_dy * c - right_dx * s
		angle += theta
