// ============================================================================
// Implementation Exercise: Stack
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Stack and all of its methods below!
//
// ------------
// Constraints:
// ------------
//
// Make sure the time and space complexity of each is equivalent to those 
// in the table provided in the Time and Space Complexity Analysis section
// of your Stack reading!
//
// -----------
// Let's Code!
// -----------

class Node {
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor(){
    this.top = null;
    this.bottom =  null;
    this.length = 0;
  }

  pop(){
    const removed = this.top;
    if (this.length > 1){
      this.length--;
      this.top = this.top.next;
      return removed.value;
    } else if (this.length === 1){
      this.length = 0;
      this.top = null;
      this.bottom = null;
      return removed.value;
    }
    return null;
  }
  
  push(val){
    let n = new Node(val);
    n.next = this.top;
    switch (this.length) {
      case 0:
        this.top = n;
        this.bottom = n;
        break;
      default:
        this.top = n;
        break;
    }
    this.length++;
    return this.length;
  }

  size(){
    return this.length
  }
}

exports.Node = Node;
exports.Stack = Stack;
