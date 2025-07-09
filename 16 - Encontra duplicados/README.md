# 16 - Encontra duplicados

Este código foi criado para identificar dois números repetidos dentro de uma lista de números inteiros. Imagine que temos várias listas diferentes e queremos saber se, em cada uma delas, há dois elementos que aparecem mais de uma vez.

A função chamada encontrar_duplicados faz essa verificação. Ela começa assumindo que não há nenhum número duplicado, e usa duas variáveis para armazenar possíveis repetições, chamadas duplicado1 e duplicado2. Também cria uma espécie de “caixa de memória” chamada checados, que guarda os números já vistos.

À medida que percorre a lista:

Se encontra um número que já foi visto antes e ainda não encontrou nenhum duplicado, ele registra esse número como o primeiro duplicado.

Se encontra outro número repetido, diferente do primeiro, ele registra esse como o segundo duplicado e para imediatamente, retornando os dois.

No final, se não encontrar dois duplicados, retorna o que tiver encontrado (podendo ser apenas um ou nenhum).

Depois disso, o código percorre as outras sequencias de numeros inteiros e aplica essa verificação em cada uma. Para cada lista, ele exibe os seus elementos e os seus duplicados (se houverem)