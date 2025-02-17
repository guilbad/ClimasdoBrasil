<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
</head>
<body>
    <header>
        <h1 align="center">Monitor de Clima</h1>
    </header>
    <div class="container">
        <section>
            <h2>Sobre o Projeto</h2>
            <p>O Monitor de Clima é uma aplicação desenvolvida em Python usando a biblioteca Tkinter. O objetivo é fornecer uma interface gráfica simples para monitorar a temperatura e a umidade de diferentes estados brasileiros. O usuário pode selecionar um estado e visualizar os dados climáticos correspondentes.</p>
        </section>

 <section>
            <h2>Como Funciona</h2>
            <p>A aplicação exibe uma interface gráfica com:</p>
            <ul>
                <li><strong>Um <code>Combobox</code> para selecionar o estado.</strong></li>
                <li><strong>Um botão para obter os dados climáticos.</strong></li>
                <li><strong>Uma área de texto para exibir os resultados.</strong></li>
                <li><strong>Uma imagem do mapa do Brasil.</strong></li>
            </ul>
            <p>Quando o usuário seleciona um estado e clica no botão, os dados de temperatura e umidade são exibidos na área de texto.</p>
   </section>

 <section>
            <h2>Estrutura do Código</h2>
            <p>O código é organizado em várias classes:</p>
            <ul>
                <li><strong><code>MonitorClima</code></strong>: Classe base para monitoramento climático com métodos abstratos para medir e exibir resultados.</li>
                <li><strong><code>MonitorTemperatura</code></strong>: Herda de <code>MonitorClima</code> e implementa os métodos para monitorar a temperatura.</li>
                <li><strong><code>MonitorUmidade</code></strong>: Herda de <code>MonitorClima</code> e implementa os métodos para monitorar a umidade.</li>
                <li><strong><code>MonitorClimaApp</code></strong>: Classe principal da aplicação Tkinter que configura a interface gráfica e exibe dados com base na seleção do estado.</li>
            </ul>
        </section>

   <section>
            <h2>Como Executar</h2>
            <p>Para executar o projeto, certifique-se de ter o Python e a biblioteca Tkinter instalados. Você pode executar o código com o seguinte comando:</p>
            <pre><code>python monitor_clima.py</code></pre>
            <p>Certifique-se de que a imagem <code>mapa-brasil.png</code> está no mesmo diretório do script para que seja carregada corretamente.</p>
        </section>

 <section>
            <h2>Pontos Fortes e Fracos</h2>
            <h3>Pontos Fortes</h3>
            <ul>
                <li><strong>Interface Gráfica Intuitiva:</strong> A aplicação possui uma interface gráfica amigável que facilita a interação do usuário.</li>
                <li><strong>Simples e Direto:</strong> O aplicativo é direto ao ponto, fornecendo informações básicas sobre clima sem complexidade adicional.</li>
                <li><strong>Uso de Tkinter:</strong> Tkinter é uma biblioteca padrão do Python para interfaces gráficas, tornando a aplicação acessível e fácil de instalar.</li>
            </ul>

   <h3>Pontos Fracos</h3>
            <ul>
                <li><strong>Dados Estáticos:</strong> Os dados climáticos são estáticos e não atualizam automaticamente. Para obter informações atualizadas, seria necessário integrar com uma API de clima.</li>
                <li><strong>Não Suporta Vários Estados ao Mesmo Tempo:</strong> A aplicação permite visualizar dados para apenas um estado por vez.</li>
                <li><strong>Tratamento de Erros Básico:</strong> O tratamento de erros é limitado, e a aplicação pode falhar silenciosamente se ocorrerem problemas ao carregar a imagem.</li>
            </ul>
        </section>

 <section>
            <h2>Contribuindo</h2>
            <p>Sinta-se à vontade para contribuir para este projeto. Você pode:</p>
            <ul>
                <li>Enviar pull requests para correções ou melhorias.</li>
                <li>Reportar problemas na seção de issues do repositório.</li>
                <li>Participar de discussões para melhorias futuras.</li>
            </ul>
 </section>

 <section>
            <h2>Licença</h2>
            <p>Este projeto está licenciado sob a Licença MIT - consulte o arquivo <code>LICENSE</code> para obter detalhes.</p>
        </section>
    </div>

<footer>
        <h1 align="center">Contato</h1>
        <p align="left">Para mais informações, entre em contato com os desenvolvedores:</p>
        <ul>
            <li>Douglas Souza Silva - <a href="mailto:ddouglss1999@gmail.com">ddouglss1999@gmail.com</a></li>
            <li>Guilherme Guimarães - <a href="mailto:guiguimaraes906@gmail.com">guiguimaraes906@gmail.com</a></li>
            
 </ul>
        <p>Muito obrigado!</p>
    </footer>
</body>
</html>
