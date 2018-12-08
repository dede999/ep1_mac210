# EP 1 - MAC 0210

## Alunos
* **André Luiz Abdalla Silveira** -> 8030353
* **Bruno Guilherme Ricci Lucas** -> 4460596
* **Eugênio Augusto Jimenes** -> 7118981
## Observações

* Matemática  feita com Numpy
    * Procurou-se utilizar os conceitos aprendidos em sala de aula.
    * Numpy permitiu que se realizasse cálculos mais parrudos, o que
    nos permitiu mais precisão no cálculo dos pontos das curvas.
    * As funções que determinam a função da curva na forma
    a_0*t^n + a_1*t^{n-1}+ ... + a_n e, consequentemente, a que
    determina os pontos dessa curva são feitas com primazia.
    * A função da curva mais próxima do ponto clicada (**_closest1_**),
    por outro lado, não deu tão certo, obrigando-nos a calcular esse
    item da forma mais rude, porém funcional que tínhamos. (**_closest_**)
    * tal decisão de projeto decorre-se do fato de não sabermos se a data
     será prorrogada de fato ou não.
    * O fato de termos muitas provas nessa semana é crucial e agravante
* Parte gráfica com Pygame
    * Utilizamos a biblioteca pygame pela facilidade que ela promove na
    criação de interfaces.
    * A única ferramenta que faltou nessa biblioteca foi uma funcão que
    plotasse as curvas, mas conseguimos resolver isso salvando os pontos
    de cada uma das curvas e traçando um segmento de reta entre cada um
    deles com a função (**_pygame.draw.line()_**), que inclusive já 
    permitia a inclusão da cor desejada para a reta.
    * Usamos o padrão RGB para definir as cores, e decidimos usar a cor
    branca como plano de fundo para o aplicativo para garantir, no começo
    da producão do ep, que o pygame estava funconando corretamente, já
    que a cor padrão do canvas gerado é preto.
    * Encontramos a posição dos cliques usando o event handler do pygame,
    que reconhecia o clique e propiciava a função que fornecia as
    coordenadas x e y do mesmo(editado)
    * A existência da função (**_pygame.display.flip_**), que atualiza o 
    canvas, também foi de grande valia para alterar a cor das curvas. Devido 
    a sua simplicidade, usar pygame se mostrou a decisão correta
    * Botão RESET apaga as curvas existentes e cria novas, sendo o número 
    e o grau delas o mesmo que os do início do programa.
    * Botão ADD adiciona uma nova curva na tela, sendo ela aleatória mas do
     mesmo grau que as demais.
    * Foi tomado um cuidado à mais para que cliques nos botões não mudassem
     as cores das curvas.
    * Os botões foram criados usando a função (**_pygame.Rect()_**), que cria 
    um 
    retângulo de colisão na superfície. Bastou então usar a função 
    (**_pygame.draw.rect()_**), que de fato colore a parte que o retângulo toma 
    na tela para deixar o botão visível. Aí, foi apenas uma questão de usar a 
    combinação (**_myfont.render()_**) e screen.blit para colocar os textos 
    dentro dos retângulos dos botões. A verificação do clique do mouse dentro do 
    botão foi feitas usando a função (**_collidepoint()_**) dos retângulos, que 
    verifica se um ponto está contido no retângulo. O ponto, no caso, são 
    as coordenadas do mouse quando houve um clique. 
* Sobre a programação
    * Usou-se python 3.5
    * No método **_make_points_**, a
    variável delta deve ser alterada
    para balancear desempenho e precisão
* O que ficou de fora?
    * Um menu que permitisse criar curvas a partir de pontos garados por
    cliques
    * A possibilidade de alternar entre um criador de curvas, e um modo
    seletor

## Como funciona

```
# Instalar as dependências
[user] $ sudo pip install numpy
[user] $ sudo pip install pygame
[user] $ sudo pip install scipy.special

# Depois de instalar, rode o arquivo canvas.py

## Para uma configuração padrão *
[user] $ python3.5 canvas.py

## Para uma quantidade variada de curvas de grau 3
[user] $ python3.5 canvas.py (qtde_curvas)

## Para uma quantidade variada de curvas num grau escolhido
[user] $ python3.5 canvas.py (qtde_curvas) (grau)
```
* Configuração padrão cria 5 curvas de Bezier de grau 3
