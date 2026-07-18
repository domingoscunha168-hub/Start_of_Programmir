const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function perguntar(pergunta) {
  return new Promise((resolve) => rl.question(pergunta, resolve));
}

async function pedirTexto(pergunta, { vazio = false } = {}) {
  while (true) {
    const valor = (await perguntar(pergunta)).trim();
    if (valor || vazio) return valor;
    console.log('Entrada vazia. Tente novamente.');
  }
}

async function pedirNumero(pergunta, { inteiro = false, min = null, max = null } = {}) {
  while (true) {
    const texto = (await perguntar(pergunta)).trim().replace(',', '.');
    const numero = inteiro ? Number.parseInt(texto, 10) : Number.parseFloat(texto);

    if (Number.isNaN(numero)) {
      console.log('Valor invalido. Informe um numero.');
      continue;
    }

    if (min !== null && numero < min) {
      console.log(`O valor deve ser maior ou igual a ${min}.`);
      continue;
    }

    if (max !== null && numero > max) {
      console.log(`O valor deve ser menor ou igual a ${max}.`);
      continue;
    }

    return numero;
  }
}

function mostrarMenu() {
  console.log('\n=== CENTRAL DE LOGICA ===');
  console.log('1 - Cadastro de pessoas e estatisticas');
  console.log('2 - Calculadora simples');
  console.log('3 - Tabuada');
  console.log('4 - Analise de numeros');
  console.log('5 - Quiz rapido');
  console.log('6 - Jogo de adivinhacao');
  console.log('0 - Sair');
}

function linha() {
  console.log('-'.repeat(40));
}

async function cadastroPessoas() {
  const pessoas = [];
  let maiores18 = 0;
  let homens = 0;
  let mulheresMenores20 = 0;

  while (true) {
    linha();
    const nome = await pedirTexto('Nome: ');
    const idade = await pedirNumero('Idade: ', { inteiro: true, min: 0 });

    let genero = '';
    while (true) {
      genero = (await pedirTexto('Genero [M/F]: ')).toUpperCase();
      if (genero === 'M' || genero === 'F') break;
      console.log('Genero invalido. Use M ou F.');
    }

    pessoas.push({ nome, idade, genero });

    if (idade >= 18) maiores18 += 1;
    if (genero === 'M') homens += 1;
    if (genero === 'F' && idade < 20) mulheresMenores20 += 1;

    const continuar = (await pedirTexto('Deseja continuar? [S/N]: ')).toUpperCase();
    if (continuar !== 'S') break;
  }

  linha();
  console.log('Resultado do cadastro:');
  console.log(`Pessoas cadastradas: ${pessoas.length}`);
  console.log(`Maiores de 18: ${maiores18}`);
  console.log(`Homens: ${homens}`);
  console.log(`Mulheres com menos de 20 anos: ${mulheresMenores20}`);

  if (pessoas.length > 0) {
    console.log('\nLista cadastrada:');
    for (const pessoa of pessoas) {
      console.log(`${pessoa.nome} | ${pessoa.idade} anos | ${pessoa.genero}`);
    }
  }
}

async function calculadora() {
  linha();
  console.log('Calculadora simples');
  const n1 = await pedirNumero('Primeiro numero: ');
  const n2 = await pedirNumero('Segundo numero: ');

  console.log('Operacoes disponiveis:');
  console.log('1 - Soma');
  console.log('2 - Subtracao');
  console.log('3 - Multiplicacao');
  console.log('4 - Divisao');

  const operacao = await pedirNumero('Escolha uma opcao: ', { inteiro: true, min: 1, max: 4 });

  let resultado;

  switch (operacao) {
    case 1:
      resultado = n1 + n2;
      break;
    case 2:
      resultado = n1 - n2;
      break;
    case 3:
      resultado = n1 * n2;
      break;
    case 4:
      if (n2 === 0) {
        console.log('Nao existe divisao por zero.');
        return;
      }
      resultado = n1 / n2;
      break;
    default:
      console.log('Operacao invalida.');
      return;
  }

  console.log(`Resultado: ${resultado}`);
}

async function tabuada() {
  linha();
  const numero = await pedirNumero('Numero da tabuada: ', { inteiro: true });

  for (let i = 1; i <= 10; i += 1) {
    console.log(`${numero} x ${i} = ${numero * i}`);
  }
}

async function analiseNumeros() {
  linha();
  console.log('Digite varios numeros. Para parar, informe "fim".');

  const numeros = [];

  while (true) {
    const texto = await pedirTexto('Numero: ', { vazio: true });
    if (texto.toLowerCase() === 'fim') break;

    const numero = Number.parseFloat(texto.replace(',', '.'));
    if (Number.isNaN(numero)) {
      console.log('Numero invalido.');
      continue;
    }

    numeros.push(numero);
  }

  if (numeros.length === 0) {
    console.log('Nenhum numero foi informado.');
    return;
  }

  let soma = 0;
  let maior = numeros[0];
  let menor = numeros[0];
  let pares = 0;

  for (const numero of numeros) {
    soma += numero;
    if (numero > maior) maior = numero;
    if (numero < menor) menor = numero;
    if (numero % 2 === 0) pares += 1;
  }

  const media = soma / numeros.length;
  console.log(`Quantidade: ${numeros.length}`);
  console.log(`Soma: ${soma}`);
  console.log(`Media: ${media.toFixed(2)}`);
  console.log(`Maior: ${maior}`);
  console.log(`Menor: ${menor}`);
  console.log(`Pares: ${pares}`);
  console.log(`Impares: ${numeros.length - pares}`);
}

async function quizRapido() {
  linha();
  const perguntas = [
    {
      enunciado: 'Qual estrutura repete blocos enquanto a condicao for verdadeira?',
      opcoes: ['A) if', 'B) while', 'C) switch'],
      resposta: 'B',
    },
    {
      enunciado: 'Qual palavra-chave costuma ser usada para criar uma funcao em JavaScript?',
      opcoes: ['A) def', 'B) func', 'C) function'],
      resposta: 'C',
    },
    {
      enunciado: 'Qual metodo imprime informacoes no console?',
      opcoes: ['A) console.log', 'B) print.screen', 'C) echo'],
      resposta: 'A',
    },
  ];

  let pontos = 0;

  for (let i = 0; i < perguntas.length; i += 1) {
    const pergunta = perguntas[i];
    console.log(`\nPergunta ${i + 1} de ${perguntas.length}`);
    console.log(pergunta.enunciado);

    for (const opcao of pergunta.opcoes) {
      console.log(opcao);
    }

    const resposta = (await pedirTexto('Sua resposta: ')).toUpperCase();
    if (resposta === pergunta.resposta) {
      console.log('Correta.');
      pontos += 1;
    } else {
      console.log(`Incorreta. Resposta certa: ${pergunta.resposta}`);
    }
  }

  console.log(`\nVoce acertou ${pontos} de ${perguntas.length} perguntas.`);
}

async function jogoAdivinhacao() {
  linha();
  console.log('Jogo de adivinhacao');

  const segredo = Math.floor(Math.random() * 10) + 1;
  let tentativas = 0;

  while (true) {
    const chute = await pedirNumero('Adivinhe um numero de 1 a 10: ', { inteiro: true, min: 1, max: 10 });
    tentativas += 1;

    if (chute < segredo) {
      console.log('Mais alto.');
    } else if (chute > segredo) {
      console.log('Mais baixo.');
    } else {
      console.log(`Acertou em ${tentativas} tentativa(s).`);
      break;
    }
  }
}

async function main() {
  while (true) {
    mostrarMenu();
    const opcao = await pedirNumero('Escolha uma opcao: ', { inteiro: true, min: 0, max: 6 });

    switch (opcao) {
      case 1:
        await cadastroPessoas();
        break;
      case 2:
        await calculadora();
        break;
      case 3:
        await tabuada();
        break;
      case 4:
        await analiseNumeros();
        break;
      case 5:
        await quizRapido();
        break;
      case 6:
        await jogoAdivinhacao();
        break;
      case 0:
        console.log('Programa encerrado.');
        rl.close();
        return;
      default:
        console.log('Opcao invalida.');
    }
  }
}

main().catch((erro) => {
  console.error('Erro inesperado:', erro);
  rl.close();
});
