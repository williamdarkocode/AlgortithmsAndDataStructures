class Node {
    constructor(val, next) {
        this.val = val;
        this.next = next;
    }

    getNext() {
        return this.next;
    }

    getVal() {
        return this.val;
    }

    setVal(inp) {
        this.val = inp;
    }

    setNext(inp) {
        this.next = inp;
    }
}


