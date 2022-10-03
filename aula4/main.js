//Produto -> id, nome, preco
//{id:1, nome: "produto1", preco}

let listaProduto = [
    {id:1, nome:"Produto 1", preco:10},
    {id:2, nome:"Produto 2", preco:20},
    {id:3, nome:"Produto 3", preco:30},
]

let idGerado = 3


function geradorId(){
    return ++idGerado

}

/*function inserir(produto){
    if (produto &&
      produto.nome && produto.preco){
      listaProduto.push(produto)
  }
    else (console.log("ERROR", "FALATA PARAMÊTROS!"))}*/

function inserir(produto){
    produto.id = geradorId()
    listaProduto.push(produto)
    }

function listar(){
    return listaProduto

}

function buscarPorId(id){
    for(let produto of listaProduto){
        if(produto.id == id){
            return produto
        }
    }
    console.log('ERRO', "iD NÃO ENCONTRADO")
}

function atualizar(id, produtoAlterado){
    for(let produto of listaProduto){
        if(produto.id == id){
            if(produtoAlterado.nome){
                produto.nome = produtoAlterado
            }
            if(produtoAlterado.preco){
                produto.preco = produtoAlterado
            }
        }
    }
}

function deletar(id){
   
    for(let i in listaProduto){
        if(listaProduto[i].id == id) {
            listaProduto.splice(i, 1);
        }
    }
       
}

let prod4 = {
    nome: "Produto 4",
    preco: 15

}

inserir(prod4)


console.log("listar",listar())

console.log("buscar por Id=2",buscarPorId(2))

const produtoAlterado = {
    nome: "Produto 1",
    preco: 11
}

atualizar(1, produtoAlterado)
//atualizar(1, {preco = 11})

console.log("listar",listar())