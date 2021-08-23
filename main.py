from kivy.app import App
class calcApp(App):
	def calculate(self, tocalc):
		try:
			result=eval(tocalc)
		except:
			return 'error'
		return str(result)
if __name__=='__main__':
	calcApp().run()