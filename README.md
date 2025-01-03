# Simulação de Partículas Coloridas

Este projeto é uma simulação interativa de partículas coloridas que se movem, consomem energia, coletam recursos e interagem em um ambiente 2D. O objetivo é explorar como diferentes características das partículas influenciam sua sobrevivência e reprodução.

---

## Funcionalidades Atuais

1. **Movimentação Aleatória**:
   - As partículas se movem aleatoriamente pelo ambiente, consumindo energia.

2. **Coleta de Recursos (Alimentos)**:
   - As partículas podem coletar alimentos para recuperar energia.
   - Cada cor tem uma taxa de coleta específica:
     - **Vermelho**: Coleta mais rápido, mas consome mais energia.
     - **Azul**: Coleta em ritmo normal e consome menos energia.
     - **Verde**: Coleta mais devagar, com consumo de energia moderado.

3. **Energia**:
   - Energia é consumida a cada movimento.
   - Quando a energia chega a zero, a partícula é removida da simulação.

4. **Alimentos**:
   - Representados por pequenos círculos verdes que aparecem aleatoriamente no ambiente.
   - Os alimentos são consumidos quando uma partícula se aproxima o suficiente.

---

## Como Executar

1. **Requisitos**:
   - Python 3.8 ou superior.
   - Bibliotecas:
     ```bash
     pip install pygame numpy matplotlib
     ```

2. **Execução**:
   - Execute o script principal:
     ```bash
     python main.py
     ```

---

## Estrutura do Projeto

```
projeto_simulacao/
├── main.py          # Arquivo principal
├── biomas.py        # Lógica dos biomas (a implementar)
├── particulas.py    # Classe das partículas (a implementar)
├── estruturas.py    # Lógica de estruturas e pedreiras (a implementar)
├── recursos.py      # Regras de alimentos e materiais (a implementar)
├── utils.py         # Funções utilitárias (a implementar)
└── assets/          # Imagens ou sprites (opcional)
```

---

## Planejamento Futuro

1. **Adicionais**:
   - Reprodução com ovos que levam tempo para gerar novas partículas.
   - Pedreiras para coleta de materiais de construção.
   - Estruturas criadas pelas partículas para proteger ovos e monopolizar recursos.

2. **Biomas**:
   - Ambientes variados que influenciam a geração de recursos e as características dos descendentes.

3. **Troca de Recursos**:
   - Permitir interações sociais entre partículas, como troca de materiais por comida.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com sugestões e melhorias.

---

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Divirta-se explorando o mundo das partículas coloridas e suas interações!

