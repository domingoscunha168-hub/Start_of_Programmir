try:
	import matplotlib.pyplot as plt
except Exception:
	plt = None


meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
valores = [10, 25, 18, 30, 22]

if plt:
	
	plt.figure(figsize=(6, 4))
	plt.bar(meses, valores, color='#4C78A8')
	plt.title('Exemplo de gráfico em barras')
	plt.xlabel('Meses')
	plt.ylabel('Valores')
	plt.tight_layout()
	plt.savefig('grafico_exemplo.png')
	print('Gráfico criado e salvo como grafico_exemplo.png')
else:
	try:
		import importlib
		Image = importlib.import_module('PIL.Image')
		ImageDraw = importlib.import_module('PIL.ImageDraw')
		try:
			ImageFont = importlib.import_module('PIL.ImageFont')
		except Exception:
			ImageFont = None

		width, height = 600, 400
		margin = 40
		img = Image.new('RGB', (width, height), 'white')
		draw = ImageDraw.Draw(img)

		max_val = max(valores)
		bar_width = (width - 2 * margin) // len(valores)

		for i, v in enumerate(valores):
			x0 = margin + i * bar_width + 10
			x1 = x0 + bar_width - 20
			y1 = height - margin
			y0 = y1 - int((v / max_val) * (height - 2 * margin))
			draw.rectangle([x0, y0, x1, y1], fill='#4C78A8')
			
			draw.text((x0, y1 + 5), meses[i], fill='black')

		try:
			img.save('grafico_exemplo.png')
			print('matplotlib não encontrado. Gráfico criado com Pillow e salvo como grafico_exemplo.png')
		except Exception as e:
			print('Falha ao salvar imagem com Pillow:', e)
	except Exception:
		print('matplotlib não encontrado. Instale matplotlib (pip install matplotlib) ou Pillow (pip install pillow) para gerar o gráfico.')
