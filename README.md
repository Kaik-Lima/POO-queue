# POO-queue

<h3>Leetcode na transformação de queue para stacks.</h3>
<p>Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should <strong>support all the function</strong>s of a normal stack (push, top, pop, and empty).</p>

<h3>Implement the MyStack class:</h3>

<strong>void push(int x)</strong> Pushes element x to the top of the stack.<br>
<strong>int pop()</strong> Removes the element on the top of the stack and returns it.<br>
<strong>int top()</strong> Returns the element on the top of the stack.<br>
<strong>boolean empty()</strong> Returns true if the stack is empty, false otherwise.<br><br>

<em>Notes:<br>
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.</em>
 

<strong>Input</strong><br>
["MyStack", "push", "push", "top", "pop", "empty"]<br>
[[], [1], [2], [], [], []]<br><br>
<strong>Output</strong><br>
[null, null, null, 2, 2, false]
