class No {
    constructor(element) {
        this.value = element;
        this.next = undefined;
    }
}

class Lista {
    constructor() {
        this.head = undefined;
        this.count = 0;
    }

    //outros metodos

    //push() adicionar um elemento no final
    push(element) {
            const node = new No(element); //criando o nó
            let current;
            if (this.head == null) {
                this.head = node;
            } else {
                current = this.head;
                while (current.next != null) {
                    current = current.next;
                }
                current.next = node;
            }
            this.count++;
        }
        //getElementAt(position) retorna um elemento de uma posição especifica da lista
    getElementAt(position) {
            if (position >= 0 && position <= this.count) {
                let node = this.head;
                for (let i = 0; i < position && node != null; i++) {
                    node = node.next;
                }
                return node;
            }
            return undefined;
        }
        //insertAt(element,position) adicionar um elemento em qualquer posição da lista
    insertAt(element, position) {
            if (position > this.count) {
                position = this.count;
            }
            if (position >= 0 && position <= this.count) {
                const node = new No(element);
                if (position === 0) {
                    const current = this.head;
                    node.next = current;
                    this.head = node;
                } else {
                    const previous = this.getElementAt(position - 1);
                    const current = previous.next;
                    node.next = current;
                    previous.next = node;
                }
                this.count++;
                return true;
            }
            return false;
        }
        //remove() remove um elemento da lista


    //indexOf(element) retorna a posição de um elemento da lista

    //removeAt(position) remove um elemento de uma posição especifica da lista
    removeAt(position) {
        if (position >= 0 && position <= this.count) {
            const current = this.head;
            if (position === 0) {
                this.head = current.next;
            } else {
                const previous = this.getElementAt(position - 1);
                const current = previous.next;
                previous.next = current.next;
            }
            this.count--;
            return true;
        }
        return false;
    }

    //isEmpty() checar se a lista está vazia

    //size() retorna o tamanho da lista

}

const lista = new Lista();
lista.push(15);
lista.push(25);
lista.push(30);
console.log(lista);
console.log(JSON.stringify(lista, null, 2));
const terceiro = lista.getElementAt(1);
console.log(terceiro);
lista.insertAt(7, 1); //saida esperada:15,25,7,30
lista.insertAt(333, 7);
lista.insertAt(100, 0);
console.log(JSON.stringify(lista, null, 2));
lista.removeAt(2); //valor 7 sendo retirado da :100,15,7,25,30,333
console.log(JSON.stringify(lista, null, 2));