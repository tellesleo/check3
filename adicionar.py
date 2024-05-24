# Rota para a página de adição de produtos
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        codigo_produto = request.form['codigo_produto']
        nome_produto = request.form['nome_produto']
        preco_produto = request.form['valor_produto']
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO produto (codigo, nome, valor) VALUES (%s, %s, %s)", (codigo_produto, nome_produto, valor_produto))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))
    return render_template('adicionar.html')
